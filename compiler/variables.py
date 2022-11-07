from abc import ABC, abstractmethod
from enum import auto, Enum
from typing import Union

class Type(Enum):
    ERROR = -1
    INT = 0
    REAL = 1
    CHAR = 2
    BOOL = 3


class Operator(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count

    ASGMT = auto()
    PLUS = auto()
    MINUS = auto()
    TIMES = auto()
    DIVIDE = auto()
    MODULO = auto()
    EQUAL = auto()
    NEQUAL = auto()
    LTHAN_EQUAL = auto()
    GTHAN_EQUAL = auto()
    LTHAN = auto()
    GTHAN = auto()

    @classmethod
    def arithmetic_operators(cls):
        return cls.PLUS, cls.MINUS, cls.TIMES, cls.DIVIDE, cls.MODULO

    @classmethod
    def relational_operators(cls):
        return cls.EQUAL, cls.NEQUAL, cls.LTHAN_EQUAL, cls.GTHAN_EQUAL, cls.LTHAN, cls.GTHAN


class Variable:
    def __init__(self):
        self.__id = None
        self.__type = None


    def set_id(self, id: str) -> None:
        self.__id = id


    def set_type(self, type: Type) -> None:
        self.__type = type


    def get_id(self) -> str:
        return self.__id


    def get_type(self) -> Type:
        return self.__type


    def __str__(self) -> str:
        return f'Variable(id={self.__id} type={self.__type})'


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


class VariableTable():
    def __init__(self) -> None:
        self._table: dict[str, Variable] = {}

    
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