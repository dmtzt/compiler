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
        '''start : global_variables_declaration functions_definition entry_point_definition'''


    def p_global_variables_declaration(self, p):
        '''global_variables_declaration : GLOBAL variables_declaration
                                        | empty'''

    
    def p_functions_definition(self, p):
        '''functions_definition : functions_definition single_function_definition
                                | empty'''

    
    def p_single_function_definition(self, p):
        '''single_function_definition : FUNCTION type ID LPAREN function_definition_params RPAREN local_variables_declaration instruction_block
                                      | FUNCTION VOID ID LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


    def p_function_definition_params(self, p):
        '''function_definition_params : function_definition_params COMMA single_function_definition_param
                                      | single_function_definition_param
                                      | empty'''


    def p_single_function_definition_param(self, p):
        '''single_function_definition_param : type ID'''

    
    def p_entry_point_definition(self, p):
        '''entry_point_definition : START LPAREN RPAREN local_variables_declaration instruction_block'''


    def p_local_variables_declaration(self, p):
        '''local_variables_declaration : LOCAL variables_declaration
                                       | empty'''

    
    def p_variables_declaration(self, p):
        '''variables_declaration : VARIABLES COLON distinct_type_variables_declaration'''

    
    def p_distinct_type_variables_declaration(self, p):
        '''distinct_type_variables_declaration : distinct_type_variables_declaration shared_type_variables_declaration
                                               | shared_type_variables_declaration'''


    def p_shared_type_variables_declaration(self, p):
        '''shared_type_variables_declaration : type shared_type_variables_declaration_list SEMI'''

    
    def p_shared_type_variables_declaration_list(self, p):
        '''shared_type_variables_declaration_list : shared_type_variables_declaration_list COMMA single_variable_declaration
                                                  | single_variable_declaration'''


    def p_single_variable_declaration(self, p):
        '''single_variable_declaration : ID dims_definition'''


    def p_dims_definition(self, p):
        '''dims_definition : dims_definition single_dim_definition
                           | empty'''
                           

    def p_single_dim_definition(self, p):
        '''single_dim_definition : LBRACKET CONST_INT RBRACKET'''

    
    def p_instruction_block(self, p):
        '''instruction_block : LBRACE statements RBRACE'''

    
    def p_statements(self, p):
        '''statements : statements single_statement
                      | empty'''

    def p_single_statement(self, p):
        '''single_statement : assignment
                            | function_call
                            | read
                            | print
                            | conditional
                            | loop
                            | return'''

    
    def p_assignment(self, p):
        '''assignment : variable_access ASGMT expression SEMI
                      | variable_access ASGMT read'''


    def p_variable_access(self, p):
        '''variable_access : ID dims_access'''

    
    def p_dims_access(self, p):
        '''dims_access : dims_access single_dim_access
                       | empty'''

    
    def p_dim_access(self, p):
        '''single_dim_access : LBRACKET expression RBRACKET'''

    
    def p_function_call(self, p):
        '''function_call : ID LPAREN function_call_params RPAREN SEMI'''

    
    def p_function_call_params(self, p):
        '''function_call_params : function_call_params COMMA single_function_call_param
                                | single_function_call_param
                                | empty'''


    def p_single_function_call_param(self, p):
        '''single_function_call_param : expression'''

     
    def p_read(self, p):
        '''read : READ LPAREN RPAREN SEMI'''

    
    def p_print(self, p):
        '''print : PRINT LPAREN RPAREN SEMI'''

    
    def p_conditional(self, p):
        '''conditional : empty'''

    
    def p_loop(self, p):
        '''loop : empty'''

    
    def p_return(self, p):
        '''return : empty'''

    
    def p_expression(self, p):
        '''expression : and_expression'''


    def p_and_expression(self, p):
        '''and_expression : relational_expression'''


    def p_relational_expression(self, p):
        '''relational_expression : additive_expression'''


    def p_additive_expression(self, p):
        '''additive_expression : multiplicative_expression'''


    def p_multiplicative_expression(self, p):
        '''multiplicative_expression : unary_expression'''

    
    def p_unary_expression(self, p):
        '''unary_expression : posfix_expression'''

    
    def p_posfix_expression(self, p):
        '''posfix_expression : constant'''


    def p_constant(self, p):
        '''constant : CONST_INT
                    | CONST_REAL
                    | CONST_CHAR
                    | constant_bool'''

    
    def p_constant_bool(self, p):
        '''constant_bool : TRUE
                         | FALSE'''

    
    def p_type(self, p):
        '''type : INT
                | REAL
                | CHAR
                | BOOL'''
        

    def p_empty(self, p):
        'empty :'
        pass


    def p_error(self, p):
        if p:
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
            raise SyntaxError('Syntax error at token', p)
        else:
          raise SyntaxError('Error at EOF')


class SyntaxError(Exception):
    pass