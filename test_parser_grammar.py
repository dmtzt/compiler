import unittest
from pathlib import Path

from compiler.lexer import Lexer
from compiler.parser import Parser

class TestLexerGrammar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexer = Lexer()
        cls.parser = Parser()
        cls.dir_files = Path('./test_files')


    def read_test_file(self, test_name: str) -> str:
        fname = f'{test_name}.txt'
        fpath = self.dir_files / fname

        with open(fpath) as f:
            return '\n'.join(line.rstrip() for line in f)


    def test_lexer_grammar_1(self):
        """Parser accepts (1):
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_1'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_2(self):
        """Parser accepts (2):
            - Global integer variable declaration
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_2'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_3(self):
        """Parser accepts (3):
            - Global integer variable declaration
            - Void function without parameters definition
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_3'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_4(self):
        """Parser accepts (5):
            - Global integer variable declaration
            - Global real variable declaration
            - Global char variable declaration
            - Global bool variable declaration
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_4'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_5(self):
        """Parser accepts (2):
            - Void function without parameters definition
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_5'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_6(self):
        """Parser accepts (2):
            - Primitive type function without parameters definition
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_6'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_7(self):
        """Parser accepts (5):
            - Integer type function without parameters declaration
            - Real type function without parameters declaration
            - Char type function without parameters declaration
            - Bool type function without parameters declaration
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_7'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_8(self):
        """Parser accepts (2):
            - Void function with multiple arguments definition
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_8'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)


    def test_lexer_grammar_9(self):
        """Parser accepts (1):
            - Empty entry point with an integer local variable definition"""
        test_name = 'test_lexer_grammar_9'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_10(self):
        """Parser accepts (2): 
            - Void function with an integer local variable definition
            - Empty entry point definition"""
        test_name = 'test_lexer_grammar_10'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_11(self):
        """Parser accepts (1): 
            - Empty entry point definition with a local integer vector (1D) variable"""
        test_name = 'test_lexer_grammar_10'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_12(self):
        """Parser accepts (1): 
            - Empty entry point definition with a local integer matrix (2D) variable"""
        test_name = 'test_lexer_grammar_12'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
