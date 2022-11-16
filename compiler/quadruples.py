from abc import ABC
from abc import abstractmethod
from collections import deque
from dataclasses import dataclass

from .variables import Variable
from .variables import Operator

class Quadruple(ABC):
    UNUSED_STATEMENT = -1

    @abstractmethod
    def __str__(self) -> str:
        pass


    @abstractmethod
    def get_named_representation(self) -> str:
        pass

    
    # @abstractmethod
    # def get_intermediate_code_representation(self) -> str:
    #     pass

@dataclass
class ArithmeticQuadruple(Quadruple):
    operator: Operator
    left_operand: Variable
    right_operand: Variable
    temporal_storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.left_operand} {self.right_operand} {self.temporal_storage_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.left_operand.get_id() : <10}{self.right_operand.get_id() : <10}{self.temporal_storage_variable.get_id()}'


@dataclass
class UnaryArithmeticQuadruple(Quadruple):
    operator: Operator
    value_variable: Variable
    temporal_storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.value_variable} {self.temporal_storage_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.value_variable.get_id() : <10}{" " : <10}{self.temporal_storage_variable.get_id()}'


@dataclass
class RelationalQuadruple(Quadruple):
    operator: Operator
    left_operand: Variable
    right_operand: Variable
    temporal_storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.left_operand} {self.right_operand} {self.temporal_storage_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.left_operand.get_id() : <10}{self.right_operand.get_id() : <10}{self.temporal_storage_variable.get_id()}'


@dataclass
class AssignmentQuadruple(Quadruple):
    operator: Operator
    value_variable: Variable
    storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.value_variable} {self.storage_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.value_variable.get_id() : <10}{" " : <10}{self.storage_variable.get_id()}'


@dataclass
class ConditionalControlTransferQuadruple(Quadruple):
    operator: Operator
    boolean_variable: Variable
    program_count: int

    def __str__(self) -> str:
        return f'{self.operator.name} {self.boolean_variable} {self.program_count}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.boolean_variable.get_id() : <10}{" " : <10}{self.program_count}'


@dataclass
class UnconditionalControlTransferQuadruple(Quadruple):
    operator: Operator
    program_count: int

    def __str__(self) -> str:
        return f'{self.operator.name} {self.program_count}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.program_count}'


@dataclass
class ConstantStorageQuadruple(Quadruple):
    operator: Operator
    constant_value: str
    storage_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.constant_value} {self.storage_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.constant_value : <10}{" " : <10}{self.storage_variable.get_id()}'


@dataclass
class ReadQuadruple(Quadruple):
    operator: Operator
    storage_variable: Variable


    def __str__(self) -> str:
        return f'{self.operator.name} {self.storage_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.storage_variable.get_id()}'


@dataclass
class PrintQuadruple(Quadruple):
    operator: Operator
    printed_variable: Variable

    def __str__(self) -> str:
        return f'{self.operator.name} {self.printed_variable}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.printed_variable.get_id()}'


@dataclass
class EndFunctionQuadruple(Quadruple):
    operator: Operator = Operator.ENDFUNC

    def __str__(self) -> str:
        return f'{self.operator.name}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name}'



@dataclass
class EndProgramQuadruple(Quadruple):
    operator: Operator

    def __str__(self) -> str:
        return f'{self.operator.name}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name}'


class QuadrupleList():
    def __init__(self) -> None:
        self._list: deque[Quadruple] = deque()


    def insert_quadruple(self, quadruple: Quadruple) -> None:
        self._list.append(quadruple)

    
    def fill_control_transfer_quadruple(self, quadruple_number: int, program_count: int) -> None:
        self._list[quadruple_number].program_count = program_count

    
    def __str__(self) -> str:
        s = 'QuadrupleList(\n'

        for count, item in enumerate(self._list):
            s += f'\t{count : <4} {item.get_named_representation()}\n'
        
        s += ')'

        return s
