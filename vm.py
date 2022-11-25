#
import argparse
from pathlib import Path
from typing import Union

from compiler.execution import ExecutionStack
from compiler.execution import FunctionCall
from compiler.execution import FunctionDirectory
from compiler.execution import FunctionParameterStack
from compiler.execution import GlobalScope
from compiler.execution import GlobalMemory
from compiler.execution import ProgramCounterStack
from compiler.execution import Quadruple
from compiler.execution import QuadrupleList
from compiler.execution import ResolvedVariable
from compiler.execution import VariableScope
from compiler.execution import VirtualMemoryAddressResolver
from compiler.files import IntermediateCodeFileReader
from compiler.operators import Operator
from compiler.variables import Type

global_scope = None
function_directory = None
quadruple_list = None

execution_stack = None
program_counter_stack = None
function_parameter_stack = None

function = None
function_call = None

program_counter = 0

class InvalidFileExtensionError(RuntimeError):
    pass


def get_base_virtual_memory_address(virtual_memory_address: int) -> int:
    return VirtualMemoryAddressResolver.get_base_virtual_memory_address(virtual_memory_address)


def resolve_base_virtual_memory_address(base_virtual_memory_address: int) -> tuple[str, Type]:
    return VirtualMemoryAddressResolver.resolve_virtual_memory_address(base_virtual_memory_address)


def get_variable_index(virtual_memory_address: int) -> int:
    return VirtualMemoryAddressResolver.get_index(virtual_memory_address)


def resolve_virtual_memory_address(virtual_memory_address: int) -> ResolvedVariable:
    # Get variable index
    # Extract variable scope and type from base virtual memory address
    scope, type, index = resolve_base_virtual_memory_address(virtual_memory_address)

    return ResolvedVariable(scope, type, index)


def dispatch_assignment(quadruple: Quadruple) -> None:
    result_virtual_memory_address = int(quadruple.get_q2())
    storage_virtual_memory_address = int(quadruple.get_q4())

    resolved_result_variable = resolve_virtual_memory_address(result_virtual_memory_address)
    resolved_storage_variable = resolve_virtual_memory_address(storage_virtual_memory_address)

    value = get_variable_value(resolved_result_variable)
    set_variable_value(resolved_storage_variable, value)


def dispatch_addition(quadruple: Quadruple) -> None:            
    left_operand_virtual_memory_address = int(quadruple.get_q2())
    right_operand_virtual_memory_address = int(quadruple.get_q3())
    result_virtual_memory_address = int(quadruple.get_q4())

    left_operand_resolved_variable = resolve_virtual_memory_address(
        left_operand_virtual_memory_address
    )
    right_operand_resolved_variable = resolve_virtual_memory_address(
        right_operand_virtual_memory_address
    )
    result_resolved_variable = resolve_virtual_memory_address(
        result_virtual_memory_address
    )

    left_value = get_variable_value(left_operand_resolved_variable)
    right_value = get_variable_value(right_operand_resolved_variable)
    result_value = left_value + right_value

    set_variable_value(result_resolved_variable, result_value)


def dispatch_subtraction(quadruple: Quadruple) -> None:
    left_operand_virtual_memory_address = int(quadruple.get_q2())
    right_operand_virtual_memory_address = int(quadruple.get_q3())
    result_virtual_memory_address = int(quadruple.get_q4())

    left_operand_resolved_variable = resolve_virtual_memory_address(
        left_operand_virtual_memory_address
    )
    right_operand_resolved_variable = resolve_virtual_memory_address(
        right_operand_virtual_memory_address
    )
    result_resolved_variable = resolve_virtual_memory_address(
        result_virtual_memory_address
    )

    left_value = get_variable_value(left_operand_resolved_variable)
    right_value = get_variable_value(right_operand_resolved_variable)
    result_value = left_value - right_value

    set_variable_value(result_resolved_variable, result_value)


def dispatch_multiplication(quadruple: Quadruple) -> None:
    left_operand_virtual_memory_address = int(quadruple.get_q2())
    right_operand_virtual_memory_address = int(quadruple.get_q3())
    result_virtual_memory_address = int(quadruple.get_q4())

    left_operand_resolved_variable = resolve_virtual_memory_address(
        left_operand_virtual_memory_address
    )
    right_operand_resolved_variable = resolve_virtual_memory_address(
        right_operand_virtual_memory_address
    )
    result_resolved_variable = resolve_virtual_memory_address(
        result_virtual_memory_address
    )

    left_value = get_variable_value(left_operand_resolved_variable)
    right_value = get_variable_value(right_operand_resolved_variable)
    result_value = left_value * right_value

    set_variable_value(result_resolved_variable, result_value)


