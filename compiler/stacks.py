from .variables import Operator
from .variables import Variable

class OperandStack():
    def __init__(self) -> None:
        self._stack = list()

    
    def push(self, operand: Variable) -> None:
        self._stack.append(operand)

    
    def pop(self) -> Variable:
        return self._stack.pop()

    
    def top(self) -> Variable:
        return self._stack[-1]

    
    def __str__(self) -> str:
        s = 'OperandStack(stack='

        for item in self._stack:
            s += f'{item.__str__()}, '

        s += ')'

        return s


class OperatorStack():
    def __init__(self) -> None:
        self._stack = list()

    
    def push(self, operator: Operator) -> None:
        self._stack.append(operator)

    
    def pop(self) -> Operator:
        return self._stack.pop()

    
    def top(self) -> Operator:
        return self._stack[-1]

    
    def __str__(self) -> str:
        return f'OperatorStack(stack={self._stack})'


class JumpStack():
    def __init__(self) -> None:
        self._stack = list()

    
    def push(self, jump: int) -> None:
        self._stack.append(jump)

    
    def pop(self) -> int:
        return self._stack.pop()

    
    def top(self) -> int:
        return self._stack[-1]

    
    def __str__(self) -> str:
        s = 'JumpStack(stack='

        for item in self._stack:
            s += f'{item}'

        s += ')'

        return s


class FunctionParameterCountStack():
    def __init__(self) -> None:
        self._stack : list[tuple[str, int]] = list()

    
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

    
    def __str__(self) -> str:
        s = 'FunctionParameterStack(stack='

        for item in self._stack:
            s += f'{item}'

        s += ')'

        return s