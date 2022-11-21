from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from enum import Enum

from .operators import Operator

class Type(Enum):
    ERROR = -1
    VOID = 0
    INT = 1
    REAL = 2
    CHAR = 3
    BOOL = 4
    STRING = 5
    POINTER = 6


class Boolean(Enum):
    FALSE = 'False'
    TRUE = 'True'


@dataclass
class DimensionNode:
    _size : int
    _m : int = field(init=False, default=0)

    def get_size(self) -> int:
        return self._size


    def set_m(self, m: int) -> None:
        self._m = m


@dataclass
class Variable:
    _id : str = field(init=False)
    _type : Type = field(init=False)
    _virtual_memory_address : int = field(init=False)
    _dimension_nodes : deque[DimensionNode] = field(default_factory=deque)

    def get_id(self) -> str:
        return self._id

    
    def get_type(self) -> Type:
        return self._type

    
    def get_virtual_memory_address(self) -> int:
        return self._virtual_memory_address

    
    def get_number_dimensions(self) -> int:
        return len(self._dimension_nodes)


    def set_id(self, id: str) -> None:
        self._id = id

    
    def set_type(self, type: Type) -> None:
        self._type = type

    
    def set_virtual_memory_address(self, virtual_memory_address: int) -> None:
        self._virtual_memory_address = virtual_memory_address


    def append_dimension_node(self, dimension_node: DimensionNode) -> None:
        self._dimension_nodes.append(dimension_node)


    def get_dimension_size(self, dimension: int) -> int:
        return self._dimension_nodes[dimension].get_size()


    def set_dimension_node_m(self, dimension: int, m: int) -> None:
        self._dimension_nodes[dimension].set_m(m)

    
    def __str__(self) -> str:
        return f'Variable({self._id} {self._type} {self._virtual_memory_address} {self._dimension_nodes})'


class Builder(ABC):
    @property
    @abstractmethod
    def build(self) -> Variable:
        pass


    @abstractmethod
    def set_id(self, id: str) -> None:
        pass


    @abstractmethod
    def set_type(self, type: Type) -> None:
        pass


    @abstractmethod
    def set_virtual_memory_address(self, virtual_memory_address: int) -> None:
        pass


    @abstractmethod
    def append_dimension_node(self, dimension_node: DimensionNode) -> None:
        pass


    @abstractmethod
    def get_number_dimensions(self) -> int:
        pass


    @abstractmethod
    def get_dimension_size(self, dimension: int) -> int:
        pass


    @abstractmethod
    def set_dimension_node_m(self, dimension: int, m: int) -> None:
        pass

    
class VariableBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    
    def reset(self) -> None:
        self.__variable = Variable()


    def build(self) -> Variable:
        product = self.__variable
        self.reset()
        return product


    def set_id(self, id: str) -> None:
        self.__variable.set_id(id)


    def set_type(self, type: Type) -> None:
        self.__variable.set_type(type)

    
    def set_virtual_memory_address(self, virtual_memory_address: int) -> None:
        self.__variable.set_virtual_memory_address(virtual_memory_address)


    def append_dimension_node(self, dimension_node: DimensionNode) -> None:
        self.__variable.append_dimension_node(dimension_node)


    def get_number_dimensions(self) -> int:
        return self.__variable.get_number_dimensions()


    def get_dimension_size(self, dimension: int) -> int:
        return self.__variable.get_dimension_size(dimension)


    def set_dimension_node_m(self, dimension: int, m: int) -> None:
        self.__variable.set_dimension_node_m(dimension, m)


@dataclass
class VariableTable:
    _table: dict[str, Variable] = field(default_factory=dict)

    def get_variable(self, variable_id: str) -> Variable:
        if variable_id not in self._table:
            raise VariableUndefinedException()

        return self._table[variable_id]


    def insert_variable(self, variable_id: str, variable: Variable) -> None:
        if variable_id in self._table:
            raise VariableAlreadyDeclaredException()

        self._table[variable_id] = variable

    
    def variable_exists(self, variable_id: str) -> bool:
        return variable_id in self._table

    
    def __str__(self) -> str:
        s = f'VariableTable(\n'

        for variable_id in self._table:
            s += '\t'
            s += self._table[variable_id].__str__()
            s += '\n'

        s += ')'

        return s


@dataclass
class ParameterTable:
    _table: deque[Variable] = field(default_factory=deque)

    def get_number_parameters(self) -> int:
        return len(self._table)

    
    def insert_parameter(self, parameter: Variable) -> None:
        self._table.append(parameter)

    
    def get_parameter(self, number: int) -> Variable:
        return self._table[number - 1]

    
    def __str__(self) -> str:
        s = f'ParameterTable('

        for parameter in self._table:
            s += parameter.__str__()
            s += '\n'

        s += ')'

        return s


