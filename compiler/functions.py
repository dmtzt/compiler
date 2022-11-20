from abc import ABC, abstractmethod
from collections import defaultdict

from .variables import Variable
from .variables import VariableTable
from .variables import ParameterTable
from .variables import Type


class VirtualMemoryAddress:
    _global = dict()
    _local = dict()
    _constant = dict()
    _temporal = dict()
    _pointer = dict()

    _global[Type.INT] = 0
    _global[Type.REAL] = 1000
    _global[Type.CHAR] = 2000
    _global[Type.BOOL] = 3000
    _global[Type.STRING] = 4000

    _local[Type.INT] = 5000
    _local[Type.REAL] = 6000
    _local[Type.CHAR] = 7000
    _local[Type.BOOL] = 8000
    _local[Type.STRING] = 9000

    _constant[Type.INT] = 10000
    _constant[Type.REAL] = 11000
    _constant[Type.CHAR] = 12000
    _constant[Type.BOOL] = 13000
    _constant[Type.STRING] = 14000

    _temporal[Type.INT] = 15000
    _temporal[Type.REAL] = 16000
    _temporal[Type.CHAR] = 17000
    _temporal[Type.BOOL] = 18000
    _temporal[Type.STRING] = 19000

    _pointer[Type.INT] = 20000
    _pointer[Type.REAL] = 21000
    _pointer[Type.CHAR] = 22000
    _pointer[Type.BOOL] = 23000
    _pointer[Type.STRING] = 24000
    
    @classmethod
    def get_global_base_virtual_memory_address(cls, type: Type) -> int:
        if type not in cls._global:
            raise UndefinedTypeBaseVirtualAddressError()

        return cls._global[type]

    
    @classmethod
    def get_local_base_virtual_memory_address(cls, type: Type) -> int:
        if type not in cls._local:
            raise UndefinedTypeBaseVirtualAddressError()

        return cls._local[type]

    
    @classmethod
    def get_constant_base_virtual_memory_address(cls, type: Type) -> int:
        if type not in cls._constant:
            raise UndefinedTypeBaseVirtualAddressError()

        return cls._constant[type]

    
    @classmethod
    def get_temporal_base_virtual_memory_address(cls, type: Type) -> int:
        if type not in cls._temporal:
            raise UndefinedTypeBaseVirtualAddressError()

        return cls._temporal[type]

    
    @classmethod
    def get_pointer_base_virtual_memory_address(cls, type: Type) -> int:
        if type not in cls._pointer:
            raise UndefinedTypeBaseVirtualAddressError()

        return cls._pointer[type]


class ActivationRecord:
    def __init__(self) -> None:
        self._local = defaultdict(int)
        self._constant = defaultdict(int)
        self._temporal = defaultdict(int)
        self._pointer = defaultdict(int)

    def increment_local_counter(self, type: Type) -> None:
        self._local[type] += 1

    
    def increment_constant_counter(self, type: Type) -> None:
        self._constant[type] += 1

    
    def increment_temporal_counter(self, type: Type) -> None:
        self._temporal[type] += 1

    
    def increment_pointer_counter(self, type: Type) -> None:
        self._pointer[type] += 1

    
    def get_local_counter(self, type: Type) -> int:
        return self._local[type]


    def get_constant_counter(self, type: Type) -> int:
        return self._constant[type]

    
    def get_temporal_counter(self, type: Type) -> int:
        return self._temporal[type]

    
    def get_pointer_counter(self, type: Type) -> int:
        return self._pointer[type]


class Memory:
    pass


