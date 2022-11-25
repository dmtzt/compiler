from collections import namedtuple
from dataclasses import dataclass, field
from enum import Enum
from typing import Union

from compiler.operators import Operator
from compiler.variables import Type
from compiler.memory import BaseVirtualMemoryAddressEnum

class Limit(Enum):
    EXECUTION_STACK_LIMIT = 1000

    
class VariableScope(Enum):
    GLOBAL = 'global'
    VARIABLE = 'variable'
    TEMPORAL = 'temporal'
    CONSTANT = 'constant'
    POINTER = 'pointer'


class VirtualMemoryAddressResolver:
    _address_dict = {
        BaseVirtualMemoryAddressEnum.GLOBAL_VARIABLE_INT: (VariableScope.GLOBAL, Type.INT),
        BaseVirtualMemoryAddressEnum.GLOBAL_VARIABLE_REAL: (VariableScope.GLOBAL, Type.REAL),
        BaseVirtualMemoryAddressEnum.GLOBAL_VARIABLE_CHAR: (VariableScope.GLOBAL, Type.CHAR),
        BaseVirtualMemoryAddressEnum.GLOBAL_VARIABLE_BOOL: (VariableScope.GLOBAL, Type.BOOL),

        BaseVirtualMemoryAddressEnum.LOCAL_VARIABLE_INT: (VariableScope.VARIABLE, Type.INT),
        BaseVirtualMemoryAddressEnum.LOCAL_VARIABLE_REAL: (VariableScope.VARIABLE, Type.REAL),
        BaseVirtualMemoryAddressEnum.LOCAL_VARIABLE_CHAR: (VariableScope.VARIABLE, Type.CHAR),
        BaseVirtualMemoryAddressEnum.LOCAL_VARIABLE_BOOL: (VariableScope.VARIABLE, Type.BOOL),

        BaseVirtualMemoryAddressEnum.LOCAL_TEMPORAL_INT: (VariableScope.TEMPORAL, Type.INT),
        BaseVirtualMemoryAddressEnum.LOCAL_TEMPORAL_REAL: (VariableScope.TEMPORAL, Type.REAL),
        BaseVirtualMemoryAddressEnum.LOCAL_TEMPORAL_CHAR: (VariableScope.TEMPORAL, Type.CHAR),
        BaseVirtualMemoryAddressEnum.LOCAL_TEMPORAL_BOOL: (VariableScope.TEMPORAL, Type.BOOL),
        BaseVirtualMemoryAddressEnum.LOCAL_TEMPORAL_POINTER: (VariableScope.TEMPORAL, Type.POINTER),

        BaseVirtualMemoryAddressEnum.LOCAL_CONSTANT_INT: (VariableScope.CONSTANT, Type.INT),
        BaseVirtualMemoryAddressEnum.LOCAL_CONSTANT_REAL: (VariableScope.CONSTANT, Type.REAL),
        BaseVirtualMemoryAddressEnum.LOCAL_CONSTANT_CHAR: (VariableScope.CONSTANT, Type.CHAR),
        BaseVirtualMemoryAddressEnum.LOCAL_CONSTANT_BOOL: (VariableScope.CONSTANT, Type.BOOL),
        BaseVirtualMemoryAddressEnum.LOCAL_CONSTANT_STRING: (VariableScope.CONSTANT, Type.STRING),
    }

    @staticmethod
    def get_base_virtual_memory_address(virtual_memory_address: int) -> int:
        base = int(virtual_memory_address / 1000)
        base *= 1000

        return base


    @classmethod
    def resolve_virtual_memory_address(cls, virtual_memory_address: BaseVirtualMemoryAddressEnum) -> tuple[str, Type, int]:
        base_virtual_memory_address = int(virtual_memory_address / 1000) * 1000

        scope, type = cls._address_dict[BaseVirtualMemoryAddressEnum(base_virtual_memory_address)]
        index = virtual_memory_address % 1000

        return scope, type, index


ResolvedVariable = namedtuple("ResolvedVariable", ["scope", "type", "index"])


