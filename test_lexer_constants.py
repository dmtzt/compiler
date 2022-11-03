import unittest
from compiler.lexer import Lexer

class TestLexerConstants(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexer = Lexer()

    def test_lexer_constants_1(self):
        """Lexer parses a CONST_INT"""
        test_value = "1"
        test_type = "CONST_INT"

        token = self.lexer.scan_single_token(test_value)
        token_type = self.lexer.get_token_type(token)

        print(token)

        self.assertEqual(test_type, token_type)


    def test_lexer_constants_2(self):
        """Lexer parses a CONST_REAL"""
        test_value = "2.3"
        test_type = "CONST_REAL"

        token = self.lexer.scan_single_token(test_value)
        token_type = self.lexer.get_token_type(token)

        print(token)

        self.assertEqual(test_type, token_type)

    
    def test_lexer_constants_3(self):
        """Lexer parses a CONST_INT, followed by a CONST_REAL"""
        test_value = "1 2.3"
        test_types = ["CONST_INT", "CONST_REAL"]

        tokens = self.lexer.scan_multiple_tokens(test_value)
        token_types = self.lexer.get_tokens_types(tokens)

        print(tokens)

        self.assertCountEqual(test_types, token_types)

    
    def test_lexer_constants_4(self):
        """Lexer parses a CONST_REAL, followed by a CONST_INT"""
        test_value = "2.3 1"
        test_types = ["CONST_REAL", "CONST_INT"]

        tokens = self.lexer.scan_multiple_tokens(test_value)
        token_types = self.lexer.get_tokens_types(tokens)

        print(tokens)

        self.assertCountEqual(test_types, token_types)

    
    def test_lexer_constants_5(self):
        """Lexer parses a CONST_INT surrounded by whitespace"""
        test_value = " 10 "
        test_type = "CONST_INT"

        token = self.lexer.scan_single_token(test_value)
        token_type = self.lexer.get_token_type(token)

        print(token)

        self.assertEqual(test_type, token_type)

    
    def test_lexer_constants_6(self):
        """Lexer parses a CONST_REAL surrounded by whitespace"""
        test_value = " 20.5 "
        test_type = "CONST_REAL"

        token = self.lexer.scan_single_token(test_value)
        token_type = self.lexer.get_token_type(token)

        print(token)

        self.assertEqual(test_type, token_type)


    def test_lexer_constants_7(self):
        """Lexer parses and splits a MINUS and a CONST_INT"""
        test_value = "-1"
        test_types = ["MINUS", "CONST_INT"]

        token = self.lexer.scan_multiple_tokens(test_value)
        token_types = self.lexer.get_tokens_types(token)

        print(token)

        self.assertCountEqual(test_types, token_types)


    def test_lexer_constants_7(self):
        """Lexer parses and splits a MINUS and a CONST_REAL"""
        test_value = "-9.8"
        test_types = ["MINUS", "CONST_REAL"]

        token = self.lexer.scan_multiple_tokens(test_value)
        token_types = self.lexer.get_tokens_types(token)

        print(token)

        self.assertCountEqual(test_types, token_types)


if __name__ == '__main__':
    unittest.main()
