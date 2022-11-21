from dataclasses import dataclass, field

from .variables import Operator
from .variables import Variable

@dataclass
class OperandStack:
    _stack : list[Variable] = field(default_factory=list)
    
    def push(self, operand: Variable) -> None:
        self._stack.append(operand)


    def pop(self) -> Variable:
        return self._stack.pop()


    def top(self) -> Variable:
        return self._stack[-1]


@dataclass
class OperatorStack:
    _stack : list[Operator] = field(default_factory=list)
    
    def push(self, operator: Operator) -> None:
        self._stack.append(operator)

    
    def pop(self) -> Operator:
        return self._stack.pop()

    
    def top(self) -> Operator:
        return self._stack[-1]


@dataclass
class JumpStack:
    _stack : list[int] = field(default_factory=list)
    
    def push(self, jump: int) -> None:
        self._stack.append(jump)

    
    def pop(self) -> int:
        return self._stack.pop()

    
    def top(self) -> int:
        return self._stack[-1]


@dataclass
class FunctionParameterCountStack:
    _stack : list[tuple[str, int]] = field(default_factory=list)
    
    def push_count(self, function_id: str) -> None:
        self._stack.append((function_id, 0))

    
    def pop_count(self) -> tuple[str, int]:
        return self._stack.pop()

    
    def get_top_count(self) -> tuple[str, int]:
        return self._stack[-1]

    
    def increment_top_count(self) -> None:
        function_id, count = self._stack[-1]
        count +=1

        self._stack[-1] = (function_id, count)
