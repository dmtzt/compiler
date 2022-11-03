import unittest
from compiler.lexer import Lexer

class TestLexerReserved(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lexer = Lexer()

        cls.reserved = {
            "alie": "ELSE",
            "au": "OR",
            "bul": "BOOL",
            "dum": "WHILE",
            "ekde": "FROM",
            "ent": "INT",
            "funkcio": "FUNCTION",
            "komenco": "START",
            "kar": "CHAR",
            "kaj": "AND",
            "legi": "READ",
            "lokaj": "LOCAL",
            "malplena": "VOID",
            "malvera": "FALSE",
            "ne": "NOT",
            "reel": "REAL",
            "redonu": "RETURN",
            "skribi": "PRINT",
            "se": "IF",
            "tutmondaj": "GLOBAL",
            "variabloj": "VARIABLES", 
            "vera": "TRUE",
        }

    def get_reserved_types(self):
        return list(self.reserved.values())

    
    def get_reserved_values(self):
        return list(self.reserved.keys())

    
    def join_list_as_string(self, l):
        return ' '.join(l)


    def test_lexer_reserved_1(self):
        """Lexer parses all reserved keywords"""
        reserved_values = self.get_reserved_values()
        reserved_values_string = self.join_list_as_string(reserved_values)

        reserved_types = self.get_reserved_types()

        tokens = self.lexer.scan_multiple_tokens(reserved_values_string)
        tokens_types = self.lexer.get_tokens_types(tokens)

        self.assertCountEqual(reserved_types, tokens_types)


if __name__ == '__main__':
    unittest.main()