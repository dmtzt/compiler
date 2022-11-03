from ply import yacc
from .lexer import Lexer

class Parser(object):
    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)


    def parse(self, input):
        return self.parser.parse(input)


    def p_start_1(self, p):
        '''start : global_variables_declaration functions_definition entry_point_definition'''

    
    def p_start_2(self, p):
        '''start : global_variables_declaration entry_point_definition'''

    
    def p_start_3(self, p):
        '''start : functions_definition entry_point_definition'''

    
    def p_start_4(self, p):
        '''start : entry_point_definition'''


    def p_global_variables_declaration(self, p):
        '''global_variables_declaration : GLOBAL variables_declaration'''

    
    def p_functions_definition_1(self, p):
        '''functions_definition : functions_definition single_function_definition'''
    

    def p_functions_definition_2(self, p):
        '''functions_definition : single_function_definition'''

    
    def p_single_function_definition_primitive_type_1(self, p):
        '''single_function_definition : FUNCTION type ID LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


    def p_single_function_definition_primitive_type_2(self, p):
        '''single_function_definition : FUNCTION type ID LPAREN function_definition_params RPAREN instruction_block'''

    
    def p_single_function_definition_primitive_type_3(self, p):
        '''single_function_definition : FUNCTION type ID LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_single_function_definition_primitive_type_4(self, p):
        '''single_function_definition : FUNCTION type ID LPAREN RPAREN instruction_block'''


    def p_single_function_definition_void_type_1(self, p):
        '''single_function_definition : FUNCTION VOID ID LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


    def p_single_function_definition_void_type_2(self, p):
        '''single_function_definition : FUNCTION VOID ID LPAREN function_definition_params RPAREN instruction_block'''

    
    def p_single_function_definition_void_type_3(self, p):
        '''single_function_definition : FUNCTION VOID ID LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_single_function_definition_void_type_4(self, p):
        '''single_function_definition : FUNCTION VOID ID LPAREN RPAREN instruction_block'''


    def p_function_definition_params_1(self, p):
        '''function_definition_params : function_definition_params COMMA single_function_definition_param'''

    
    def p_function_definition_params_2(self, p):
        '''function_definition_params : single_function_definition_param'''


    def p_single_function_definition_param(self, p):
        '''single_function_definition_param : type ID'''

    
    def p_entry_point_definition_1(self, p):
        '''entry_point_definition : START LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_entry_point_definition_2(self, p):
        '''entry_point_definition : START LPAREN RPAREN instruction_block'''


    def p_local_variables_declaration(self, p):
        '''local_variables_declaration : LOCAL variables_declaration'''

    
    def p_variables_declaration(self, p):
        '''variables_declaration : VARIABLES COLON distinct_type_variables_declaration'''

    
    def p_distinct_type_variables_declaration_1(self, p):
        '''distinct_type_variables_declaration : distinct_type_variables_declaration shared_type_variables_declaration'''


    def p_distinct_type_variables_declaration_2(self, p):
        '''distinct_type_variables_declaration : shared_type_variables_declaration'''


    def p_shared_type_variables_declaration(self, p):
        '''shared_type_variables_declaration : type shared_type_variables_declaration_list SEMI'''

    
    def p_shared_type_variables_declaration_list_1(self, p):
        '''shared_type_variables_declaration_list : shared_type_variables_declaration_list COMMA single_variable_declaration'''


    def p_shared_type_variables_declaration_list_2(self, p):
        '''shared_type_variables_declaration_list : single_variable_declaration'''


    def p_single_variable_declaration_1(self, p):
        '''single_variable_declaration : ID dim_definition dim_definition'''

    
    def p_single_variable_declaration_2(self, p):
        '''single_variable_declaration : ID dim_definition'''

    
    def p_single_variable_declaration_3(self, p):
        '''single_variable_declaration : ID'''
                           

    def p_dim_definition(self, p):
        '''dim_definition : LBRACKET CONST_INT RBRACKET'''

    
    def p_instruction_block_1(self, p):
        '''instruction_block : LBRACE statements RBRACE'''

    
    def p_instruction_block_2(self, p):
        '''instruction_block : LBRACE RBRACE'''

    
    def p_statements_1(self, p):
        '''statements : statements single_statement'''

    
    def p_statements_1(self, p):
        '''statements : single_statement'''


    def p_single_statement_1(self, p):
        '''single_statement : assignment'''


    def p_single_statement_2(self, p):
        '''single_statement : function_call'''


    def p_single_statement_3(self, p):
        '''single_statement : read'''


    def p_single_statement_4(self, p):
        '''single_statement : print'''


    def p_single_statement_5(self, p):
        '''single_statement : conditional'''


    def p_single_statement_6(self, p):
        '''single_statement : loop'''


    def p_single_statement_7(self, p):
        '''single_statement : return'''

    
    def p_assignment_1(self, p):
        '''assignment : variable_access ASGMT expr SEMI'''


    def p_assignment_2(self, p):
        '''assignment : variable_access ASGMT read'''


    def p_variable_access_1(self, p):
        '''variable_access : ID dim_access dim_access'''

    
    def p_variable_access_2(self, p):
        '''variable_access : ID dim_access'''

    
    def p_variable_access_3(self, p):
        '''variable_access : ID'''


    def p_dim_access(self, p):
        '''dim_access : LBRACKET expr RBRACKET'''

    
    def p_function_call_1(self, p):
        '''function_call : ID LPAREN function_call_params RPAREN SEMI'''

    
    def p_function_call_2(self, p):
        '''function_call : ID LPAREN RPAREN SEMI'''

    
    def p_function_call_params_1(self, p):
        '''function_call_params : function_call_params COMMA single_function_call_param'''


    def p_function_call_params_2(self, p):
        '''function_call_params : single_function_call_param'''


    def p_single_function_call_param(self, p):
        '''single_function_call_param : expr'''

     
    def p_read(self, p):
        '''read : READ LPAREN RPAREN SEMI'''

    
    def p_print_1(self, p):
        '''print : PRINT LPAREN print_params RPAREN SEMI'''

    
    def p_print_2(self, p):
        '''print : PRINT LPAREN RPAREN SEMI'''


    def p_print_params_1(self, p):
        '''print_params : print_params COMMA single_print_param'''

    
    def p_print_params_2(self, p):
        '''print_params : single_print_param'''

    
    def p_single_print_param_1(self, p):
        '''single_print_param : expr'''

    
    def p_single_print_param_2(self, p):
        '''single_print_param : CONST_STRING'''

    
    def p_conditional_1(self, p):
        '''conditional : IF LPAREN expr RPAREN instruction_block ELSE instruction_block'''

    
    def p_conditional_2(self, p):
        '''conditional : IF LPAREN expr RPAREN instruction_block'''

    
    def p_loop_1(self, p):
        '''loop : while'''

    
    def p_loop_2(self, p):
        '''loop : for'''

    
    def p_while(self, p):
        '''while : WHILE LPAREN expr RPAREN instruction_block'''

    
    def p_for_1(self, p):
        '''for : FROM LPAREN ID ASGMT CONST_INT COLON CONST_INT COLON CONST_INT RPAREN instruction_block'''

    
    def p_for_2(self, p):
        '''for : FROM LPAREN ID ASGMT CONST_INT COLON CONST_INT RPAREN instruction_block'''

    
    def p_return_1(self, p):
        '''return : RETURN expr SEMI'''


    def p_return_2(self, p):
        '''return : RETURN SEMI'''

    
    def p_expr_1(self, p):
        '''expr : expr OR and_expr'''


    def p_expr_2(self, p):
        '''expr : and_expr'''


    def p_and_expr_1(self, p):
        '''and_expr : equality_expr AND equality_expr'''


    def p_and_expr_2(self, p):
        '''and_expr : equality_expr'''


    def p_equality_expr_1(self, p):
        '''equality_expr : relational_expr EQUAL relational_expr'''


    def p_equality_expr_2(self, p):
        '''equality_expr : relational_expr NEQUAL relational_expr'''


    def p_equality_expr_3(self, p):
        '''equality_expr : relational_expr'''


    def p_relational_expr_1(self, p):
        '''relational_expr : additive_expr LTHAN_EQUAL additive_expr'''

    
    def p_relational_expr_2(self, p):
        '''relational_expr : additive_expr LTHAN additive_expr'''

    
    def p_relational_expr_3(self, p):
        '''relational_expr : additive_expr GTHAN_EQUAL additive_expr'''

    
    def p_relational_expr_4(self, p):
        '''relational_expr : additive_expr GTHAN additive_expr'''

    
    def p_relational_expr_5(self, p):
        '''relational_expr : additive_expr'''


    def p_additive_expr_1(self, p):
        '''additive_expr : multiplicative_expr PLUS multiplicative_expr'''

    
    def p_additive_expr_2(self, p):
        '''additive_expr : multiplicative_expr MINUS multiplicative_expr'''

    
    def p_additive_expr_3(self, p):
        '''additive_expr : multiplicative_expr'''


    def p_multiplicative_expr_1(self, p):
        '''multiplicative_expr : unary_expr TIMES unary_expr'''

    
    def p_multiplicative_expr_2(self, p):
        '''multiplicative_expr : unary_expr DIVIDE unary_expr'''


    def p_multiplicative_expr_3(self, p):
        '''multiplicative_expr : unary_expr MODULO unary_expr'''


    def p_multiplicative_expr_4(self, p):
        '''multiplicative_expr : unary_expr'''

    
    def p_unary_expr_1(self, p):
        '''unary_expr : MINUS postfix_expr'''

    
    def p_unary_expr_2(self, p):
        '''unary_expr : PLUS postfix_expr'''

    
    def p_unary_expr_3(self, p):
        '''unary_expr : NOT postfix_expr'''

    
    def p_unary_expr_4(self, p):
        '''unary_expr : postfix_expr'''

    
    def p_postfix_expr_1(self, p):
        '''postfix_expr : LPAREN expr RPAREN'''

    
    def p_postfix_expr_2(self, p):
        '''postfix_expr : variable_access'''

    
    def p_postfix_expr_3(self, p):
        '''postfix_expr : function_call'''

    
    def p_postfix_expr_4(self, p):
        '''postfix_expr : constant'''


    def p_constant_1(self, p):
        '''constant : CONST_INT'''

                
    def p_constant_2(self, p):
        '''constant : CONST_REAL'''


    def p_constant_3(self, p):
        '''constant : CONST_CHAR'''

    
    def p_constant_4(self, p):
        '''constant : constant_bool'''

    
    def p_constant_bool_1(self, p):
        '''constant_bool : TRUE'''

    
    def p_constant_bool_2(self, p):
        '''constant_bool : FALSE'''

    
    def p_type_1(self, p):
        '''type : INT'''


    def p_type_2(self, p):
        '''type : REAL'''


    def p_type_3(self, p):
        '''type : CHAR'''


    def p_type_4(self, p):
        '''type : BOOL'''


    def p_error(self, p):
        if p:
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
            raise SyntaxError('Syntax error at token', p)
        else:
          raise SyntaxError('Error at EOF')


class SyntaxError(Exception):
    pass