from compiler.quadruples import ActivationRecordExpansionQuadruple
from compiler.quadruples import ArithmeticQuadruple
from compiler.quadruples import AssignmentQuadruple
from compiler.quadruples import ConstantStorageQuadruple
from compiler.quadruples import ConditionalControlTransferQuadruple
from compiler.quadruples import EndFunctionQuadruple
from compiler.quadruples import EndProgramQuadruple
from compiler.quadruples import PrintQuadruple
from compiler.quadruples import ReadQuadruple
from compiler.quadruples import RelationalQuadruple
from compiler.quadruples import Quadruple
from compiler.quadruples import QuadrupleList
from compiler.quadruples import UnaryArithmeticQuadruple
from compiler.quadruples import UnconditionalControlTransferQuadruple
from compiler.files import IntermediateCodeFileReader

OPERATION_CODE = 0
FIRST_OPERAND = 1
SECOND_OPERAND = 2
THIRD_OPERAND = 3

def main():
    file_reader = IntermediateCodeFileReader()
    pass