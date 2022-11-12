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
        print(self.__str__())
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