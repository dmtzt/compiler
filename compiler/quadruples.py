from abc import ABC
from abc import abstractmethod
from collections import deque
from dataclasses import dataclass

from .variables import Variable
from .variables import Operator

class Quadruple(ABC):
    UNUSED_STATEMENT = '-'

    @abstractmethod
    def get_named_representation(self) -> str:
        pass

    
    @abstractmethod
    def get_intermediate_code_representation(self) -> str:
        pass

    
    def _generate_intermediate_code_representation(self, q1: str, q2: str, q3: str, q4: str) -> str:
        return f'{q1}{" "}{q2}{" "}{q3}{" "}{q4}'


class ControlTransferQuadruple(Quadruple):
    @abstractmethod
    def fill_program_count(self, program_count: int) -> None:
        pass


@dataclass
class ArithmeticQuadruple(Quadruple):
    operator: Operator
    left_operand: Variable
    right_operand: Variable
    temporal_storage_variable: Variable
    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16} {self.left_operand.get_id() : <10} {self.right_operand.get_id() : <10} {self.temporal_storage_variable.get_id()}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.left_operand.get_virtual_memory_address())
        q3 = str(self.right_operand.get_virtual_memory_address())
        q4 = str(self.temporal_storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class UnaryArithmeticQuadruple(Quadruple):
    operator: Operator
    value_variable: Variable
    temporal_storage_variable: Variable
    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16} {self.value_variable.get_id() : <10} {" " : <10} {self.temporal_storage_variable.get_id()}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.value_variable.get_virtual_memory_address())
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.temporal_storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class RelationalQuadruple(Quadruple):
    operator: Operator
    left_operand: Variable
    right_operand: Variable
    temporal_storage_variable: Variable
    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16} {self.left_operand.get_id() : <10} {self.right_operand.get_id() : <10} {self.temporal_storage_variable.get_id()}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.left_operand.get_virtual_memory_address())
        q3 = str(self.right_operand.get_virtual_memory_address())
        q4 = str(self.temporal_storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class AssignmentQuadruple(Quadruple):
    operator: Operator
    value_variable: Variable
    storage_variable: Variable
    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16} {self.value_variable.get_id() : <10} {" " : <10} {self.storage_variable.get_id()}'

    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.value_variable.get_virtual_memory_address())
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ConditionalControlTransferQuadruple(ControlTransferQuadruple):
    operator: Operator
    boolean_variable: Variable
    program_count: int
    
    def fill_program_count(self, program_count: int) -> None:
        self.program_count = program_count

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.boolean_variable.get_id() : <10}{" " : <10}{self.program_count}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.boolean_variable.get_virtual_memory_address())
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.program_count)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class UnconditionalControlTransferQuadruple(ControlTransferQuadruple):
    operator: Operator
    program_count: int
    
    def fill_program_count(self, program_count: int) -> None:
        self.program_count = program_count

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.program_count}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.program_count)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ConstantStorageQuadruple(Quadruple):
    operator: Operator
    constant_value: str
    storage_variable: Variable
    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.constant_value : <10}{" " : <10}{self.storage_variable.get_id()}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.constant_value)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ReadQuadruple(Quadruple):
    operator: Operator
    storage_variable: Variable
    
    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.storage_variable.get_id()}'


    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class PrintQuadruple(Quadruple):
    operator: Operator
    printed_variable: Variable

    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.printed_variable.get_id()}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.printed_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ActivationRecordExpansionQuadruple(Quadruple):
    function_id: str
    operator: Operator = Operator.ERA

    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.function_id}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.function_id)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ParameterPassingQuadruple(Quadruple):
    variable : Variable
    parameter_number : int
    operator : Operator = Operator.PARAM

    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{self.variable.get_id() : <10}{" " : <10}{self.parameter_number}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.variable.get_virtual_memory_address())
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.parameter_number)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ReturnValueQuadruple(Quadruple):
    return_variable : Variable
    operator : Operator = Operator.RETURN

    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.return_variable.get_id()}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.return_variable.get_id())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ReturnVoidQuadruple(Quadruple):
    operator : Operator = Operator.RETURN

    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.UNUSED_STATEMENT)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class StartSubroutineQuadruple(Quadruple):
    function_id : str
    operator : Operator = Operator.GOSUB

    def get_named_representation(self) -> str:
        return f'{self.operator.name : <16}{" " : <10}{" " : <10}{self.function_id}'

    
    def get_intermediate_code_representation(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.function_id)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class EndFunctionQuadruple(Quadruple):
    operator: Operator = Operator.ENDFUNC

    def __str__(self) -> str:
        return f'{self.operator.name}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name}'

    
    def get_intermediate_code_representation(self) -> str:
        return f'{self.operator.value : <3}{self.UNUSED_STATEMENT : <6}{self.UNUSED_STATEMENT : <6}{self.UNUSED_STATEMENT}'



@dataclass
class EndProgramQuadruple(Quadruple):
    operator: Operator

    def __str__(self) -> str:
        return f'{self.operator.name}'

    
    def get_named_representation(self) -> str:
        return f'{self.operator.name}'

    
    def get_intermediate_code_representation(self) -> str:
        return f'{self.operator.value : <3}{self.UNUSED_STATEMENT : <6}{self.UNUSED_STATEMENT : <6}{self.UNUSED_STATEMENT}'


class QuadrupleList():
    def __init__(self) -> None:
        self._list: deque[Quadruple] = deque()


    def insert_quadruple(self, quadruple: Quadruple) -> None:
        self._list.append(quadruple)

    
    def fill_control_transfer_quadruple(self, quadruple_number: int, program_count: int) -> None:
        if not isinstance(self._list[quadruple_number], ControlTransferQuadruple):
            raise InvalidQuadrupleOperationError()

        self._list[quadruple_number].fill_program_count(program_count)

    
    def get_quadruples(self) -> deque[Quadruple]:
        return self._list

    
    def __str__(self) -> str:
        s = 'QuadrupleList(\n'

        for count, item in enumerate(self._list):
            s += f'\t{count : <4} {item.get_intermediate_code_representation()}\n'
        
        s += ')'

        return s


class InvalidQuadrupleOperationError(RuntimeError):
    pass