class SemanticTable():
    n_operands = len(Type) - 1
    n_operators = len(Operator)


    def __init__(self) -> None:
        self._create_table()
        self._fill_table()


    def _create_table(self):
        self._table = [[[Type.ERROR.value for _ in range(self.n_operators)] for _ in range(self.n_operands)] for _ in range(self.n_operands)]

    
    def _fill_table(self):
        self._fill_integer_operations()
        self._fill_real_operations()
        self._fill_char_operations()
        self._fill_bool_operations()

    
    def search_operation_result_type(
        self,
        type_1: Type,
        type_2: Type,
        operator: Operator
    ) -> Type:
        return Type(self._table[type_1.value][type_2.value][operator.value])


    def _fill_integer_operations(self):
        self.fill_integer_arithmetic_operations()
        self.fill_integer_relational_operations()
        self.fill_integer_assignment_operations()

    
    def fill_integer_arithmetic_operations(self):
        for operator in Operator.arithmetic_operators():
            self._table[Type.INT.value][Type.INT.value][operator.value] = Type.INT.value
            self._table[Type.INT.value][Type.REAL.value][operator.value] = Type.REAL.value
            self._table[Type.INT.value][Type.CHAR.value][operator.value] = Type.INT.value
            self._table[Type.INT.value][Type.BOOL.value][operator.value] = Type.ERROR.value

    
    def fill_integer_relational_operations(self):
        for operator in Operator.relational_operators():
            self._table[Type.INT.value][Type.INT.value][operator.value] = Type.BOOL.value
            self._table[Type.INT.value][Type.REAL.value][operator.value] = Type.BOOL.value
            self._table[Type.INT.value][Type.CHAR.value][operator.value] = Type.BOOL.value
            self._table[Type.INT.value][Type.BOOL.value][operator.value] = Type.ERROR.value

    
    def fill_integer_assignment_operations(self):
        self._table[Type.INT.value][Type.INT.value][Operator.ASGMT.value] = Type.INT.value
        self._table[Type.INT.value][Type.REAL.value][Operator.ASGMT.value] = Type.INT.value
        self._table[Type.INT.value][Type.CHAR.value][Operator.ASGMT.value] = Type.INT.value
        self._table[Type.INT.value][Type.BOOL.value][Operator.ASGMT.value] = Type.ERROR.value


    def _fill_real_operations(self):
        self.fill_real_arithmetic_operations()
        self.fill_real_relational_operations()
        self.fill_real_assignment_operations()


    def fill_real_arithmetic_operations(self):
        for operator in Operator.arithmetic_operators():
            self._table[Type.REAL.value][Type.INT.value][operator.value] = Type.REAL.value
            self._table[Type.REAL.value][Type.REAL.value][operator.value] = Type.REAL.value
            self._table[Type.REAL.value][Type.CHAR.value][operator.value] = Type.REAL.value
            self._table[Type.REAL.value][Type.BOOL.value][operator.value] = Type.ERROR.value

    
    def fill_real_relational_operations(self):
        for operator in Operator.relational_operators():
            self._table[Type.REAL.value][Type.INT.value][operator.value] = Type.BOOL.value
            self._table[Type.REAL.value][Type.REAL.value][operator.value] = Type.BOOL.value
            self._table[Type.REAL.value][Type.CHAR.value][operator.value] = Type.BOOL.value
            self._table[Type.REAL.value][Type.BOOL.value][operator.value] = Type.ERROR.value


    def fill_real_assignment_operations(self):
            self._table[Type.REAL.value][Type.INT.value][Operator.ASGMT.value] = Type.REAL.value
            self._table[Type.REAL.value][Type.REAL.value][Operator.ASGMT.value] = Type.REAL.value
            self._table[Type.REAL.value][Type.CHAR.value][Operator.ASGMT.value] = Type.REAL.value
            self._table[Type.REAL.value][Type.BOOL.value][Operator.ASGMT.value] = Type.ERROR.value

    
    def _fill_char_operations(self):
        self.fill_char_arithmetic_operations()
        self.fill_char_relational_operations()
        self.fill_char_assignment_operations()


    def fill_char_arithmetic_operations(self):
        for operator in Operator.arithmetic_operators():
            self._table[Type.CHAR.value][Type.INT.value][operator.value] = Type.CHAR.value
            self._table[Type.CHAR.value][Type.REAL.value][operator.value] = Type.CHAR.value
            self._table[Type.CHAR.value][Type.CHAR.value][operator.value] = Type.CHAR.value
            self._table[Type.CHAR.value][Type.BOOL.value][operator.value] = Type.ERROR.value

    
    def fill_char_relational_operations(self):
        for operator in Operator.relational_operators():
            self._table[Type.REAL.value][Type.INT.value][operator.value] = Type.BOOL.value
            self._table[Type.REAL.value][Type.REAL.value][operator.value] = Type.BOOL.value
            self._table[Type.REAL.value][Type.CHAR.value][operator.value] = Type.BOOL.value
            self._table[Type.REAL.value][Type.BOOL.value][operator.value] = Type.ERROR.value


    def fill_char_assignment_operations(self):
            self._table[Type.CHAR.value][Type.INT.value][Operator.ASGMT.value] = Type.CHAR.value
            self._table[Type.CHAR.value][Type.REAL.value][Operator.ASGMT.value] = Type.CHAR.value
            self._table[Type.CHAR.value][Type.CHAR.value][Operator.ASGMT.value] = Type.CHAR.value
            self._table[Type.CHAR.value][Type.BOOL.value][Operator.ASGMT.value] = Type.ERROR.value

    
    def _fill_bool_operations(self):
        self.fill_bool_arithmetic_operations()
        self.fill_bool_relational_operations()
        self.fill_bool_assignment_operations()


    def fill_bool_arithmetic_operations(self):
        for operator in Operator.arithmetic_operators():
            self._table[Type.BOOL.value][Type.INT.value][operator.value] = Type.ERROR.value
            self._table[Type.BOOL.value][Type.REAL.value][operator.value] = Type.ERROR.value
            self._table[Type.BOOL.value][Type.CHAR.value][operator.value] = Type.ERROR.value
            self._table[Type.BOOL.value][Type.BOOL.value][operator.value] = Type.ERROR.value

    
    def fill_bool_relational_operations(self):
        for operator in Operator.relational_operators():
            self._table[Type.BOOL.value][Type.INT.value][operator.value] = Type.ERROR.value
            self._table[Type.BOOL.value][Type.REAL.value][operator.value] = Type.ERROR.value
            self._table[Type.BOOL.value][Type.CHAR.value][operator.value] = Type.ERROR.value

        self._table[Type.BOOL.value][Type.BOOL.value][Operator.EQUAL.value] = Type.BOOL.value
        self._table[Type.BOOL.value][Type.BOOL.value][Operator.NEQUAL.value] = Type.BOOL.value
        self._table[Type.BOOL.value][Type.BOOL.value][Operator.LTHAN_EQUAL.value] = Type.ERROR.value
        self._table[Type.BOOL.value][Type.BOOL.value][Operator.LTHAN.value] = Type.ERROR.value
        self._table[Type.BOOL.value][Type.BOOL.value][Operator.GTHAN_EQUAL.value] = Type.ERROR.value
        self._table[Type.BOOL.value][Type.BOOL.value][Operator.GTHAN.value] = Type.ERROR.value

    
    def fill_bool_assignment_operations(self):
        self._table[Type.BOOL.value][Type.INT.value][Operator.ASGMT.value] = Type.ERROR.value
        self._table[Type.BOOL.value][Type.REAL.value][Operator.ASGMT.value] = Type.ERROR.value
        self._table[Type.BOOL.value][Type.CHAR.value][Operator.ASGMT.value] = Type.ERROR.value
        self._table[Type.BOOL.value][Type.BOOL.value][Operator.ASGMT.value] = Type.BOOL.value

    
    def __str__(self) -> str:
        s = 'SemanticTable(\n'

        for operand_1 in Type:
            for operand_2 in Type:
                s += '\t'
                for operator in Operator.arithmetic_operators():
                    s += f'({Type(operand_1).name}, {Type(operand_2).name}, {Operator.arithmetic_operators()(operator).name}, {Type(self.search_operation_result_type(operand_1, operand_2, operator)).name}) '

                for operator in Operator.relational_operators():
                    s += f'({Type(operand_1).name}, {Type(operand_2).name}, {Operator.relational_operators()(operator).name}, {Type(self.search_operation_result_type(operand_1, operand_2, operator)).name}) '
                
                s += '\n'

        s += ')'

        return s


class VariableAlreadyDeclaredException(RuntimeError):
    pass


class VariableUndefinedException(RuntimeError):
    pass


class OperationNotSupportedException(RuntimeError):
    pass