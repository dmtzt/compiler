from dataclasses import dataclass, field
from enum import Enum
from .variables import Type

def activation_record_variable_factory():
    return {
        Type.INT: 0,
        Type.REAL: 0,
        Type.CHAR: 0,
        Type.BOOL: 0
    }


def activation_record_temporal_factory():
    return {
        Type.INT: 0,
        Type.REAL: 0,
        Type.CHAR: 0,
        Type.BOOL: 0,
        Type.POINTER: 0
    }


def activation_record_constant_factory():
    return {
        Type.INT: 0,
        Type.REAL: 0,
        Type.CHAR: 0,
        Type.BOOL: 0,
        Type.STRING: 0
    }


@dataclass
class ActivationRecord:
    _variable : dict[Type, int] = field(default_factory=activation_record_variable_factory)
    _temporal : dict[Type, int] = field(default_factory=activation_record_temporal_factory)
    _constant : dict[Type, int] = field(default_factory=activation_record_constant_factory)

    def get_variable_counter(self, type: Type) -> int:
        return self._variable[type]


    def increment_variable_counter(self, type: Type) -> None:
        self._variable[type] += 1


    def increment_variable_counter_array(self, type: Type, array_size: int) -> None:
        self._variable[type] += array_size
        print(self._variable[type])

    def get_temporal_counter(self, type: Type) -> int:
        return self._temporal[type]


    def increment_temporal_counter(self, type: Type) -> None:
        self._temporal[type] += 1
    

    def get_pointer_counter(self) -> int:
        return self._temporal[Type.POINTER]


    def increment_pointer_counter(self) -> int:
        self._temporal[Type.POINTER] += 1


    def get_constant_counter(self, type: Type) -> int:
        return self._constant[type]


    def increment_constant_counter(self, type: Type) -> None:
        self._constant[type] += 1

    
    def get_intermediate_code_representation(self) -> dict:
        data = {
            "variable": {
                str(key): self._variable[key]
                for key in self._variable
            },
            "temporal": {
                str(key): self._temporal[key]
                for key in self._temporal
            },
            "constant": {
                str(key): self._constant[key]
                for key in self._constant
            },
        }

        return data


class VirtualMemoryAddressEnumeration(Enum):
    GLOBAL_VARIABLE_INT = 0
    GLOBAL_VARIABLE_REAL = 1000
    GLOBAL_VARIABLE_CHAR = 2000
    GLOBAL_VARIABLE_BOOL = 3000
    
    LOCAL_VARIABLE_INT = 4000
    LOCAL_VARIABLE_REAL = 5000
    LOCAL_VARIABLE_CHAR = 6000
    LOCAL_VARIABLE_BOOL = 7000

    LOCAL_TEMPORAL_INT = 8000
    LOCAL_TEMPORAL_REAL = 9000
    LOCAL_TEMPORAL_CHAR = 10000
    LOCAL_TEMPORAL_BOOL = 11000
    LOCAL_TEMP_POINTER = 12000

    LOCAL_CONSTANT_INT = 13000
    LOCAL_CONSTANT_REAL = 14000
    LOCAL_CONSTANT_CHAR = 15000
    LOCAL_CONSTANT_BOOL = 16000
    LOCAL_CONSTANT_STRING = 17000


class VirtualMemoryAddress:
    _global = {
        Type.INT: VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_INT.value,
        Type.REAL: VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_REAL.value,
        Type.CHAR: VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_CHAR.value,
        Type.BOOL: VirtualMemoryAddressEnumeration.GLOBAL_VARIABLE_BOOL.value,
    }

    _local = {
        Type.INT: VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_INT.value,
        Type.REAL: VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_REAL.value,
        Type.CHAR: VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_CHAR.value,
        Type.BOOL: VirtualMemoryAddressEnumeration.LOCAL_VARIABLE_BOOL.value,
    }

    _temporal = {
        Type.INT: VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_INT.value,
        Type.REAL: VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_REAL.value,
        Type.CHAR: VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_CHAR.value,
        Type.BOOL: VirtualMemoryAddressEnumeration.LOCAL_TEMPORAL_BOOL.value,
        Type.POINTER: VirtualMemoryAddressEnumeration.LOCAL_TEMP_POINTER.value,
    }

    _constant = {
        Type.INT: VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_INT.value,
        Type.REAL: VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_REAL.value,
        Type.CHAR: VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_CHAR.value,
        Type.BOOL: VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_BOOL.value,
        Type.STRING: VirtualMemoryAddressEnumeration.LOCAL_CONSTANT_STRING.value,
    }

    @classmethod
    def get_global_base_virtual_memory_address(cls, variable_type: Type) -> int:
        return cls._global[variable_type]


    @classmethod
    def get_local_base_virtual_memory_address(cls, variable_type: Type) -> int:
        return cls._local[variable_type]


    @classmethod
    def get_temporal_base_virtual_memory_address(cls, variable_type: Type) -> int:
        return cls._temporal[variable_type]
    

    @classmethod
    def get_pointer_base_virtual_memory_address(cls) -> int:
        return cls._temporal[Type.POINTER]


    @classmethod
    def get_constant_base_virtual_memory_address(cls, variable_type: Type) -> int:
        return cls._constant[variable_type]


class Memory:
    type_dict = {
        Type.INT: int,
        Type.REAL: float,
        Type.CHAR: str,
        Type.BOOL: str,
        Type.POINTER: int,
        Type.STRING: str
    }
