from dataclasses import dataclass

from .functions import FunctionDirectory
from .quadruples import QuadrupleList

@dataclass
class IntermediateCodeContainer:
    _function_directory: FunctionDirectory
    _quadruple_list : QuadrupleList