class Variable:
    def __init__(self, variable_dict: dict) -> None:
        self._id = variable_dict['id']
        self._type = Type(int(variable_dict['type']))
        self._virtual_memory_address = int(variable_dict['virtual_memory_address'])
        self._dimensions = variable_dict['dimensions']


    def __str__(self) -> str:
        return f'Variable({self._id} {self._type} {self._virtual_memory_address} {self._dimensions})'
    

class GlobalScope:
    def __init__(self, global_scope_dict: dict) -> None:
        self.id = global_scope_dict['id']

        self._activation_record = {
            VariableScope.GLOBAL: {Type(int(type)): global_scope_dict['activation_record']['variable'][type]
                         for type in global_scope_dict['activation_record']['variable']},
        }

        self._variable_table = {
            variable_id : Variable(global_scope_dict['variable_table'][variable_id])
            for variable_id in global_scope_dict['variable_table']
        }


    def get_variable_activation_record(self) -> dict:
        return self._activation_record[VariableScope.GLOBAL]



class Function:
    def __init__(self, function_dict: dict) -> None:
        self._id = function_dict['id']
        self._start_quadruple_number = int(function_dict['start_quadruple_number'])
        self._return_type = Type(int(function_dict['return_type']))

        self._activation_record = {
            VariableScope.VARIABLE: {Type(int(type)): function_dict['activation_record']['variable'][type]
                         for type in function_dict['activation_record']['variable']},
            VariableScope.TEMPORAL: {Type(int(type)): function_dict['activation_record']['temporal'][type]
                         for type in function_dict['activation_record']['temporal']},
            VariableScope.CONSTANT: {Type(int(type)): function_dict['activation_record']['constant'][type]
                         for type in function_dict['activation_record']['constant']},
        }

        self._variable_table = {
            variable_id : Variable(function_dict['variable_table'][variable_id])
            for variable_id in function_dict['variable_table']
        }

        self._parameter_table = [
            param_virtual_memory_address
            for param_virtual_memory_address in function_dict['parameter_table']
        ]


    def get_id(self) -> str:
        return self._id
    

    def get_start_quadruple_number(self) -> int:
        return self._start_quadruple_number
    

    def get_parameter_virtual_memory_address(self, number: int) -> int:
        return self._parameter_table[number - 1]
    

    def get_variable_activation_record(self) -> dict:
        return self._activation_record[VariableScope.VARIABLE]
    

    def get_temporal_activation_record(self) -> dict:
        return self._activation_record[VariableScope.TEMPORAL]


    def get_constant_activation_record(self) -> dict:
        return self._activation_record[VariableScope.CONSTANT]


    def __str__(self) -> str:
        s = f'Function({self._id} {self._return_type} {self._start_quadruple_number} {self._activation_record}\n'
        
        for variable_id in self._variable_table:
            s += '\t'
            s += self._variable_table[variable_id].__str__()
            s += '\n'

        return s


class FunctionDirectory:
    def __init__(self, function_directory_dict: dict) -> None:
        self._directory = {
            function_id : Function(function_directory_dict[function_id])
            for function_id in function_directory_dict
        }

    
    def __str__(self) -> str:
        s = 'FunctionDirectory('
        s += '\n'

        for function_id in self._directory:
            s += '\t'
            s += f'{function_id}: {self._directory[function_id].__str__()}'
            s += '\n'

        s += ')'

        return s
    

    def get_function(self, function_id: str) -> Function:
        return self._directory[function_id]


class GlobalMemory:
    def __init__(self, global_scope: GlobalScope) -> None:
        variable_activation_record = global_scope.get_variable_activation_record()

        self._memory = {
            type : [None] * variable_activation_record[type]
            for type in variable_activation_record
        }

    
    def set_value(
            self,
            type: Type,
            index: int,
            value: Union[int, float, bool, str],
    ) -> None:
        self._memory[type][index] = value

    
    def get_value(
            self,
            type: Type,
            index: int,
    ) -> Union[int, float, bool, str]:
        value = self._memory[type][index]

        if value is None:
            raise VariableNotInitializedError()

        return value
    