class Function:
    def __init__(self) -> None:
        self._id = None
        self._return_type = None
        self._start_quadruple_number = None
        self._activation_record = ActivationRecord()
        self._parameter_table = ParameterTable()
        self._variable_table = VariableTable()


    def set_id(self, id) -> None:
        self._id = id

    
    def set_return_type(self, return_type) -> None:
        self._return_type = return_type

    
    def get_return_type(self) -> Type:
        return self._return_type


    def set_start_quadruple_number(self, start_quadruple_number) -> None:
        self._start_quadruple_number = start_quadruple_number


    def insert_variable(self, id: str, variable: Variable) -> None:
        self._variable_table.insert_variable(id, variable)

    
    def get_variable(self, variable_id) -> Variable:
        return self._variable_table.get_variable(variable_id)

    
    def variable_exists(self, variable_id: str) -> bool:
        return self._variable_table.variable_exists(variable_id)

    
    def insert_parameter(self, parameter: Variable) -> None:
        self._parameter_table.insert_parameter(parameter)


    def get_parameter(self, number: int) -> Variable:
        return self._parameter_table.get_parameter(number)

    
    def get_number_params(self) -> int:
        return self._parameter_table.get_number_parameters()

    
    def increment_local_counter(self, type: Type) -> None:
        self._activation_record.increment_local_counter(type)

    
    def increment_constant_counter(self, type: Type) -> None:
        self._activation_record.increment_constant_counter(type)

    
    def increment_temporal_counter(self, type: Type) -> None:
        self._activation_record.increment_temporal_counter(type)

    
    def increment_pointer_counter(self, type: Type) -> None:
        self._activation_record.increment_pointer_counter(type)

    
    def get_local_counter(self, type: Type) -> int:
        return self._activation_record.get_local_counter(type)


    def get_constant_counter(self, type: Type) -> int:
        return self._activation_record.get_constant_counter(type)

    
    def get_temporal_counter(self, type: Type) -> int:
        return self._activation_record.get_temporal_counter(type)

    
    def get_pointer_counter(self, type: Type) -> int:
        return self._activation_record.get_pointer_counter(type)


    def __str__(self) -> str:
        return f'Function(id={self._id} type={self._return_type} start={self._start_quadruple_number} vars=\n\t{self._variable_table.__str__()} params=\n\t{self._parameter_table.__str__()})'