def dispatch_division(quadruple: Quadruple) -> None:
    left_operand_virtual_memory_address = int(quadruple.get_q2())
    right_operand_virtual_memory_address = int(quadruple.get_q3())
    result_virtual_memory_address = int(quadruple.get_q4())

    left_operand_resolved_variable = resolve_virtual_memory_address(
        left_operand_virtual_memory_address
    )
    right_operand_resolved_variable = resolve_virtual_memory_address(
        right_operand_virtual_memory_address
    )
    result_resolved_variable = resolve_virtual_memory_address(
        result_virtual_memory_address
    )

    left_value = get_variable_value(left_operand_resolved_variable)
    right_value = get_variable_value(right_operand_resolved_variable)
    result_value = left_value // right_value

    set_variable_value(result_resolved_variable, result_value)


def dispatch_modulo(quadruple: Quadruple) -> None:
    left_operand_virtual_memory_address = int(quadruple.get_q2())
    right_operand_virtual_memory_address = int(quadruple.get_q3())
    result_virtual_memory_address = int(quadruple.get_q4())

    left_operand_resolved_variable = resolve_virtual_memory_address(
        left_operand_virtual_memory_address
    )
    right_operand_resolved_variable = resolve_virtual_memory_address(
        right_operand_virtual_memory_address
    )
    result_resolved_variable = resolve_virtual_memory_address(
        result_virtual_memory_address
    )

    left_value = get_variable_value(left_operand_resolved_variable)
    right_value = get_variable_value(right_operand_resolved_variable)
    result_value = left_value % right_value

    set_variable_value(result_resolved_variable, result_value)


def dispatch_read(quadruple: Quadruple) -> None:
    # Get variable virtual memory address
    variable_virtual_memory_address = int(quadruple.get_q4())
    # Resolve virtual memory address
    resolved_variable = resolve_virtual_memory_address(variable_virtual_memory_address)

    # Read value from console
    reading_value = input()

    # Cast value to target type
    casted_value = cast_constant(reading_value, resolved_variable.type)

    set_variable_value(resolved_variable, casted_value)


def dispatch_print(quadruple: Quadruple) -> None:
    # Get variable virtual memory address
    variable_virtual_memory_address = int(quadruple.get_q4())
    # Resolve virtual memory address
    resolved_variable = resolve_virtual_memory_address(variable_virtual_memory_address)

    printed_value = get_variable_value(resolved_variable)

    # Print value
    print(printed_value)


def dispatch_store_constant(quadruple: Quadruple) -> None:
    # Get variable virtual memory address
    raw_constant = quadruple.get_q2()
    variable_virtual_memory_address = int(quadruple.get_q4())

    # Resolve virtual memory address
    resolved_variable = resolve_virtual_memory_address(variable_virtual_memory_address)

    # Cast constant
    casted_constant = cast_constant(raw_constant, resolved_variable.type)

    if resolved_variable.scope == VariableScope.GLOBAL:
        global_memory.set_value(
            resolved_variable.type,
            resolved_variable.index,
            casted_constant
        )
    else:
        execution_stack.set_value_top_function_call(
            resolved_variable.scope,
            resolved_variable.type,
            resolved_variable.index,
            casted_constant
        )


def dispatch_goto(quadruple: Quadruple) -> int:
    jumped_to_program_counter = int(quadruple.get_q4())
    return jumped_to_program_counter


def dispatch_param(quadruple: Quadruple) -> None:
    input_variable_virtual_address = int(quadruple.get_q2())
    parameter_number = int(quadruple.get_q4())

    input_resolved_variable = resolve_virtual_memory_address(input_variable_virtual_address)
    value = get_variable_value(input_resolved_variable)

    global function
    parameter_virtual_memory_address = function.get_parameter_virtual_memory_address(
            parameter_number
    )

    resolved_parameter_variable = resolve_virtual_memory_address(
        parameter_virtual_memory_address
    )

    global function_call
    function_call.set_value(
        resolved_parameter_variable.scope,
        resolved_parameter_variable.type,
        resolved_parameter_variable.index,
        value
    )


def dispatch_return_value(quadruple: Quadruple) -> None:
    returned_variable_virtual_memory_address = int(quadruple.get_q2())
    global_function_virtual_memory_address = int(quadruple.get_q4())

    resolved_returned_variable = resolve_virtual_memory_address(returned_variable_virtual_memory_address)
    resolved_global_function_variable = resolve_virtual_memory_address(global_function_virtual_memory_address)

    value = get_variable_value(resolved_returned_variable)
    set_variable_value(resolved_global_function_variable, value)


def get_variable_value(
        resolved_variable: ResolvedVariable,
    ) -> Union[int, float, bool, str]:
    if resolved_variable.scope == VariableScope.GLOBAL:
        value = global_memory.get_value(
            resolved_variable.type,
            resolved_variable.index
        )
    else:
        value = execution_stack.get_value_top_function_call(
            resolved_variable.scope,
            resolved_variable.type,
            resolved_variable.index
        )

    return value


