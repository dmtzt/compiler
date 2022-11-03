import unittest
from compiler.lexer import Lexer

class TestLexerReserved(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexer = Lexer()

            
    def test_lexer_operators_1(self):
        """Lexer parses and splits an integer variable"""
        test_value = "ent i;"
        test_types = ["INT", "ID", "SEMI"]

        token = self.lexer.scan_multiple_tokens(test_value)
        token_types = self.lexer.get_tokens_types(token)

        print(token)

        self.assertCountEqual(test_types, token_types)

    
    def test_lexer_operators_2(self):
        """Lexer parses and splits an integer vector (1D)"""
        test_value = "ent i[10];"
        test_types = ["INT", "ID", "LBRACKET", "CONST_INT", "RBRACKET", "SEMI"]

        token = self.lexer.scan_multiple_tokens(test_value)
        token_types = self.lexer.get_tokens_types(token)

        print(token)

        self.assertCountEqual(test_types, token_types)


if __name__ == '__main__':
    unittest.main()