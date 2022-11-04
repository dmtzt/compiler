from abc import ABC, abstractmethod

from .variables import Variable
from .variables import VariableTable
from .command import Command

class Function():
    def __init__(self):
        self.__id = None
        self.__return_type = None
        self._variable_table = VariableTable()


    def set_id(self, id):
        self.__id = id


    def set_return_type(self, return_type):
        self.__return_type = return_type

    
    def get_id(self) -> str:
        return self.__id


    def get_return_type(self) -> str:
        return self.__return_type

    
    def insert_variable(self, id: str, variable: Variable) -> None:
        self._variable_table.insert_variable(id, variable)


    def __str__(self) -> str:
        return f'Function(id={self.__id}, return_type={self.__return_type}, variables={self._variable_table.__str__()})'


class FunctionDirectory():
    def __init__(self) -> None:
        self._directory : dict[str, Function] = {}

    
    def insert_function(self, id: str, function: Function) -> None:
        if id in self._directory:
            raise FunctionAlreadyDeclaredException()

        self._directory[id] = function


    def insert_function_variable(self, function_id: str, variable_id: str, variable: Variable) -> None:
        if function_id not in self._directory:
            raise FunctionNotFoundException(function_id)

        self._directory[function_id].insert_variable(variable_id, variable)

    
    def __str__(self) -> str:
        s = "FunctionDirectory[\n"

        for id in self._directory:
            s += f'\t{id}: {self._directory[id].__str__()}\n'

        s += ']'

        return s


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Function:
        pass


    @abstractmethod
    def set_id(self, id: str) -> None:
        pass


    @abstractmethod
    def set_return_type(self, return_type: str) -> None:
        pass

    
class FunctionBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    
    def reset(self) -> None:
        self.__function = Function()


    def product(self) -> Function:
        product = self.__function
        self.reset()
        return product


    def set_id(self, id: str) -> None:
        self.__function.set_id(id)


    def set_return_type(self, return_type: str) -> None:
        self.__function.set_return_type(return_type)


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


class InsertFunctionToDirectoryCommand(Command):
    def __init__(self, directory: FunctionDirectory, function_id: str, function: Function) -> None:
        self._directory = directory
        self._function_id = function_id
        self._function = function

    
    def execute(self) -> None:
        self._directory.insert_function(self._function_id, self._function)


class InsertVariableToFunctionCommand(Command):
    def __init__(self, directory: FunctionDirectory, function_id: str, variable_id: str, variable: Variable) -> None:
        self._directory = directory
        self._function_id = function_id
        self._variable_id = variable_id
        self._variable = variable

    
    def execute(self) -> None:
        self._directory.insert_function_variable(self._function_id, self._variable_id, self._variable)


class FunctionAlreadyDeclaredException(RuntimeError):
    pass


class FunctionNotFoundException(RuntimeError):
    pass