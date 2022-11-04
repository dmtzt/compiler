import unittest
from pathlib import Path

from compiler.parser import Parser

class TestLexerGrammar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser()
        cls.dir_files = Path('./test_files/lexer')


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


    def test_lexer_grammar_13(self):
        """Parser accepts (1): 
            - Empty entry point definition with local integer variable and a vector (1D) in a single line"""
        test_name = 'test_lexer_grammar_13'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_14(self):
        """Parser accepts (1): 
            - Empty entry point definition with local integer variable, a vector (1D), and a matrix (2D) in a single line"""
        test_name = 'test_lexer_grammar_14'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_15(self):
        """Parser accepts (1): 
            - Empty entry point definition with a  local matrix (2D), a vector (1D), and integer variable in a single line"""
        test_name = 'test_lexer_grammar_15'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)


    def test_lexer_grammar_16(self):
        """Parser accepts (4): 
            - Empty entry point definition with:
                - Local integer variable, a vector (1D), and a matrix (2D) in a single line
                - Local real variable, a vector (1D), and a matrix (2D) in a single line
                - Local char variable, a vector (1D), and a matrix (2D) in a single line
                - Local bool variable, a vector (1D), and a matrix (2D) in a single line"""
        test_name = 'test_lexer_grammar_16'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_17(self):
        """Parser accepts (1): 
            - Entry point definition with an assignment statement of an integer to a variable"""
        test_name = 'test_lexer_grammar_17'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_18(self):
        """Parser accepts (1): 
            - Entry point definition with an assignment statement of an integer to a vector index defined by a constant"""
        test_name = 'test_lexer_grammar_18'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_19(self):
        """Parser accepts (1): 
            - Entry point definition with an assignment statement of an integer to a MATRIX index defined by constants"""
        test_name = 'test_lexer_grammar_19'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_20(self):
        """Parser accepts (1): 
            - Entry point definition with an assignment statement of the read function to a MATRIX index defined by constants"""
        test_name = 'test_lexer_grammar_20'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)


    def test_lexer_grammar_21(self):
        """Parser accepts (1): 
            - Entry point definition with a function call with no parameters"""
        test_name = 'test_lexer_grammar_21'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_22(self):
        """Parser accepts (1): 
            - Entry point definition with a function call with 1 integer"""
        test_name = 'test_lexer_grammar_22'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    def test_lexer_grammar_23(self):
        """Parser accepts (1): 
            - Entry point definition with a function call with 1 integer, 1 real, 1 char, 1 bool"""
        test_name = 'test_lexer_grammar_23'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)

    
    def test_lexer_grammar_24(self):
        test_name = 'test_lexer_grammar_24'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)
        
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
