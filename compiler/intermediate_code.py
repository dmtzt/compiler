import json
from dataclasses import dataclass

from .functions import FunctionDirectory
from .functions import Scope
from .quadruples import QuadrupleList

@dataclass
class IntermediateCodeContainer:
    _global_scope: Scope
    _function_directory: FunctionDirectory
    _quadruple_list : QuadrupleList

    def get_json_obj(self) -> str:
        obj = {
            "global_scope": self._global_scope.get_json_obj(),
            "function_directory": self._function_directory.get_json_obj(),
            "quadruple_list": self._quadruple_list.get_json_obj()
        }

        json_str = json.dumps(obj, indent=4)
        return json_str
    

    def get_quadruple_list(self) -> QuadrupleList:
        return self._quadruple_list