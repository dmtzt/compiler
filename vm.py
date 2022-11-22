import argparse
from pathlib import Path

from compiler.execution import ExecutionStack
from compiler.execution import FunctionCall
from compiler.execution import FunctionDirectory
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
operator = 1
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

print(function_directory.__str__())
print(quadruple_list.__str__())

# for quadruple in quadruple_list:
#     match operator:
#         case Operator.PLUS:
#             pass
#         case Operator.MINUS:
#             pass
#         case Operator.TIMES:
#             pass
#         case Operator.DIVIDE:
#             pass
#         case Operator.MODULO:
#             pass
#         case Operator.UNARY_PLUS:
#             pass
#         case Operator.UNARY_MINUS:
#             pass
#         case Operator.EQUAL:
#             pass
#         case Operator.NEQUAL:
#             pass
#         case Operator.LTHAN_EQUAL:
#             pass
#         case Operator.GTHAN_EQUAL:
#             pass
#         case Operator.LTHAN:
#             pass
#         case Operator.GTHAN:
#             pass
#         case Operator.AND:
#             pass
#         case Operator.OR:
#             pass
#         case Operator.NOT:
#             pass
#         case Operator.READ:
#             pass
#         case Operator.PRINT:
#             pass
#         case Operator.STORE_CONSTANT:
#             pass
#         case Operator.GOTO:
#             pass
#         case Operator.GOTOF:
#             pass
#         case Operator.GOSUB:
#             pass
#         case Operator.ERA:
#             pass
#         case Operator.PARAM:
#             pass
#         case Operator.RETURN_VALUE:
#             pass
#         case Operator.RETURN_VOID:
#             pass
#         case Operator.ENDFUNC:
#             pass
#         case Operator.END:
#             pass