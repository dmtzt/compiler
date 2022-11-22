from collections import deque
from dataclasses import dataclass, field
from enum import Enum

from compiler.operators import Operator
from compiler.variables import Type

class Limit(Enum):
    EXECUTION_STACK_LIMIT = 1000


class Variable:
    def __init__(self, variable_dict: dict) -> None:
        self._id = variable_dict['id']
        self._type = Type(int(variable_dict['type']))
        self._virtual_memory_address = int(variable_dict['virtual_memory_address'])
        self._dimensions = variable_dict['dimensions']


    def __str__(self) -> str:
        return f'Variable({self._id} {self._type} {self._virtual_memory_address} {self._dimensions})'


class Function:
    def __init__(self, function_dict: dict) -> None:
        self._id = function_dict['id']

        if function_dict['start_quadruple_number'] is None:
            self._start_quadruple_number = None
        else:
            self._start_quadruple_number = int(function_dict['start_quadruple_number'])

        if function_dict['return_type'] is None:
            self._return_type = None
        else:
            self._return_type = Type(int(function_dict['return_type']))

        self._activation_record = {
            'variable': {Type(int(type)): function_dict['activation_record']['variable'][type]
                         for type in function_dict['activation_record']['variable']},
            'temporal': {Type(int(type)): function_dict['activation_record']['temporal'][type]
                         for type in function_dict['activation_record']['temporal']},
            'constant': {Type(int(type)): function_dict['activation_record']['constant'][type]
                         for type in function_dict['activation_record']['constant']},
        }

        self._variable_table = {
            variable_id : Variable(function_dict['variable_table'][variable_id])
            for variable_id in function_dict['variable_table']
        }


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
    

class FunctionCall:
    def __init__(self) -> None:
        self._function_id = None
        self._memory = None


    def get_variable_int(self, count: int) -> int:
        return self._memory['variable'][Type.INT][count]


    def get_variable_real(self, count: int) -> float:
        return self._memory['variable'][Type.REAL][count]


    def get_variable_bool(self, count: int) -> bool:
        return self._memory['variable'][Type.BOOL][count]


    def get_variable_char(self, count: int) -> str:
        return self._memory['variable'][Type.CHAR][count]


    def set_variable_int(self, count: int, value: int) -> None:
        self._memory['variable'][Type.INT][count] = value


    def set_variable_real(self, count: int, value: float) -> None:
        self._memory['variable'][Type.REAL][count] = value


    def set_variable_bool(self, count: int, value: bool) -> None:
        self._memory['variable'][Type.BOOL][count] = value


    def set_variable_char(self, count: int, value: int) -> None:
        self._memory['variable'][Type.CHAR][count] = value

    
    def get_temporal_int(self, count: int) -> int:
        return self._memory['temporal'][Type.INT][count]


    def get_temporal_real(self, count: int) -> float:
        return self._memory['temporal'][Type.REAL][count]


    def get_temporal_bool(self, count: int) -> bool:
        return self._memory['temporal'][Type.BOOL][count]


    def get_temporal_char(self, count: int) -> str:
        return self._memory['temporal'][Type.CHAR][count]
    

    def get_temporal_pointer(self, count: int) -> str:
        return self._memory['temporal'][Type.POINTER][count]


    def set_temporal_int(self, count: int, value: int) -> None:
        self._memory['temporal'][Type.INT][count] = value


    def set_temporal_real(self, count: int, value: float) -> None:
        self._memory['temporal'][Type.REAL][count] = value


    def set_temporal_bool(self, count: int, value: bool) -> None:
        self._memory['temporal'][Type.BOOL][count] = value


    def set_temporal_char(self, count: int, value: int) -> None:
        self._memory['temporal'][Type.CHAR][count] = value

    
    def set_temporal_pointer(self, count: int, value: int) -> None:
        self._memory['temporal'][Type.POINTER][count] = value

        
class Quadruple:
    def __init__(self, quadruple: list) -> None:
        self._q1 = Operator(int(quadruple[0]))
        self._q2 = quadruple[1]
        self._q3 = quadruple[2]
        self._q4 = quadruple[3]

    
    def __str__(self) -> str:
        return f'Quadruple({self._q1} {self._q2} {self._q3} {self._q4})'
        

class QuadrupleList:
    def __init__(self, quadruple_list: list) -> None:
        self._list = [
            Quadruple(quadruple)
            for quadruple in quadruple_list
        ]


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
    _stack : deque[FunctionCall] = field(default_factory=deque)
    _limit : int = field(default=Limit.EXECUTION_STACK_LIMIT)

    def push_function(self, function: Function) -> None:
        if len(self._stack) > self._limit:
            raise StackOverflow()
        
        self._stack.append(function)


class FunctionParametersStack:
    pass


class Memory:
    def __init__(self, activation_record_dict: dict) -> None:
        self._variable = []
        self._temporal = []
        self._constant = []


class StackOverflow(RuntimeError):
    pass


class IndexOutOfBoundsError(RuntimeError):
    pass