from abc import ABC
from abc import abstractmethod
from collections import deque
from dataclasses import dataclass, field

from .variables import Variable
from .variables import Operator

class Quadruple(ABC):
    UNUSED_STATEMENT = '-'

    @abstractmethod
    def get_debug_repr(self) -> str:
        pass

    
    @abstractmethod
    def get_json_obj(self) -> str:
        pass


    def _generate_intermediate_code_representation(self, q1: str, q2: str, q3: str, q4: str) -> list:
        return [q1, q2, q3, q4]
    

    def _generate_debug_repr(self, q1: str, q2: str, q3: str, q4: str) -> str:
         return f"{q1 : <16} {q2 : <20} {q3 : <20} {q4}"


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
    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        left_id = self.left_operand.get_id()
        left_address = self.left_operand.get_virtual_memory_address()
        right_id = self.right_operand.get_id()
        right_address = self.right_operand.get_virtual_memory_address()
        temp_id = self.temporal_storage_variable.get_id()
        temp_address = self.temporal_storage_variable.get_virtual_memory_address()

        return self._generate_debug_repr(
                operator_name,
                f'{left_id}({left_address})',
                f'{right_id}({right_address})',
                f'{temp_id}({temp_address})',
        )

    
    def get_json_obj(self) -> str:
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
    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        value_id = self.value_variable.get_id()
        value_address = self.value_variable.get_virtual_memory_address()
        temp_id = self.temporal_storage_variable.get_id()
        temp_address = self.temporal_storage_variable.get_virtual_memory_address()
        
        return self._generate_debug_repr(
            operator_name,
            f'{value_id}({value_address})',
            '',
            f'{temp_id}({temp_address})'
        )


    def get_json_obj(self) -> str:
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
    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        left_id = self.left_operand.get_id()
        left_address = self.left_operand.get_virtual_memory_address()
        right_id = self.right_operand.get_id()
        right_address = self.right_operand.get_virtual_memory_address()
        temp_id = self.temporal_storage_variable.get_id()
        temp_address = self.temporal_storage_variable.get_virtual_memory_address()

        return self._generate_debug_repr(
            operator_name,
            f'{left_id}({left_address})',
            f'{right_id}({right_address})',
            f'{temp_id}({temp_address})',
        )


    def get_json_obj(self) -> str:
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
    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        value_id = self.value_variable.get_id()
        value_address = self.value_variable.get_virtual_memory_address()
        storage_id = self.storage_variable.get_id()
        storage_address = self.storage_variable.get_virtual_memory_address()
        
        return self._generate_debug_repr(
            operator_name,
            f'{value_id}({value_address})',
            '',
            f'{storage_id}({storage_address})'
        )


    def get_json_obj(self) -> str:
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

    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        boolean_id = self.boolean_variable.get_id()
        boolean_address = self.boolean_variable.get_virtual_memory_address()
        program_count = self.program_count
        
        return self._generate_debug_repr(
            operator_name,
            f'{boolean_id}({boolean_address})',
            '',
            program_count,
        )

    
    def get_json_obj(self) -> str:
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

    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        program_count = self.program_count
        
        return self._generate_debug_repr(
            operator_name,
            '',
            '',
            program_count,
        )

    
    def get_json_obj(self) -> str:
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
    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        constant_value = self.constant_value
        storage_id = self.storage_variable.get_id()
        storage_address = self.storage_variable.get_virtual_memory_address()
        
        return self._generate_debug_repr(
            operator_name,
            constant_value,
            '',
            f'{storage_id}({storage_address})',
        )

    
    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.constant_value)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ReadQuadruple(Quadruple):
    storage_variable: Variable
    operator: Operator = Operator.READ
    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        storage_id = self.storage_variable.get_id()
        storage_address = self.storage_variable.get_virtual_memory_address()
        
        return self._generate_debug_repr(
            operator_name,
            '',
            '',
            f'{storage_id}({storage_address})',
        )


    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.storage_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class PrintQuadruple(Quadruple):
    printed_variable: Variable
    operator: Operator = Operator.PRINT

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        printed_id = self.printed_variable.get_id()
        printed_address = self.printed_variable.get_virtual_memory_address()
        
        return self._generate_debug_repr(
            operator_name,
            '',
            '',
            f'{printed_id}({printed_address})',
        )


    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.printed_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)
    

