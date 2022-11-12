import unittest
from pathlib import Path

from compiler.parser import ParserCodeGenerator
from compiler.parser import TypeMismatchError

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

    @unittest.skip
    def test_code_generator_8(self):
        """Creates function directory with global scope, main function, and sum function"""
        test_name = 'test_code_generator_8'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_9(self):
        """Raises a TypeMismatchException when trying to sum an integer variable with a boolean variable"""
        with self.assertRaises(TypeMismatchError):
            test_name = 'test_code_generator_10'
            text = self.read_test_file(test_name)
            self.parser.parse(text)


    @unittest.skip
    def test_code_generator_10(self):
        """Generates an addition quadruple between 2 integer variables"""
        test_name = 'test_code_generator_9'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)        

    
    @unittest.skip
    def test_code_generator_11(self):
        """Generates a subtraction quadruple between 2 integer variables"""
        test_name = 'test_code_generator_11'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)


    @unittest.skip
    def test_code_generator_12(self):
        """Generates a product quadruple between 2 integer variables"""
        test_name = 'test_code_generator_12'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_13(self):
        """Generates a division quadruple between 2 integer variables"""
        test_name = 'test_code_generator_13'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_14(self):
        """Generates product and addition quadruples in hierarchical order"""
        test_name = 'test_code_generator_14'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)


    @unittest.skip
    def test_code_generator_15(self):
        """Generates product, divison and subtraction quadruples in hierarchical order"""
        test_name = 'test_code_generator_15'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    
    @unittest.skip
    def test_code_generator_16(self):
        """Generates quadruples for a simple if statement"""
        test_name = 'test_code_generator_16'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    
    @unittest.skip
    def test_code_generator_17(self):
        """Generates quadruples for a simple if-else statement"""
        test_name = 'test_code_generator_17'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_18(self):
        """Generates quadruples for an assignment of a read statement"""
        test_name = 'test_code_generator_18'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_19(self):
        """Generates quadruples for an assignment of an integer constant"""
        test_name = 'test_code_generator_19'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    @unittest.skip
    def test_code_generator_20(self):
        """Generates quadruples for an assignment of an addition of two integer constants"""
        test_name = 'test_code_generator_20'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)

    
    def test_code_generator_21(self):
        """Generates quadruples for an assignment of an addition of one integer and one real constant"""
        test_name = 'test_code_generator_21'
        text = self.read_test_file(test_name)

        result = self.parser.parse(text)

        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
