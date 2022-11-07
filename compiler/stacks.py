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