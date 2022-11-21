from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

from .memory import GlobalActivationRecord
from .memory import LocalActivationRecord
from .variables import Variable
from .variables import VariableTable
from .variables import ParameterTable
from .variables import Type


class Names(Enum):
    GLOBAL = 'global'
    MAIN = 'main'


@dataclass
class Module:
    _id : str = field(init=False)
    _activation_record : GlobalActivationRecord = field(default_factory=GlobalActivationRecord)
    _variable_table : VariableTable = field(default_factory=VariableTable)

    def get_id(self) -> Type:
        return self._id


    def set_id(self, id) -> None:
        self._id = id


    def get_variable_counter(self, variable_type: Type) -> int:
        return self._activation_record.get_variable_counter(variable_type)


    def increment_variable_counter(self, variable_type: Type) -> None:
        self._activation_record.increment_variable_counter(variable_type)

    
    def increment_variable_counter_array(self, variable_type: Type, array_size: int) -> None:
        self._activation_record.increment_variable_counter_array(variable_type, array_size)


    def get_variable(self, variable_id) -> Variable:
        return self._variable_table.get_variable(variable_id)

    
    def insert_variable(self, id: str, variable: Variable) -> None:
        self._variable_table.insert_variable(id, variable)


    def variable_exists(self, variable_id: str) -> bool:
        return self._variable_table.variable_exists(variable_id)

    
    def __str__(self) -> str:
        return f'Module({self._id} {self._activation_record.__str__()} {self._variable_table.__str__()}'


@dataclass
class Function(Module):
    _return_type : Type = field(init=False, default=None)
    _start_quadruple_number : int = field(init=False, default=None)
    _activation_record : LocalActivationRecord = field(default_factory=LocalActivationRecord)
    _parameter_table : ParameterTable = field(default_factory=ParameterTable)


    def get_return_type(self) -> Type:
        return self._return_type


    def set_return_type(self, return_type) -> None:
        self._return_type = return_type


    def set_start_quadruple_number(self, start_quadruple_number) -> None:
        self._start_quadruple_number = start_quadruple_number


    def get_parameter(self, number: int) -> Variable:
        return self._parameter_table.get_parameter(number)


    def insert_parameter(self, parameter: Variable) -> None:
        self._parameter_table.insert_parameter(parameter)


    def get_number_params(self) -> int:
        return self._parameter_table.get_number_parameters()


    def get_temporal_counter(self, variable_type: Type) -> int:
        return self._activation_record.get_temporal_counter(variable_type)


    def increment_temporal_counter(self, variable_type: Type) -> None:
        self._activation_record.increment_temporal_counter(variable_type)


    def get_pointer_counter(self) -> int:
        return self._activation_record.get_pointer_counter()


    def increment_pointer_counter(self) -> None:
        self._activation_record.increment_pointer_counter()

    
    def get_constant_counter(self, variable_type: Type) -> int:
        return self._activation_record.get_constant_counter(variable_type)


    def increment_constant_counter(self, variable_type: Type) -> None:
        self._activation_record.increment_constant_counter(variable_type)

    
    def __str__(self) -> str:
        return f'Function({self._id} {self._activation_record.__str__()} {self._variable_table.__str__()} {self._parameter_table.__str__()}'


@dataclass
class FunctionDirectory:
    _directory : dict[str, Function] = field(default_factory=dict)

    def __post_init__(self):
        self.generate_global_module()
        self.generate_main_function()


    def generate_global_module(self) -> None:
        global_id = Names.GLOBAL.value

        global_module = Module()
        global_module.set_id(global_id)
        self.insert_function(global_id, global_module)


    def generate_main_function(self) -> None:
        main_id = Names.MAIN.value
        main_module = Function()
        main_module.set_id(main_id)
        self.insert_function(main_id, main_module)


    def insert_function(self, id: str, function: Function) -> None:
        if id in self._directory:
            raise FunctionAlreadyDefinedException()

        self._directory[id] = function

    
    def get_global_variable(self, variable_id: str) -> Variable:
        return self._directory[Names.GLOBAL.value].get_variable(variable_id)

    
    def insert_global_variable(self, variable_id: str, variable: Variable) -> None:
        self._directory[Names.GLOBAL.value].insert_variable(variable_id, variable)

    
    def get_function_local_variable(self, function_id: str, variable_id: str) -> Variable:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_variable(variable_id)


    def insert_function_local_variable(self, function_id: str, variable_id: str, variable: Variable) -> None:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        self._directory[function_id].insert_variable(variable_id, variable)


    def get_function_number_parameters(self, function_id: str) -> int:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_number_params()


    def get_function_parameter(self, function_id: str, number: int) -> Variable:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_parameter(number)


    def insert_function_parameter(self, function_id: str, parameter: Variable) -> None:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].insert_parameter(parameter)

    
    def get_function_return_type(self, function_id: str) -> Type:
        if function_id not in self._directory:
            raise FunctionUndefinedException(function_id)

        return self._directory[function_id].get_return_type()

    
    def function_exists(self, function_id: str) -> bool:
        return function_id in self._directory


    def variable_exists(self, function_id: str, variable_id: str) -> bool:
        return self._directory[function_id].variable_exists(variable_id)


    def get_global_variable_counter(self, variable_type: Type) -> int:
        return self._directory[Names.GLOBAL.value].get_variable_counter(variable_type)

    
    def increment_global_variable_counter(self, variable_type: Type) -> None:
        self._directory[Names.GLOBAL.value].increment_variable_counter(variable_type)

    
    def increment_global_variable_counter_array(self, variable_type: Type, array_size: int) -> None:
        self._directory[Names.GLOBAL.value].increment_variable_counter_array(variable_type, array_size)


    def get_function_variable_counter(self, function_id: str, variable_type: Type) -> int:
        return self._directory[function_id].get_variable_counter(variable_type)


    def increment_function_variable_counter(self, function_id: str, variable_type: Type) -> None:
        self._directory[function_id].increment_variable_counter(variable_type)

    
    def increment_function_variable_counter_array(self, function_id: str, variable_type: Type, array_size: int) -> None:
        self._directory[function_id].increment_variable_counter_array(variable_type, array_size)

    
    def get_function_temporal_counter(self, function_id: str, variable_type: Type) -> int:
        return self._directory[function_id].get_temporal_counter(variable_type)


    def increment_function_temporal_counter(self, function_id: str, variable_type: Type) -> None:
        self._directory[function_id].increment_temporal_counter(variable_type)


    def get_function_pointer_counter(self, function_id: str) -> int:
        return self._directory[function_id].get_pointer_counter()


    def increment_function_pointer_counter(self, function_id: str) -> None:
        self._directory[function_id].increment_pointer_counter()


    def get_function_constant_counter(self, function_id: str, variable_type: Type) -> int:
        return self._directory[function_id].get_constant_counter(variable_type)


    def increment_function_constant_counter(self, function_id: str, variable_type: Type) -> None:
        self._directory[function_id].increment_constant_counter(variable_type)

    
    def __str__(self) -> str:
        s = 'FunctionDirectory('

        for function_id in self._directory:
            s += self._directory[function_id].__str__()
            s += '\n'

        s += ')'

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