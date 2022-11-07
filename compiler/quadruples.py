from typing import Union

from abc import ABC, abstractmethod
from .variables import Variable
from .variables import Operator

class Quadruple():
    def __init__(self, operator, operand_1, operand_2, target):
        self._operator = operator
        self._operand_1 = operand_1
        self._operand_2 = operand_2
        self._target = target


    def set_operator(self, operator: Operator) -> None:
        self._operator = operator


    def set_operand_1(self, operand_1: Variable) -> None:
        self._operand_1 = operand_1

    
    def set_operand_2(self, operand_2: Variable) -> None:
        self._operand_2 = operand_2

    
    def set_target(self, target: Variable) -> None:
        self._target = target


    def __str__(self) -> str:
        return f'Quadruple({self._operator}, { self._operand_1.__str__()}, {self._operand_2.__str__()}, {self._target.__str__()})'


class QuadrupleList():
    def __init__(self) -> None:
        self._list = list()

    
    def insert_quadruple(self, quadruple: Quadruple) -> None:
        self._list.append(quadruple)

    
    def __str__(self) -> str:
        s = 'QuadrupleList(\n'

        for item in self._list:
            s += f'\t{item.__str__()}\n'
        
        s += ')'

        return s


# class Builder(ABC):
#     @property
#     @abstractmethod
#     def build(self) -> Quadruple:
#         pass


#     @abstractmethod
#     def set_operator(self, operand_2: Variable) -> None:
#         pass


#     @abstractmethod
#     def set_operand_1(self, operand_1: Variable) -> None:
#         pass


#     @abstractmethod
#     def set_operand_2(self, operand_2: Variable) -> None:
#         pass


#     @abstractmethod
#     def set_target(self, operand_2: Variable) -> None:
#         pass

    
# class QuadruplenBuilder(Builder):
#     def __init__(self) -> None:
#         self.reset()

    
#     def reset(self) -> None:
#         self.__quadruple = Quadruple()


#     def build(self) -> Quadruple:
#         product = self.__quadruple
#         self.reset()
#         return product


#     def set_operator(self, operator: Operator) -> None:
#         self.__quadruple.set_operator(operator)


#     def set_operand_1(self, operand_1: Variable) -> None:
#         self.__quadruple.set_operand_1(operand_1)

    
#     def set_operand_2(self, operand_2: Variable) -> None:
#         self.__quadruple.set_operand_2(operand_2)

    
#     def set_target(self, target: Variable) -> None:
#         self.__quadruple.set_target(target)
