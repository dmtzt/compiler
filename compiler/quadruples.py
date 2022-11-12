from collections import deque

from .variables import Variable
from .variables import Operator

UNUSED_STATEMENT = -1

class ArithmeticQuadruple():
    def __init__(
        self,
        operator: Operator,
        left_operand: Variable,
        right_operand: Variable,
        temporal_storage_variable: Variable
    ) -> None:
        self._operator = operator
        self._left_operand = left_operand
        self._right_operand = right_operand
        self._temporal_storage_variable = temporal_storage_variable

    
    def get_intermediate_code_representation(self) -> str:
        return f'{self._operator.value}, {self._left_operand.get_virtual_memory_address()}, {self._right_operand.get_virtual_memory_address()}, {self._temporal_storage_variable.get_virtual_memory_address()}'

    
    def __str__(self) -> str:
        return f'ArithmeticQuadruple(op={self._operator} left={self._left_operand.__str__()} right={self._right_operand.__str__()} temp_var={self._temporal_storage_variable.__str__()})'


class RelationalQuadruple():
    def __init__(
        self,
        operator: Operator,
        left_operand: Variable,
        right_operand: Variable,
        temporal_storage_variable: Variable
    ) -> None:
        self._operator = operator
        self._left_operand = left_operand
        self._right_operand = right_operand
        self._temporal_storage_variable = temporal_storage_variable

    
    def get_intermediate_code_representation(self) -> str:
        return f'{self._operator.value}, {self._left_operand.get_virtual_memory_address()}, {self._right_operand.get_virtual_memory_address()}, {self._temporal_storage_variable.get_virtual_memory_address()}'


    def __str__(self) -> str:
        return f'RelationalQuadruple(op={self._operator} left_o={self._left_operand.__str__()} right={self._right_operand.__str__()} temp_var={self._temporal_storage_variable.__str__()})'


class AssignmentQuadruple():
    def __init__(
        self,
        operator: Operator,
        value_variable: Variable,
        storage_variable: Variable
    ) -> None:
        self._operator = operator
        self._value_variable = value_variable
        self._storage_variable = storage_variable
    

    def get_intermediate_code_representation(self) -> str:
        return f'{self._operator.value}, {self._value_variable.get_virtual_memory_address()}, {UNUSED_STATEMENT}, {self._storage_variable.get_virtual_memory_address()}'


    def __str__(self) -> str:
        return f'AssignmentQuadruple(op={self._operator} value_var={self._value_variable.__str__()} storage_var={self._storage_variable.__str__()})'


class ControlTransferQuadruple():
    def __init__(
        self,
        operator: Operator,
        boolean_variable: Variable,
        program_count: int
    ) -> None:
        self._operator = operator
        self._boolean_variable = boolean_variable
        self._program_count = program_count

    
    def set_program_count(self, program_count):
        self._program_count = program_count

    
    def get_intermediate_code_representation(self) -> str:
        return f'{self._operator.value}, {self._boolean_variable.get_virtual_memory_address()}, {UNUSED_STATEMENT}, {self._program_count}'

    
    def __str__(self) -> str:
        return f'ControlTransferQuadruple(op={self._operator} boolean_var={self._boolean_variable.__str__()} program_count={self._program_count})'


class ConstantStorageQuadruple():
    def __init__(
        self,
        constant_value: str,
        storage_variable: Variable,
    ) -> None:
        self._operator = Operator.STORE_CONSTANT
        self._constant_value = constant_value
        self._storage_variable = storage_variable

    
    def __str__(self) -> str:
        return f'ConstantStorageQuadruple(op={self._operator} value={self._constant_value} storage_var={self._storage_variable})'


class ReadQuadruple():
    def __init__(self, temporal_storage_variable: Variable) -> None:
        self._operator = Operator.READ
        self._temporal_storage_variable = temporal_storage_variable


    def __str__(self) -> str:
        return f'ReadQuadruple(op={self._operator} temp_var={self._temporal_storage_variable.__str__()})'


class PrintQuadruple():
    def __init__(self, printed_variable: Variable) -> None:
        self._operator = Operator.PRINT
        self._printed_variable = printed_variable

    
    def __str__(self) -> str:
        return f'PrintQuadruple(op={self._operator} temp_var={self._printed_variable.__str__()})'


class QuadrupleList():
    def __init__(self) -> None:
        self._list = deque()

    
    def insert_arithmetic_quadruple(self, quadruple: ArithmeticQuadruple) -> None:
        self._list.append(quadruple)

    
    def insert_relational_quadruple(self, quadruple: RelationalQuadruple) -> None:
        self._list.append(quadruple)

    
    def insert_assignment_quadruple(self, quadruple: AssignmentQuadruple) -> None:
        self._list.append(quadruple)

    
    def insert_control_transfer_quadruple(self, quadruple: ControlTransferQuadruple) -> None:
        self._list.append(quadruple)

    
    def insert_constant_storage_quadruple(self, quadruple: ConstantStorageQuadruple) -> None:
        self._list.append(quadruple)

    
    def insert_read_quadruple(self, quadruple: ReadQuadruple) -> None:
        self._list.append(quadruple)

    
    def insert_print_quadruple(self, quadruple: PrintQuadruple) -> None:
        self._list.append(quadruple)

    
    def fill_control_transfer_quadruple(self, quadruple_number: int, program_count: int) -> None:
        self._list[quadruple_number].set_program_count(program_count)

    
    def __str__(self) -> str:
        s = 'QuadrupleList(\n'

        for count, item in enumerate(self._list):
            s += f'\t{count}: {item.__str__()}\n'
        
        s += ')'

        return s
