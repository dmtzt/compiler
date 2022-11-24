from enum import Enum

class Operator(Enum):
    ASGMT = 0

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    MODULO = 5

    UNARY_PLUS = 6
    UNARY_MINUS = 7

    EQUAL = 8
    NEQUAL = 9
    LTHAN_EQUAL = 10
    GTHAN_EQUAL = 11
    LTHAN = 12
    GTHAN = 13

    AND = 14
    OR = 15
    NOT = 16

    READ = 17
    PRINT = 18

    STORE_CONSTANT = 19

    GOTO = 20
    GOTOF = 21
    GOTOT = 22
    GOSUB = 23

    VER = 24
    ERA = 25
    PARAM = 26
    RETURN_VALUE = 27
    RETURN_VOID = 28
    ENDFUNC = 29

    END = 30

    @classmethod
    def assignment_operator(cls):
        return cls.ASGMT


    @classmethod
    def arithmetic_operators(cls):
        return cls.PLUS, cls.MINUS, cls.TIMES, cls.DIVIDE, cls.MODULO


    @classmethod
    def unary_arithmetic_operators(cls):
        return cls.UNARY_PLUS, cls.UNARY_MINUS


    @classmethod
    def relational_operators(cls):
        return cls.EQUAL, cls.NEQUAL, cls.LTHAN_EQUAL, cls.GTHAN_EQUAL, cls.LTHAN, cls.GTHAN
