from abc import ABC
from abc import abstractmethod
from collections import deque
from dataclasses import dataclass

from .variables import Variable
from .variables import Operator

UNUSED_STATEMENT = -1

class Quadruple(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

@dataclass
class ArithmeticQuadruple(Quadruple):
    operator: Operator
    left_operand: Variable
    right_operand: Variable
    temporal_storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.left_operand} {self.right_operand} {self.temporal_storage_variable}'


@dataclass
class UnaryArithmeticQuadruple(Quadruple):
    operator: Operator
    value_variable: Variable
    temporal_storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.value_variable} {self.temporal_storage_variable}'


@dataclass
class RelationalQuadruple(Quadruple):
    operator: Operator
    left_operand: Variable
    right_operand: Variable
    temporal_storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.left_operand} {self.right_operand} {self.temporal_storage_variable}'


@dataclass
class AssignmentQuadruple(Quadruple):
    operator: Operator
    value_variable: Variable
    storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.value_variable} {self.storage_variable}'


@dataclass
class ControlTransferQuadruple(Quadruple):
    operator: Operator
    boolean_variable: Variable
    program_count: int

    def __str__(self) -> str:
        return f'{self.operator.name} {self.boolean_variable} {self.program_count}'


@dataclass
class ConstantStorageQuadruple(Quadruple):
    operator: Operator
    constant_value: str
    storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.constant_value} {self.storage_variable}'


@dataclass
class ReadQuadruple(Quadruple):
    operator: Operator
    storage_variable: Variable


    def __str__(self) -> str:
        return f'{self.operator.name} {self.storage_variable}'


@dataclass
class PrintQuadruple(Quadruple):
    operator: Operator
    printed_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.printed_variable}'


@dataclass
class EndFunctionQuadruple(Quadruple):
    operator: Operator = Operator.ENDFUNC

    def __str__(self) -> str:
        return f'{self.operator.name}'


@dataclass
class EndProgramQuadruple(Quadruple):
    operator: Operator

    def __str__(self) -> str:
        return f'{self.operator.name}'


class QuadrupleList():
    def __init__(self) -> None:
        self._list = deque()


    def insert_quadruple(self, quadruple: Quadruple) -> None:
        self._list.append(quadruple)

    
    def fill_control_transfer_quadruple(self, quadruple_number: int, program_count: int) -> None:
        self._list[quadruple_number].program_count = program_count

    
    def __str__(self) -> str:
        s = 'QuadrupleList(\n'

        for count, item in enumerate(self._list):
            s += f'\t{count}: {item.__str__()}\n'
        
        s += ')'

        return s
