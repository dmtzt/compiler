import json
from dataclasses import dataclass

from .functions import FunctionDirectory
from .quadruples import QuadrupleList

@dataclass
class IntermediateCodeContainer:
    _function_directory: FunctionDirectory
    _quadruple_list : QuadrupleList

    def get_intermediate_code_representation(self) -> str:
        data = {
            "function_directory": self._function_directory.get_intermediate_code_representation(),
            "quadruple_list": self._quadruple_list.get_intermediate_code_representation()
        }

        json_str = json.dumps(data, indent=4)
        return json_str
    

    def get_quadruple_list(self) -> QuadrupleList:
        return self._quadruple_list