from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from enum import Enum


class Type(Enum):
    ERROR = -1
    VOID = 0
    INT = 1
    REAL = 2
    CHAR = 3
    BOOL = 4
    STRING = 5


class Operator(Enum):
    ASGMT = 0

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    MODULO = 5

    UNARY_PLUS = 6
    UNARY_MINUS = 7

    EQUAL = 8
    NEQUAL = 9
    LTHAN_EQUAL = 10
    GTHAN_EQUAL = 11
    LTHAN = 12
    GTHAN = 13

    AND = 14
    OR = 15
    NOT = 16

    READ = 17
    PRINT = 18

    STORE_CONSTANT = 19

    GOTO = 20
    GOTOF = 21
    GOTOT = 22
    GOSUB = 23

    ERA = 24
    PARAM = 25
    RETURN = 26
    ENDFUNC = 27

    END = 28

    @classmethod
    def assignment_operator(cls):
        return cls.ASGMT


    @classmethod
    def arithmetic_operators(cls):
        return cls.PLUS, cls.MINUS, cls.TIMES, cls.DIVIDE, cls.MODULO


    @classmethod
    def unary_arithmetic_operators(cls):
        return cls.UNARY_PLUS, cls.UNARY_MINUS


    @classmethod
    def relational_operators(cls):
        return cls.EQUAL, cls.NEQUAL, cls.LTHAN_EQUAL, cls.GTHAN_EQUAL, cls.LTHAN, cls.GTHAN


class Boolean(Enum):
    FALSE = 0
    TRUE = 1


class Variable:
    def __init__(self) -> None:
        pass


    def set_id(self, id: str) -> None:
        self._id = id

    
    def set_type(self, type: Type) -> None:
        self._type = type

    
    def set_virtual_memory_address(self, virtual_memory_address: int) -> None:
        self._virtual_memory_address = virtual_memory_address

    
    def get_id(self) -> str:
        return self._id

    
    def get_type(self) -> Type:
        return self._type

    
    def get_virtual_memory_address(self) -> int:
        return self._virtual_memory_address

    
    def __str__(self) -> str:
        return f'{self._id} {self._type.name} {self._virtual_memory_address}'


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


class VariableTable():
    def __init__(self) -> None:
        self._table: dict[str, Variable] = dict()

    
    def insert_variable(self, variable_id: str, variable: Variable) -> None:
        if variable_id in self._table:
            raise VariableAlreadyDeclaredException()

        self._table[variable_id] = variable


    def get_variable(self, variable_id: str) -> Variable:
        if variable_id not in self._table:
            raise VariableUndefinedException()

        return self._table[variable_id]
    

    def __str__(self) -> str:
        s = "VariableTable[\n"

        for id in self._table:
            s += f'\t\t{id}: {self._table[id].__str__()},\n'

        s += ']'

        return s


class ParameterTable:
    def __init__(self) -> None:
        self._table: deque[Variable] = deque()


    def get_number_parameters(self) -> int:
        return len(self._table)

    
    def insert_parameter(self, parameter: Variable) -> None:
        self._table.append(parameter)

    
    def get_parameter(self, number: int) -> Variable:
        return self._table[number - 1]

    
    def __str__(self) -> str:
        s = "ParameterTable[\n"

        for param in self._table:
            s += f'\t\t{param.__str__()},\n'

        s += ']'

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