from abc import ABC, abstractmethod
from enum import Enum
from typing import Union


class Variable:
    def __init__(self):
        self.__id = None
        self.__type = None


    def set_id(self, id):
        self.__id = id


    def set_type(self, type):
        self.__type = type


    def get_id(self) -> str:
        return self.__id


    def get_type(self) -> str:
        return self.__type


    def __str__(self) -> str:
        return f'Variable(id={self.__id} = type={self.__type})'


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Variable:
        pass


    @abstractmethod
    def set_id(self, id: str) -> None:
        pass


    @abstractmethod
    def set_type(self, type: str) -> None:
        pass

    
class VariableBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    
    def reset(self) -> None:
        self.__variable = Variable()


    def product(self) -> Variable:
        product = self.__variable
        self.reset()
        return product


    def set_id(self, id: str) -> None:
        self.__variable.set_id(id)


    def set_type(self, type: str) -> None:
        self.__variable.set_type(type)


class VariableTable():
    def __init__(self) -> None:
        self._table = {}

    
    def insert_variable(self, id: str, variable: Variable) -> None:
        if id in self._table:
            raise VariableAlreadyDeclaredException()

        self._table[id] = variable
    
    def __str__(self) -> str:
        s = "VariableTable[\n"

        for id in self._table:
            s += f'\t\t{id}: {self._table[id].__str__()},\n'

        s += ']'

        return s


class Operand(Enum):
    INT = 0
    REAL = 1
    CHAR = 2
    BOOL = 3


