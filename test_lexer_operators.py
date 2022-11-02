import unittest
from compiler.lexer import Lexer

class TestLexerReserved(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexer = Lexer()

        cls.operators = {
            "+": "PLUS",
            "-": "MINUS",
            "*": "TIMES",
            "/": "DIVIDE",
            "%": "MODULO",
            "==": "EQUAL",
            "!=": "NEQUAL",
            "<=": "LTHAN_EQUAL",
            ">=": "GTHAN_EQUAL",
            "<": "LTHAN",
            ">": "GTHAN",
            "=": "ASGMT",
            "(": "LPAREN",
            ")": "RPAREN",
            "[": "LBRACKET",
            "]": "RBRACKET",
            "{": "LBRACE",
            "}": "RBRACE",
            ":": "COLON",
            ";": "SEMI",
            ",": "COMMA",
        }

    def get_operators_types(self):
        return list(self.operators.values())

    
    def get_operators_values(self):
        return list(self.operators.keys())

    
    def join_list_as_string(self, l):
        return ' '.join(l)

    
    def test_lexer_operators_1(self):
        """Lexer parses all reserved keywords"""
        operators_values = self.get_operators_values()
        operators_values_string = self.join_list_as_string(operators_values)

        operators_types = self.get_operators_types()

        tokens = self.lexer.scan_multiple_tokens(operators_values_string)
        tokens_types = self.lexer.get_tokens_types(tokens)

        self.assertCountEqual(operators_types, tokens_types)


if __name__ == '__main__':
    unittest.main()