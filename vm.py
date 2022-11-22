import argparse
from pathlib import Path

from compiler.execution import ExecutionStack
from compiler.execution import FunctionCall
from compiler.execution import FunctionDirectory
from compiler.execution import FunctionParameterStack
from compiler.execution import InstructionPointerStack
from compiler.execution import QuadrupleList
from compiler.files import IntermediateCodeFileReader
from compiler.operators import Operator

class InvalidFileExtensionError(RuntimeError):
    pass


FILE_EXTENSION = '.obj'

OPERATION_CODE = 0
FIRST_OPERAND = 1
SECOND_OPERAND = 2
THIRD_OPERAND = 3

file_reader = IntermediateCodeFileReader()

execution_stack = ExecutionStack()
instruction_pointer_stack = InstructionPointerStack()
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
function_directory = FunctionDirectory(data['function_directory'])
quadruple_list = QuadrupleList(data['quadruple_list'])

main_function = function_directory.get_function('main')
main_function_call = FunctionCall(main_function)
execution_stack.push_function_call(main_function_call)

print(function_directory.__str__())
print(quadruple_list.__str__())
print(execution_stack.__str__())

quadruple = quadruple_list.get_quadruple(0)
operator = quadruple.get_operator()

while operator != Operator.END:
    match operator:
        case Operator.ASGMT:
            print('ASGMT')
            program_counter += 1
        case Operator.PLUS:
            print('PLUS')
            program_counter += 1
        case Operator.MINUS:
            print('MINUS')
            program_counter += 1
        case Operator.TIMES:
            print('TIMES')
            program_counter += 1
        case Operator.DIVIDE:
            print('DIVIDE')
            program_counter += 1
        case Operator.MODULO:
            print('MODULE')
            program_counter += 1
        case Operator.UNARY_PLUS:
            print('UNARY PLUS')
            program_counter += 1
        case Operator.UNARY_MINUS:
            print('UNARY MINUS')
            program_counter += 1
        case Operator.EQUAL:
            print('EQUAL')
            program_counter += 1
        case Operator.NEQUAL:
            print('NEQUAL')
            program_counter += 1
        case Operator.LTHAN_EQUAL:
            print('LTHAN EQUAL')
            program_counter += 1
        case Operator.GTHAN_EQUAL:
            print('GTHAN EQUAL')
            program_counter += 1
        case Operator.LTHAN:
            print('LTHAN')
            program_counter += 1
        case Operator.GTHAN:
            print('GTHAN')
            program_counter += 1
        case Operator.AND:
            print('AND')
            program_counter += 1
        case Operator.OR:
            print('OR')
            program_counter += 1
        case Operator.NOT:
            print('NOT')
            program_counter += 1
        case Operator.READ:
            print('READ')
            program_counter += 1
        case Operator.PRINT:
            print('PRINT')
            program_counter += 1
        case Operator.STORE_CONSTANT:
            print('STORE_CONSTANT')
            program_counter += 1
        case Operator.GOTO:
            print('GOTO')
            program_counter += 1
        case Operator.GOTOF:
            print('GOTOF')
            program_counter += 1
        case Operator.GOSUB:
            print('GOSUB')
            program_counter += 1
        case Operator.ERA:
            print('ERA')
            program_counter += 1
        case Operator.PARAM:
            print('PARAM')
            program_counter += 1
        case Operator.RETURN_VALUE:
            print('RETURN VALUE')
            program_counter += 1
        case Operator.RETURN_VOID:
            print('RETURN VOID')
            program_counter += 1
        case Operator.ENDFUNC:
            print('ENDFUNC')
            program_counter += 1

    quadruple = quadruple_list.get_quadruple(program_counter)
    operator = quadruple.get_operator()