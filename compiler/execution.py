from dataclasses import dataclass, field
from enum import Enum

from compiler.operators import Operator
from compiler.variables import Type
from compiler.memory import VirtualMemoryAddressEnumeration

class Limit(Enum):
    EXECUTION_STACK_LIMIT = 1000


class VirtualMemoryAddressResolver:
    _address_dict = {
        VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_INT: ('global', Type.INT),
        VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_REAL: ('global', Type.REAL),
        VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_CHAR: ('global', Type.CHAR),
        VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_BOOL: ('global', Type.BOOL),
        VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_INT: ('variable', Type.INT),
        VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_REAL: ('variable', Type.REAL),
        VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_CHAR: ('variable', Type.CHAR),
        VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_BOOL: ('variable', Type.BOOL),
        VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_INT: ('temporal', Type.INT),
        VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_REAL: ('temporal', Type.REAL),
        VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_CHAR: ('temporal', Type.CHAR),
        VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_BOOL: ('temporal', Type.BOOL),
        VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_POINTER: ('temporal', Type.POINTER),
        VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_INT: ('constant', Type.INT),
        VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_REAL: ('constant', Type.REAL),
        VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_CHAR: ('constant', Type.CHAR),
        VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_BOOL: ('constant', Type.BOOL),
        VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_STRING: ('constant', Type.STRING),
    }

    @classmethod
    def resolve_virtual_address(cls, base_virtual_address: VirtualMemoryAddressEnumeration) -> tuple[str, Type]:
        return cls._address_dict[base_virtual_address]


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


    def get_id(self) -> str:
        return self._id
    

    def get_variable_activation_record(self) -> dict:
        return self._activation_record['variable']
    

    def get_temporal_activation_record(self) -> dict:
        return self._activation_record['temporal']


    def get_constant_activation_record(self) -> dict:
        return self._activation_record['constant']


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

class FunctionCall:
    def __init__(self, function: Function) -> None:
        self._function_id = function.get_id()

        variable_activation_record = function.get_variable_activation_record()
        temporal_activation_record = function.get_temporal_activation_record()
        constant_activation_record = function.get_constant_activation_record()

        self._memory = {
            'variable': {
                type : [None] * variable_activation_record[type]
                for type in variable_activation_record
            },
            'temporal': {
                type : [None] * temporal_activation_record[type]
                for type in temporal_activation_record
            },
            'constant': {
                type : [None] * constant_activation_record[type]
                for type in constant_activation_record
            },
        }


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
    

    def get_temporal_pointer(self, count: int) -> int:
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

    
    def get_constant_int(self, count: int) -> int:
        return self._memory['constant'][Type.INT][count]


    def get_constant_real(self, count: int) -> float:
        return self._memory['constant'][Type.REAL][count]


    def get_constant_bool(self, count: int) -> bool:
        return self._memory['constant'][Type.BOOL][count]


    def get_constant_char(self, count: int) -> str:
        return self._memory['constant'][Type.CHAR][count]
    

    def get_constant_string(self, count: int) -> str:
        return self._memory['constant'][Type.STRING][count]


    def set_constant_int(self, count: int, value: int) -> None:
        self._memory['constant'][Type.INT][count] = value


    def set_constant_real(self, count: int, value: float) -> None:
        self._memory['constant'][Type.REAL][count] = value


    def set_constant_bool(self, count: int, value: bool) -> None:
        self._memory['constant'][Type.BOOL][count] = value


    def set_constant_char(self, count: int, value: int) -> None:
        self._memory['constant'][Type.CHAR][count] = value

    
    def set_constant_string(self, count: int, value: str) -> None:
        self._memory['constant'][Type.STRING][count] = value

    
    def __str__(self) -> str:
        return f'FunctionCall({self._function_id}: {self._memory})'

        
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
    _stack : list[FunctionCall] = field(default_factory=list)
    _limit : int = field(default=Limit.EXECUTION_STACK_LIMIT.value)

    def push_function_call(self, function_call: FunctionCall) -> None:
        if len(self._stack) > self._limit:
            raise StackOverflow()
        
        self._stack.append(function_call)


    def pop_function_call(self) -> None:
        self._stack.pop()

    
    def __str__(self) -> str:
        s = 'ExecutionStack(\n'

        for function_call in self._stack:
            s += '\t'
            s += function_call.__str__()
            s += '\n'

        s += ')'

        return s



class InstructionPointerStack:
    _stack : list[int] = field(default_factory=list)

    def push_pointer(self, pointer: int) -> None:
        self._stack.append(pointer)


    def pop_pointer(self) -> int:
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


class IndexOutOfBoundsError(RuntimeError):
    pass