class ArithmeticOperator(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIVIDE = 3
    MODULO = 4


class RelationalOperator(Enum):
    EQUAL = 5
    NEQUAL = 6
    LTHAN_EQUAL = 7
    GTHAN_EQUAL = 8
    LTHAN = 9
    GTHAN = 10


class ResultType(Enum):
    ERROR = -1
    INT = 0
    REAL = 1
    CHAR = 2
    BOOL = 3


class SemanticTable():
    n_operands = len(Operand)
    n_operators = len(ArithmeticOperator) + len(RelationalOperator)

    def __init__(self) -> None:
        self.create_table()
        self.fill_table()


    def create_table(self):
        self._table = [[[ResultType.ERROR.value for _ in range(self.n_operators)] for _ in range(self.n_operands)] for _ in range(self.n_operands)]

    
    def fill_table(self):
        self.fill_integer_operations()
        self.fill_real_operations()
        self.fill_char_operations()
        self.fill_bool_operations()

    
    def search_operation_result_type(self, operand_1: Operand, operand_2: Operand, operator: Union[ArithmeticOperator, RelationalOperator]) -> ResultType:
        return self._table[operand_1.value][operand_2.value][operator.value]


    def __str__(self) -> str:
        s = 'SemanticTable(\n'

        for operand_1 in Operand:
            for operand_2 in Operand:
                s += '\t'
                for operator in ArithmeticOperator:
                    s += f'({Operand(operand_1).name}, {Operand(operand_2).name}, {ArithmeticOperator(operator).name}, {ResultType(self.search_operation_result_type(operand_1, operand_2, operator)).name}) '

                for operator in RelationalOperator:
                    s += f'({Operand(operand_1).name}, {Operand(operand_2).name}, {RelationalOperator(operator).name}, {ResultType(self.search_operation_result_type(operand_1, operand_2, operator)).name}) '
                
                s += '\n'

        s += ')'

        return s


    def fill_integer_operations(self):
        self.fill_integer_arithmetic_operations()
        self.fill_integer_relational_operations()

    
    def fill_integer_arithmetic_operations(self):
        for operator in ArithmeticOperator:
            self._table[Operand.INT.value][Operand.INT.value][operator.value] = ResultType.INT.value
            self._table[Operand.INT.value][Operand.REAL.value][operator.value] = ResultType.REAL.value
            self._table[Operand.INT.value][Operand.CHAR.value][operator.value] = ResultType.INT.value
            self._table[Operand.INT.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value

    
    def fill_integer_relational_operations(self):
        for operator in RelationalOperator:
            self._table[Operand.INT.value][Operand.INT.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.INT.value][Operand.REAL.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.INT.value][Operand.CHAR.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.INT.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value


    def fill_real_operations(self):
        self.fill_real_arithmetic_operations()
        self.fill_real_relational_operations()


    def fill_real_arithmetic_operations(self):
        for operator in ArithmeticOperator:
            self._table[Operand.REAL.value][Operand.INT.value][operator.value] = ResultType.REAL.value
            self._table[Operand.REAL.value][Operand.REAL.value][operator.value] = ResultType.REAL.value
            self._table[Operand.REAL.value][Operand.CHAR.value][operator.value] = ResultType.REAL.value
            self._table[Operand.REAL.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value

    
    def fill_real_relational_operations(self):
        for operator in RelationalOperator:
            self._table[Operand.REAL.value][Operand.INT.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.REAL.value][Operand.REAL.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.REAL.value][Operand.CHAR.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.REAL.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value

    
    def fill_char_operations(self):
        self.fill_char_arithmetic_operations()
        self.fill_char_relational_operations()


    def fill_char_arithmetic_operations(self):
        for operator in ArithmeticOperator:
            self._table[Operand.CHAR.value][Operand.INT.value][operator.value] = ResultType.INT.value
            self._table[Operand.CHAR.value][Operand.REAL.value][operator.value] = ResultType.REAL.value
            self._table[Operand.CHAR.value][Operand.CHAR.value][operator.value] = ResultType.INT.value
            self._table[Operand.CHAR.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value

    
    def fill_char_relational_operations(self):
        for operator in RelationalOperator:
            self._table[Operand.REAL.value][Operand.INT.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.REAL.value][Operand.REAL.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.REAL.value][Operand.CHAR.value][operator.value] = ResultType.BOOL.value
            self._table[Operand.REAL.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value

    
    def fill_bool_operations(self):
        self.fill_bool_arithmetic_operations()
        self.fill_bool_relational_operations()


    def fill_bool_arithmetic_operations(self):
        for operator in ArithmeticOperator:
            self._table[Operand.BOOL.value][Operand.INT.value][operator.value] = ResultType.ERROR.value
            self._table[Operand.BOOL.value][Operand.REAL.value][operator.value] = ResultType.ERROR.value
            self._table[Operand.BOOL.value][Operand.CHAR.value][operator.value] = ResultType.ERROR.value
            self._table[Operand.BOOL.value][Operand.BOOL.value][operator.value] = ResultType.ERROR.value

    
    def fill_bool_relational_operations(self):
        for operator in RelationalOperator:
            self._table[Operand.BOOL.value][Operand.INT.value][operator.value] = ResultType.ERROR.value
            self._table[Operand.BOOL.value][Operand.REAL.value][operator.value] = ResultType.ERROR.value
            self._table[Operand.BOOL.value][Operand.CHAR.value][operator.value] = ResultType.ERROR.value

        self._table[Operand.BOOL.value][Operand.BOOL.value][RelationalOperator.EQUAL.value] = ResultType.BOOL.value
        self._table[Operand.BOOL.value][Operand.BOOL.value][RelationalOperator.NEQUAL.value] = ResultType.BOOL.value
        self._table[Operand.BOOL.value][Operand.BOOL.value][RelationalOperator.LTHAN_EQUAL.value] = ResultType.ERROR.value
        self._table[Operand.BOOL.value][Operand.BOOL.value][RelationalOperator.LTHAN.value] = ResultType.ERROR.value
        self._table[Operand.BOOL.value][Operand.BOOL.value][RelationalOperator.GTHAN_EQUAL.value] = ResultType.ERROR.value
        self._table[Operand.BOOL.value][Operand.BOOL.value][RelationalOperator.GTHAN.value] = ResultType.ERROR.value


class VariableAlreadyDeclaredException(RuntimeError):
    pass


class VariableNotFoundException(RuntimeError):
    pass


class OperationNotSupportedException(RuntimeError):
    pass