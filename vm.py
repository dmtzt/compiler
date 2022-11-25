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
from compiler.execution import QuadrupleList
from compiler.execution import VirtualMemoryAddressResolver
from compiler.files import IntermediateCodeFileReader
from compiler.operators import Operator
from compiler.variables import Type

class InvalidFileExtensionError(RuntimeError):
    pass


def get_base_virtual_memory_address(virtual_memory_address: int) -> int:
    return VirtualMemoryAddressResolver.get_base_virtual_memory_address(virtual_memory_address)


def resolve_base_virtual_memory_address(base_virtual_memory_address: int) -> tuple[str, Type]:
    return VirtualMemoryAddressResolver.resolve_base_virtual_memory_address(base_virtual_memory_address)


def get_variable_index(virtual_memory_address: int) -> int:
    return VirtualMemoryAddressResolver.get_index(virtual_memory_address)


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

program_counter = 0

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
            
            result_address = int(quadruple.get_q2())
            result_base_address = get_base_virtual_memory_address(result_address)
            result_index = get_variable_index(result_address)
            result_memory, result_type = resolve_base_virtual_memory_address(result_base_address)
            result_value = execution_stack.get_value_top_function_call(result_memory, result_type, result_index)

            storage_address = int(quadruple.get_q4())
            storage_base_address = get_base_virtual_memory_address(storage_address)
            storage_index = get_variable_index(storage_address)
            storage_memory, storage_type = resolve_base_virtual_memory_address(storage_base_address)

            execution_stack.set_value_top_function_call(storage_memory, storage_type, storage_index, result_value)

            program_counter += 1
        case Operator.PLUS:
            
            left_address = int(quadruple.get_q2())
            left_base_address = get_base_virtual_memory_address(left_address)
            left_index = get_variable_index(left_address)
            left_memory, left_type = resolve_base_virtual_memory_address(left_base_address)
            left_value = execution_stack.get_value_top_function_call(left_memory, left_type, left_index)

            right_address = int(quadruple.get_q3())
            right_base_address = get_base_virtual_memory_address(right_address)
            right_index = get_variable_index(right_address)
            right_memory, right_type = resolve_base_virtual_memory_address(right_base_address)
            right_value = execution_stack.get_value_top_function_call(right_memory, right_type, right_index)

            result_address = int(quadruple.get_q4())
            result_base_address = get_base_virtual_memory_address(result_address)
            result_index = get_variable_index(result_address)
            result_memory, result_type = resolve_base_virtual_memory_address(result_base_address)
            
            result_value = left_value + right_value
            execution_stack.set_value_top_function_call(result_memory, result_type, result_index, result_value)
            
            program_counter += 1
        case Operator.MINUS:
            
            left_address = int(quadruple.get_q2())
            left_base_address = get_base_virtual_memory_address(left_address)
            left_index = get_variable_index(left_address)
            left_memory, left_type = resolve_base_virtual_memory_address(left_base_address)
            left_value = execution_stack.get_value_top_function_call(left_memory, left_type, left_index)

            right_address = int(quadruple.get_q3())
            right_base_address = get_base_virtual_memory_address(right_address)
            right_index = get_variable_index(right_address)
            right_memory, right_type = resolve_base_virtual_memory_address(right_base_address)
            right_value = execution_stack.get_value_top_function_call(right_memory, right_type, right_index)

            result_address = int(quadruple.get_q4())
            result_base_address = get_base_virtual_memory_address(result_address)
            result_index = get_variable_index(result_address)
            result_memory, result_type = resolve_base_virtual_memory_address(result_base_address)
            
            result_value = left_value - right_value
            execution_stack.set_value_top_function_call(result_memory, result_type, result_index, result_value)
            program_counter += 1
        case Operator.TIMES:
            

            left_address = int(quadruple.get_q2())
            left_base_address = get_base_virtual_memory_address(left_address)
            left_index = get_variable_index(left_address)
            left_memory, left_type = resolve_base_virtual_memory_address(left_base_address)
            left_value = execution_stack.get_value_top_function_call(left_memory, left_type, left_index)

            right_address = int(quadruple.get_q3())
            right_base_address = get_base_virtual_memory_address(right_address)
            right_index = get_variable_index(right_address)
            right_memory, right_type = resolve_base_virtual_memory_address(right_base_address)
            right_value = execution_stack.get_value_top_function_call(right_memory, right_type, right_index)

            result_address = int(quadruple.get_q4())
            result_base_address = get_base_virtual_memory_address(result_address)
            result_index = get_variable_index(result_address)
            result_memory, result_type = resolve_base_virtual_memory_address(result_base_address)
            
            result_value = left_value * right_value
            execution_stack.set_value_top_function_call(result_memory, result_type, result_index, result_value)

            program_counter += 1
        case Operator.DIVIDE:
            
            left_address = int(quadruple.get_q2())
            left_base_address = get_base_virtual_memory_address(left_address)
            left_index = get_variable_index(left_address)
            left_memory, left_type = resolve_base_virtual_memory_address(left_base_address)
            left_value = execution_stack.get_value_top_function_call(left_memory, left_type, left_index)

            right_address = int(quadruple.get_q3())
            right_base_address = get_base_virtual_memory_address(right_address)
            right_index = get_variable_index(right_address)
            right_memory, right_type = resolve_base_virtual_memory_address(right_base_address)
            right_value = execution_stack.get_value_top_function_call(right_memory, right_type, right_index)

            result_address = int(quadruple.get_q4())
            result_base_address = get_base_virtual_memory_address(result_address)
            result_index = get_variable_index(result_address)
            result_memory, result_type = resolve_base_virtual_memory_address(result_base_address)
            
            result_value = left_value // right_value
            execution_stack.set_value_top_function_call(result_memory, result_type, result_index, result_value)
            
            program_counter += 1
        case Operator.MODULO:
            
            left_address = int(quadruple.get_q2())
            left_base_address = get_base_virtual_memory_address(left_address)
            left_index = get_variable_index(left_address)
            left_memory, left_type = resolve_base_virtual_memory_address(left_base_address)
            left_value = execution_stack.get_value_top_function_call(left_memory, left_type, left_index)

            right_address = int(quadruple.get_q3())
            right_base_address = get_base_virtual_memory_address(right_address)
            right_index = get_variable_index(right_address)
            right_memory, right_type = resolve_base_virtual_memory_address(right_base_address)
            right_value = execution_stack.get_value_top_function_call(right_memory, right_type, right_index)

            result_address = int(quadruple.get_q4())
            result_base_address = get_base_virtual_memory_address(result_address)
            result_index = get_variable_index(result_address)
            result_memory, result_type = resolve_base_virtual_memory_address(result_base_address)
            
            result_value = left_value % right_value
            execution_stack.set_value_top_function_call(result_memory, result_type, result_index, result_value)
            
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
            
            storage_address = int(quadruple.get_q4())
            storage_base_address = get_base_virtual_memory_address(storage_address)
            storage_index = get_variable_index(storage_address)
            storage_memory, storage_type = resolve_base_virtual_memory_address(storage_base_address)

            reading_value = input()
            storage_value = cast_constant(reading_value, storage_type)

            execution_stack.set_value_top_function_call(storage_memory, storage_type, storage_index, storage_value)
            program_counter += 1
        case Operator.PRINT:
            # 
            address = int(quadruple.get_q4())
            base_address = get_base_virtual_memory_address(address)
            index = get_variable_index(address)

            memory, type = resolve_base_virtual_memory_address(base_address)
            value = execution_stack.get_value_top_function_call(memory, type, index)
            
            print(value)

            program_counter += 1
        case Operator.STORE_CONSTANT:
            # 
            address = int(quadruple.get_q4())
            base_address = get_base_virtual_memory_address(address)
            index = get_variable_index(address)

            memory, type = resolve_base_virtual_memory_address(base_address)
            constant = cast_constant(quadruple.get_q2(), type)
            execution_stack.set_value_top_function_call(memory, type, index, constant)
            
            program_counter += 1
        case Operator.GOTO:
            jumped_to_program_counter = int(quadruple.get_q4())
            program_counter = jumped_to_program_counter
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
            program_counter += 1
        case Operator.RETURN_VALUE:
            
            program_counter += 1
        case Operator.RETURN_VOID:
            
            program_counter += 1
        case Operator.ENDFUNC:
            execution_stack.pop_function_call()

            program_counter = program_counter_stack.pop_counter()
            program_counter += 1

    quadruple = quadruple_list.get_quadruple(program_counter)
    operator = quadruple.get_operator()