def set_variable_value(
        resolved_variable: ResolvedVariable,
        value: Union[int, float, bool, str],
    ) -> None:
    if resolved_variable.scope == VariableScope.GLOBAL:
        global_memory.set_value(
            resolved_variable.type,
            resolved_variable.index,
            value
        )
    else:
        execution_stack.set_value_top_function_call(
            resolved_variable.scope,
            resolved_variable.type,
            resolved_variable.index,
            value
        )


def cast_constant(value: str, type: type) -> Union[int, float, bool, str]:
    match type:
        case Type.INT:
            return int(value)
        case Type.REAL:
            return float(value)
        case Type.BOOL:
            return bool(value)
        case Type.CHAR:
            return str(value)
        case Type.STRING:
            return str(value)
        case Type.POINTER:
            return int(value)
        case _:
            return str(value)


FILE_EXTENSION = '.obj'

OPERATION_CODE = 0
FIRST_OPERAND = 1
SECOND_OPERAND = 2
THIRD_OPERAND = 3

file_reader = IntermediateCodeFileReader()

execution_stack = ExecutionStack()
program_counter_stack = ProgramCounterStack()
function_parameter_stack = FunctionParameterStack()

arg_parser = argparse.ArgumentParser(description='Esperanto executer')
arg_parser.add_argument('infile', type=str, help='Object file name')

args = arg_parser.parse_args()
fname = args.infile

fpath = file_reader.generate_file_path(fname)
fsuffix = file_reader.get_file_suffix(fpath)

if fsuffix != FILE_EXTENSION:
    raise InvalidFileExtensionError()

data = file_reader.read_file(fpath)

global_scope = GlobalScope(data['global_scope'])
function_directory = FunctionDirectory(data['function_directory'])
quadruple_list = QuadrupleList(data['quadruple_list'])

global_memory = GlobalMemory(global_scope)

main_function = function_directory.get_function('main')
main_function_call = FunctionCall(main_function)
execution_stack.push_function_call(main_function_call)

function_call = None
function_start_quadruple_number = None

quadruple = quadruple_list.get_quadruple(0)
operator = quadruple.get_operator()

while operator != Operator.END:
    match operator:
        case Operator.ASGMT:
            dispatch_assignment(quadruple)
            program_counter += 1
        case Operator.PLUS:
            dispatch_addition(quadruple)
            program_counter += 1
        case Operator.MINUS:
            dispatch_subtraction(quadruple)
            program_counter += 1
        case Operator.TIMES:
            dispatch_multiplication(quadruple)
            program_counter += 1
        case Operator.DIVIDE:
            dispatch_division(quadruple)
            program_counter += 1
        case Operator.MODULO:
            dispatch_modulo(quadruple)
            program_counter += 1
        case Operator.UNARY_PLUS:
            
            program_counter += 1
        case Operator.UNARY_MINUS:
            
            program_counter += 1
        case Operator.EQUAL:
            
            program_counter += 1
        case Operator.NEQUAL:
            
            program_counter += 1
        case Operator.LTHAN_EQUAL:
            
            program_counter += 1
        case Operator.GTHAN_EQUAL:
            
            program_counter += 1
        case Operator.LTHAN:
            
            program_counter += 1
        case Operator.GTHAN:
            
            program_counter += 1
        case Operator.AND:
            
            program_counter += 1
        case Operator.OR:
            
            program_counter += 1
        case Operator.NOT:
            
            program_counter += 1
        case Operator.READ:
            dispatch_read(quadruple)
            program_counter += 1
        case Operator.PRINT:
            dispatch_print(quadruple)
            program_counter += 1
        case Operator.STORE_CONSTANT:
            dispatch_store_constant(quadruple)
            program_counter += 1
        case Operator.GOTO:
            program_counter = dispatch_goto(quadruple)
        case Operator.GOTOF:
            program_counter += 1
        case Operator.ERA:
            function_id = quadruple.get_q4()
            function = function_directory.get_function(function_id)
            function_start_quadruple_number = function.get_start_quadruple_number()
            function_call = FunctionCall(function)
            program_counter += 1
        case Operator.GOSUB:
            execution_stack.push_function_call(function_call)

            program_counter_stack.push_counter(program_counter)
            program_counter = function_start_quadruple_number
        case Operator.PARAM:
            dispatch_param(quadruple)
            program_counter += 1
        case Operator.RETURN_VALUE:
            dispatch_return_value(quadruple)
            program_counter += 1
        case Operator.RETURN_VOID:
            
            program_counter += 1
        case Operator.ENDFUNC:
            execution_stack.pop_function_call()

            program_counter = program_counter_stack.pop_counter()
            program_counter += 1

    quadruple = quadruple_list.get_quadruple(program_counter)
    operator = quadruple.get_operator()
