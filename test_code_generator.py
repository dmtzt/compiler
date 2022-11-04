import unittest
from pathlib import Path

from compiler.parser import ParserCodeGenerator

class TestCodeGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = ParserCodeGenerator()
        cls.dir_files = Path('./test_files/code_generator')


    def read_test_file(self, test_name: str) -> str:
        fname = f'{test_name}.txt'
        fpath = self.dir_files / fname

        with open(fpath) as f:
            return '\n'.join(line.rstrip() for line in f)


    @unittest.skip
    def test_code_generator_1(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_1'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)


    @unittest.skip
    def test_code_generator_2(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_2'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_3(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_3'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_4(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_4'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_6(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_6'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_7(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_7'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    
    def test_code_generator_8(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_8'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
