from ply import yacc
from .lexer import Lexer

class Parser(object):
    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)


    def parse(self, input):
        return self.parser.parse(input)


    def p_start(self, p):
        '''start : global_variables_declaration function_definition entry_point_definition'''


    def p_global_variables_declaration(self, p):
        '''global_variables_declaration : GLOBAL variables_declaration
                                        | empty'''

    
    def p_function_definition(self, p):
        '''function_definition : function_definition function_definition
                               | FUNCTION type ID LPAREN RPAREN local_variables_declaration instruction_block
                               | FUNCTION VOID ID LPAREN RPAREN local_variables_declaration instruction_block
                               | FUNCTION type ID LPAREN function_definition_param RPAREN local_variables_declaration instruction_block
                               | FUNCTION VOID ID LPAREN function_definition_param RPAREN local_variables_declaration instruction_block
                               | empty'''


    def p_function_definition_param(self, p):
        '''function_definition_param : function_definition_param COMMA function_definition_param
                                     | type ID dims_definition'''


    def p_dims_definition(self, p):
        '''dims_definition : dims_definition dims_definition
                           | LBRACKET CONST_INT RBRACKET
                           | empty'''


    def p_entry_point_definition(self, p):
        '''entry_point_definition : START LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_local_variables_declaration(self, p):
        '''local_variables_declaration : LOCAL variables_declaration
                                       | empty'''

    
    def p_instruction_block(self, p):
        '''instruction_block : LBRACE statement RBRACE'''

    
    def p_variables_declaration(self, p):
        '''variables_declaration : VARIABLES COLON variable_declaration'''

    
    def p_variables_declaration_list(self, p):
        '''variable_declaration : variable_declaration variable_declaration
                                | type ID SEMI'''

    def p_type(self, p):
        '''type : INT
                | REAL
                | CHAR
                | BOOL'''

    
    def p_statement(self, p):
        '''statement : empty'''


    def p_empty(self, p):
        'empty :'
        pass


    def p_error(self, p):
        if p:
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
            raise SyntaxError(f'Syntax error at token', p)
        else:
          raise SyntaxError('Error at EOF')


class SyntaxError(Exception):
    pass