class FunctionCall:
    def __init__(self, function: Function) -> None:
        self._function_id = function.get_id()

        variable_activation_record = function.get_variable_activation_record()
        temporal_activation_record = function.get_temporal_activation_record()
        constant_activation_record = function.get_constant_activation_record()

        self._memory = {
            VariableScope.VARIABLE: {
                type : [None] * variable_activation_record[type]
                for type in variable_activation_record
            },
            VariableScope.TEMPORAL: {
                type : [None] * temporal_activation_record[type]
                for type in temporal_activation_record
            },
            VariableScope.CONSTANT: {
                type : [None] * constant_activation_record[type]
                for type in constant_activation_record
            },
        }

    def set_value(
            self,
            memory: str,
            type: Type,
            index: int,
            value: Union[int, float, bool, str],
    ) -> None:
        self._memory[memory][type][index] = value

    
    def get_value(
            self,
            memory: str,
            type: Type,
            index: int,
    ) -> Union[int, float, bool, str]:
        value = self._memory[memory][type][index]

        if value is None:
            raise VariableNotInitializedError()

        return self._memory[memory][type][index]

    
    def __str__(self) -> str:
        return f'FunctionCall({self._function_id}: {self._memory})'

        
class Quadruple:
    def __init__(self, quadruple: list) -> None:
        self._q1 = Operator(int(quadruple[0]))
        self._q2 = quadruple[1]
        self._q3 = quadruple[2]
        self._q4 = quadruple[3]

        
    def get_operator(self) -> Operator:
        return self._q1
    

    def get_q2(self) -> str:
        return self._q2
    

    def get_q3(self) -> str:
        return self._q3


    def get_q4(self) -> str:
        return self._q4


    def __str__(self) -> str:
        return f'Quadruple({self._q1} {self._q2} {self._q3} {self._q4})'
        

class QuadrupleList:
    def __init__(self, quadruple_list: list) -> None:
        self._list = [
            Quadruple(quadruple)
            for quadruple in quadruple_list
        ]


    def get_quadruple(self, number: int) -> Quadruple:
        return self._list[number]


    def __str__(self) -> str:
        s = 'QuadrupleList('
        s += '\n'

        for quadruple in self._list:
            s += '\t'
            s += quadruple.__str__()
            s += '\n'

        s += ')'

        return s


@dataclass
class ExecutionStack:
    _stack : list[FunctionCall] = field(default_factory=list)
    _limit : int = field(default=Limit.EXECUTION_STACK_LIMIT.value)

    def push_function_call(self, function_call: FunctionCall) -> None:
        if len(self._stack) > self._limit:
            raise StackOverflow()
        
        self._stack.append(function_call)


    def pop_function_call(self) -> None:
        self._stack.pop()

    
    def set_value_top_function_call(
            self,
            memory: str,
            type: Type,
            count: int,
            value: Union[int, float, bool, str],
    ) -> None:
        self._stack[-1].set_value(memory, type, count, value)

    
    def get_value_top_function_call(
            self,
            memory: str,
            type: Type,
            count: int,
    ) -> None:
        return self._stack[-1].get_value(memory, type, count)

    
    def __str__(self) -> str:
        s = 'ExecutionStack(\n'

        for function_call in self._stack:
            s += '\t'
            s += function_call.__str__()
            s += '\n'

        s += ')'

        return s


@dataclass
class ProgramCounterStack:
    _stack : list[int] = field(default_factory=list)

    def push_counter(self, pointer: int) -> None:
        self._stack.append(pointer)


    def pop_counter(self) -> int:
        return self._stack.pop()


class FunctionParameterStack:
    pass


class Memory:
    def __init__(self, activation_record_dict: dict) -> None:
        self._variable = []
        self._temporal = []
        self._constant = []


class StackOverflow(RuntimeError):
    pass


class VariableNotInitializedError(RuntimeError):
    pass


class IndexOutOfBoundsError(RuntimeError):
    pass