@dataclass
class LimitsVerificationQuadruple(Quadruple):
    index_variable: Variable
    upper_bound: int
    lower_bound: int = field(init=False, default=0)
    operator: Operator = field(init=False, default=Operator.VER)

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        index_variable_id = self.index_variable.get_id()
        index_variable_address = self.index_variable.get_virtual_memory_address()
        lower_bound = self.lower_bound
        upper_bound = self.upper_bound

        return self._generate_debug_repr(
            operator_name,
            f'{index_variable_id}({index_variable_address})',
            lower_bound,
            upper_bound,
        )
    

    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.index_variable.get_virtual_memory_address())
        q3 = str(self.lower_bound)
        q4 = str(self.upper_bound)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ActivationRecordExpansionQuadruple(Quadruple):
    function_id: str
    operator: Operator = Operator.ERA

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        function_id = self.function_id
        
        return self._generate_debug_repr(
            operator_name,
            '',
            '',
            function_id,
        )


    def get_json_obj(self) -> str:
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

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        variable_id = self.variable.get_id()
        variable_address = self.variable.get_virtual_memory_address()
        parameter_number = self.parameter_number
        
        return self._generate_debug_repr(
            operator_name,
            f'{variable_id}({variable_address})',
            '',
            parameter_number,
        )


    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.variable.get_virtual_memory_address())
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.parameter_number)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ReturnValueQuadruple(Quadruple):
    return_variable : Variable
    function_global_variable : Variable
    operator : Operator = Operator.RETURN_VALUE

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        return_id = self.return_variable.get_id()
        return_address = self.return_variable.get_virtual_memory_address()
        function_id = self.function_global_variable.get_id()
        function_address = self.function_global_variable.get_virtual_memory_address()
        
        return self._generate_debug_repr(
            operator_name,
            f'{return_id}({return_address})',
            '',
            f'{function_id}({function_address})',
        )


    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.return_variable.get_virtual_memory_address())
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.function_global_variable.get_virtual_memory_address())
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class ReturnVoidQuadruple(Quadruple):
    operator : Operator = Operator.RETURN_VOID

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        
        return f'{operator_name}'

    
    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.UNUSED_STATEMENT)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class StartSubroutineQuadruple(Quadruple):
    function_id : str
    operator : Operator = Operator.GOSUB

    def get_debug_repr(self) -> str:
        operator_name = self.operator.name
        function_id = self.function_id

        return self._generate_debug_repr(
            operator_name,
            '',
            '',
            function_id,
        )

    
    def get_json_obj(self) -> str:
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

    
    def get_debug_repr(self) -> str:
        operator_name = self.operator.name

        return f'{operator_name}'


    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.UNUSED_STATEMENT)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


@dataclass
class EndProgramQuadruple(Quadruple):
    operator: Operator = Operator.END

    def __str__(self) -> str:
        return f'{self.operator.name}'


    def get_debug_repr(self) -> str:
        operator_name = self.operator.name

        return f'{operator_name}'

    
    def get_json_obj(self) -> str:
        q1 = str(self.operator.value)
        q2 = str(self.UNUSED_STATEMENT)
        q3 = str(self.UNUSED_STATEMENT)
        q4 = str(self.UNUSED_STATEMENT)
        return self._generate_intermediate_code_representation(q1, q2, q3, q4)


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
    

    def get_json_obj(self) -> list:
        obj = [
            quadruple.get_json_obj()
            for quadruple in self._list
        ]

        return obj

    
    def __str__(self) -> str:
        s = 'QuadrupleList(\n'

        for count, item in enumerate(self._list):
            s += f'\t{count : <4} {item.get_json_obj()}\n'
        
        s += ')'

        return s


class InvalidQuadrupleOperationError(RuntimeError):
    pass