class FunctionDirectory():
    GLOBAL_SCOPE_ID = 'global'
    MAIN_SCOPE_ID = 'main'

    # FIX: operations that involve global variables
    def __init__(self) -> None:
        self._directory : dict[str, Function] = {}
        
        self.create_global_scope()
        self.create_main_scope()

    
    def create_global_scope(self) -> None:
        global_scope_id = self.GLOBAL_SCOPE_ID

        global_scope = Function()
        global_scope.set_id(global_scope_id)
        self.insert_function(global_scope_id, global_scope)

    
    def create_main_scope(self) -> None:
        main_id = self.MAIN_SCOPE_ID

        main_scope = Function()
        main_scope.set_id(main_id)
        self.insert_function(main_id, main_scope)

    
    def insert_function(self, id: str, function: Function) -> None:
        if id in self._directory:
            raise FunctionAlreadyDefinedException()

        self._directory[id] = function


    def insert_global_variable(self, variable_id: str, variable: Variable) -> None:
        self._directory[self.GLOBAL_SCOPE_ID].insert_variable(variable_id, variable)


    def get_global_variable(self, variable_id: str) -> Variable:
        return self._directory[self.GLOBAL_SCOPE_ID].get_variable(variable_id)


    def insert_function_variable(self, function_id: str, variable_id: str, variable: Variable) -> None:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        self._directory[function_id].insert_variable(variable_id, variable)

    
    def insert_function_parameter(self, function_id: str, parameter: Variable) -> None:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        self._directory[function_id].insert_parameter(parameter)

    
    def get_function_variable(self, function_id: str, variable_id: str) -> Variable:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_variable(variable_id)

    
    def get_function_number_parameters(self, function_id: str) -> int:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_number_params()

    
    def get_function_parameter(self, function_id: str, number: int) -> Variable:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_parameter(number)

    
    def get_function_return_type(self, function_id: str) -> Type:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_return_type()

    
    def function_exists(self, function_id: str) -> bool:
        return function_id in self._directory

    
    def variable_exists(self, function_id: str, variable_id: str) -> bool:
        return self._directory[function_id].variable_exists(variable_id)

    
    def increment_global_local_variable_counter(self, type: Type) -> None:
        self._directory[self.GLOBAL_SCOPE_ID].increment_local_counter(type)


    def increment_global_constant_variable_counter(self, type: Type) -> None:
        self._directory[self.GLOBAL_SCOPE_ID].increment_constant_counter(type)


    def increment_global_temporal_variable_counter(self, type: Type) -> None:
        self._directory[self.GLOBAL_SCOPE_ID].increment_temporal_counter(type)

    
    def increment_global_pointer_variable_counter(self, type: Type) -> None:
        self._directory[self.GLOBAL_SCOPE_ID].increment_pointer_counter(type)


    def get_global_local_variable_counter(self, type: Type) -> int:
        return self._directory[self.GLOBAL_SCOPE_ID].get_local_counter(type)


    def get_global_constant_variable_counter(self, type: Type) -> int:
        return self._directory[self.GLOBAL_SCOPE_ID].get_constant_counter(type)

    
    def get_global_temporal_variable_counter(self, type: Type) -> int:
        return self._directory[self.GLOBAL_SCOPE_ID].get_temporal_counter(type)

    
    def get_global_pointer_variable_counter(self, type: Type) -> int:
        return self._directory[self.GLOBAL_SCOPE_ID].get_pointer_counter(type)


    def get_function_local_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_local_counter(type)


    def get_function_constant_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_constant_counter(type)

    
    def get_function_temporal_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_temporal_counter(type)

    
    def get_function_pointer_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_pointer_counter(type)

    
    def increment_function_local_variable_counter(self, function_id: str, type: Type) -> None:
        self._directory[function_id].increment_local_counter(type)

    
    def increment_function_constant_variable_counter(self, function_id: str, type: Type) -> None:
        self._directory[function_id].increment_constant_counter(type)

    
    def increment_function_temporal_variable_counter(self, function_id: str, type: Type) -> None:
        self._directory[function_id].increment_temporal_counter(type)

    
    def increment_function_pointer_variable_counter(self, function_id: str, type: Type) -> None:
        self._directory[function_id].increment_pointer_counter(type)

    
    def get_function_local_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_local_counter(type)


    def get_function_constant_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_constant_counter(type)

    
    def get_function_temporal_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_temporal_counter(type)

    
    def get_function_pointer_variable_counter(self, function_id: str, type: Type) -> int:
        return self._directory[function_id].get_pointer_counter(type)

    
    def __str__(self) -> str:
        s = "FunctionDirectory[\n"

        for id in self._directory:
            s += f'\t{id}: {self._directory[id].__str__()}\n'

        s += ']'

        return s


class Builder(ABC):
    @property
    @abstractmethod
    def build(self) -> Function:
        pass


    @abstractmethod
    def set_id(self, id: str) -> None:
        pass


    @abstractmethod
    def set_return_type(self, return_type: str) -> None:
        pass


    @abstractmethod
    def set_start_quadruple_number(self, start_quadruple_number: int) -> None:
        pass

    
class FunctionBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    
    def reset(self) -> None:
        self.__function = Function()


    def build(self) -> Function:
        product = self.__function
        self.reset()
        return product


    def set_id(self, id: str) -> None:
        self.__function.set_id(id)


    def set_return_type(self, return_type: str) -> None:
        self.__function.set_return_type(return_type)


    def set_start_quadruple_number(self, start_quadruple_number: int) -> None:
        self.__function.set_start_quadruple_number(start_quadruple_number)


class FunctionDirector:
    def __init__(self) -> None:
        self._builder = None

    
    @property
    def builder(self) -> Builder:
        return self._builder

    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    
    def build_main_function(self) -> None:
        self._builder.set_id('main')
        self._builder.set_return_type(None)


    def build_global_scope(self) -> None:
        self._builder.set_id('global')
        self._builder.set_return_type(None)


class FunctionAlreadyDefinedException(RuntimeError):
    pass


class FunctionUndefinedException(RuntimeError):
    pass


class IncorrectFunctionParameterAmountException(RuntimeError):
    pass


class IncorrectFunctionParameterTypeException(RuntimeError):
    pass


class IncorrectFunctionReturnTypeException(RuntimeError):
    pass


class VariableUndefinedException(RuntimeError):
    pass


class UndefinedTypeBaseVirtualAddressError(RuntimeError):
    pass