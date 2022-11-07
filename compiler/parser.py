from collections import defaultdict

from ply import yacc

from .lexer import Lexer
from .functions import FunctionBuilder
from .functions import FunctionDirector
from .functions import FunctionDirectory
from .quadruples import Quadruple
from .quadruples import QuadrupleList
from .stacks import OperandStack
from .stacks import OperatorStack
from .variables import SemanticTable
from .variables import Type
from .variables import Variable
from .variables import VariableBuilder
from .variables import Operator


# class Parser(object):
#     tokens = Lexer.tokens

#     def __init__(self) -> None:
#         self.lexer = Lexer()
#         self.parser = yacc.yacc(module=self)


#     def parse(self, input):
#         return self.parser.parse(input)

    
#     def p_program(self, p):
#         '''program : init start'''


#     def p_init(self, p):
#         '''init :'''


#     def p_start_1(self, p):
#         '''start : global_variables_declaration functions_definition entry_point_definition'''

    
#     def p_start_2(self, p):
#         '''start : global_variables_declaration entry_point_definition'''

    
#     def p_start_3(self, p):
#         '''start : functions_definition entry_point_definition'''
        

#     def p_start_4(self, p):
#         '''start : entry_point_definition'''


#     def p_global_variables_declaration(self, p):
#         '''global_variables_declaration : GLOBAL parsed_global_scope variables_declaration'''

    
#     def p_parsed_global_scope(self, p):
#         '''parsed_global_scope :'''

    
#     def p_functions_definition_1(self, p):
#         '''functions_definition : functions_definition single_function_definition'''
    

#     def p_functions_definition_2(self, p):
#         '''functions_definition : single_function_definition'''

    
#     def p_single_function_definition_primitive_type_1(self, p):
#         '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


#     def p_single_function_definition_primitive_type_2(self, p):
#         '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_block'''

    
#     def p_single_function_definition_primitive_type_3(self, p):
#         '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_block'''

    
#     def p_single_function_definition_primitive_type_4(self, p):
#         '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN instruction_block'''


#     def p_single_function_definition_void_type_1(self, p):
#         '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


#     def p_single_function_definition_void_type_2(self, p):
#         '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_block'''


#     def p_single_function_definition_void_type_3(self, p):
#         '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_block'''

    
#     def p_single_function_definition_void_type_4(self, p):
#         '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN instruction_block'''


#     def p_parsed_function_id(self, p):
#         '''parsed_function_id :'''


#     def p_parsed_function_return_type(self, p):
#         '''parsed_function_return_type :'''

    
#     def p_parsed_function_void_return_type(self, p):
#         '''parsed_function_void_return_type  :'''


#     def p_function_definition_params_1(self, p):
#         '''function_definition_params : function_definition_params COMMA single_function_definition_param'''

    
#     def p_function_definition_params_2(self, p):
#         '''function_definition_params : single_function_definition_param'''


#     def p_single_function_definition_param(self, p):
#         '''single_function_definition_param : type ID'''

    
#     def p_entry_point_definition_1(self, p):
#         '''entry_point_definition : START parsed_main_id LPAREN RPAREN local_variables_declaration instruction_block'''

    
#     def p_entry_point_definition_2(self, p):
#         '''entry_point_definition : START parsed_main_id LPAREN RPAREN instruction_block'''

 
#     def p_parsed_main_id(self, p):
#         '''parsed_main_id :'''


#     def p_local_variables_declaration(self, p):
#         '''local_variables_declaration : LOCAL variables_declaration'''

    
#     def p_variables_declaration(self, p):
#         '''variables_declaration : VARIABLES COLON distinct_type_variables_declaration'''

    
#     def p_distinct_type_variables_declaration_1(self, p):
#         '''distinct_type_variables_declaration : distinct_type_variables_declaration shared_type_variables_declaration'''


#     def p_distinct_type_variables_declaration_2(self, p):
#         '''distinct_type_variables_declaration : shared_type_variables_declaration'''


#     def p_shared_type_variables_declaration(self, p):
#         '''shared_type_variables_declaration : type parsed_type shared_type_variables_declaration_list SEMI'''

    
#     def p_parsed_type(self, p):
#         '''parsed_type :'''

    
#     def p_shared_type_variables_declaration_list_1(self, p):
#         '''shared_type_variables_declaration_list : shared_type_variables_declaration_list COMMA single_variable_declaration'''


#     def p_shared_type_variables_declaration_list_2(self, p):
#         '''shared_type_variables_declaration_list : single_variable_declaration'''


#     def p_single_variable_declaration_1(self, p):
#         '''single_variable_declaration : ID dim_definition dim_definition'''

    
#     def p_single_variable_declaration_2(self, p):
#         '''single_variable_declaration : ID dim_definition'''

    
#     def p_single_variable_declaration_3(self, p):
#         '''single_variable_declaration : ID'''


#     def p_dim_definition(self, p):
#         '''dim_definition : LBRACKET CONST_INT RBRACKET'''

    
#     def p_instruction_block_1(self, p):
#         '''instruction_block : LBRACE statements RBRACE'''

    
#     def p_instruction_block_2(self, p):
#         '''instruction_block : LBRACE RBRACE'''

    
#     def p_statements_1(self, p):
#         '''statements : statements single_statement'''

    
#     def p_statements_2(self, p):
#         '''statements : single_statement'''


#     def p_single_statement_1(self, p):
#         '''single_statement : assignment'''


#     def p_single_statement_2(self, p):
#         '''single_statement : function_call'''


#     def p_single_statement_3(self, p):
#         '''single_statement : read'''


#     def p_single_statement_4(self, p):
#         '''single_statement : print'''


#     def p_single_statement_5(self, p):
#         '''single_statement : conditional'''


#     def p_single_statement_6(self, p):
#         '''single_statement : loop'''


#     def p_single_statement_7(self, p):
#         '''single_statement : return'''

    
#     def p_assignment_1(self, p):
#         '''assignment : variable_access ASGMT expr SEMI'''


#     def p_assignment_2(self, p):
#         '''assignment : variable_access ASGMT read'''


#     def p_variable_access(self, p):
#         '''variable_access : ID parsed_id_variable_access dims_access'''

    
#     def p_parsed_id_variable_access(self, p):
#         '''parsed_id_variable_access :'''


#     def p_dims_access_1(self, p):
#         '''dims_access : single_dim_access single_dim_access'''


#     def p_dims_access_2(self, p):
#         '''dims_access : single_dim_access'''

    
#     def p_dims_access_3(self, p):
#         '''dims_access : empty'''


#     def p_single_dim_access(self, p):
#         '''single_dim_access : LBRACKET expr RBRACKET'''

    
#     def p_function_call_1(self, p):
#         '''function_call : ID LPAREN function_call_params RPAREN SEMI'''

    
#     def p_function_call_2(self, p):
#         '''function_call : ID LPAREN RPAREN SEMI'''

    
#     def p_function_call_params_1(self, p):
#         '''function_call_params : function_call_params COMMA single_function_call_param'''


#     def p_function_call_params_2(self, p):
#         '''function_call_params : single_function_call_param'''


#     def p_single_function_call_param(self, p):
#         '''single_function_call_param : expr'''

     
#     def p_read(self, p):
#         '''read : READ LPAREN RPAREN SEMI'''

    
#     def p_print_1(self, p):
#         '''print : PRINT LPAREN print_params RPAREN SEMI'''

    
#     def p_print_2(self, p):
#         '''print : PRINT LPAREN RPAREN SEMI'''


#     def p_print_params_1(self, p):
#         '''print_params : print_params COMMA single_print_param'''

    
#     def p_print_params_2(self, p):
#         '''print_params : single_print_param'''

    
#     def p_single_print_param_1(self, p):
#         '''single_print_param : expr'''

    
#     def p_single_print_param_2(self, p):
#         '''single_print_param : CONST_STRING'''

    
#     def p_conditional_1(self, p):
#         '''conditional : IF LPAREN expr RPAREN instruction_block ELSE instruction_block'''

    
#     def p_conditional_2(self, p):
#         '''conditional : IF LPAREN expr RPAREN instruction_block'''

    
#     def p_loop_1(self, p):
#         '''loop : while'''

    
#     def p_loop_2(self, p):
#         '''loop : for'''

    
#     def p_while(self, p):
#         '''while : WHILE LPAREN expr RPAREN instruction_block'''

    
#     def p_for_1(self, p):
#         '''for : FROM LPAREN ID ASGMT CONST_INT COLON CONST_INT COLON CONST_INT RPAREN instruction_block'''

    
#     def p_for_2(self, p):
#         '''for : FROM LPAREN ID ASGMT CONST_INT COLON CONST_INT RPAREN instruction_block'''

    
#     def p_return_1(self, p):
#         '''return : RETURN expr SEMI'''


#     def p_return_2(self, p):
#         '''return : RETURN SEMI'''

    
#     def p_expr_1(self, p):
#         '''expr : expr OR and_expr'''


#     def p_expr_2(self, p):
#         '''expr : and_expr'''


#     def p_and_expr_1(self, p):
#         '''and_expr : equality_expr AND equality_expr'''


#     def p_and_expr_2(self, p):
#         '''and_expr : equality_expr'''


#     def p_equality_expr_1(self, p):
#         '''equality_expr : relational_expr EQUAL relational_expr'''


#     def p_equality_expr_2(self, p):
#         '''equality_expr : relational_expr NEQUAL relational_expr'''


#     def p_equality_expr_3(self, p):
#         '''equality_expr : relational_expr'''


#     def p_relational_expr_1(self, p):
#         '''relational_expr : additive_expr LTHAN_EQUAL additive_expr'''

    
#     def p_relational_expr_2(self, p):
#         '''relational_expr : additive_expr LTHAN additive_expr'''

    
#     def p_relational_expr_3(self, p):
#         '''relational_expr : additive_expr GTHAN_EQUAL additive_expr'''

    
#     def p_relational_expr_4(self, p):
#         '''relational_expr : additive_expr GTHAN additive_expr'''

    
#     def p_relational_expr_5(self, p):
#         '''relational_expr : additive_expr'''


#     def p_additive_expr_1(self, p):
#         '''additive_expr : additive_expr PLUS parsed_plus multiplicative_expr'''
    

#     def p_parsed_plus(self, p):
#         '''parsed_plus :'''

    
#     def p_additive_expr_2(self, p):
#         '''additive_expr : additive_expr MINUS parsed_minus multiplicative_expr'''

    
#     def p_parsed_minus(self, p):
#         '''parsed_minus :'''

    
#     def p_additive_expr_3(self, p):
#         '''additive_expr : multiplicative_expr'''


#     def p_multiplicative_expr_1(self, p):
#         '''multiplicative_expr : multiplicative_expr TIMES parsed_times unary_expr'''

    
#     def p_parsed_times(self, p):
#         '''parsed_times :'''

    
#     def p_multiplicative_expr_2(self, p):
#         '''multiplicative_expr : multiplicative_expr DIVIDE parsed_divide unary_expr'''

    
#     def p_parsed_divide(self, p):
#         '''parsed_divide :'''


#     def p_multiplicative_expr_3(self, p):
#         '''multiplicative_expr : multiplicative_expr MODULO parsed_modulo unary_expr'''

    
#     def p_parsed_modulo(self, p):
#         '''parsed_modulo :'''


#     def p_multiplicative_expr_4(self, p):
#         '''multiplicative_expr : unary_expr'''

    
#     def p_unary_expr_1(self, p):
#         '''unary_expr : MINUS postfix_expr'''

    
#     def p_unary_expr_2(self, p):
#         '''unary_expr : PLUS postfix_expr'''

    
#     def p_unary_expr_3(self, p):
#         '''unary_expr : NOT postfix_expr'''

    
#     def p_unary_expr_4(self, p):
#         '''unary_expr : postfix_expr'''

    
#     def p_postfix_expr_1(self, p):
#         '''postfix_expr : LPAREN expr RPAREN'''

    
#     def p_postfix_expr_2(self, p):
#         '''postfix_expr : variable_access'''

    
#     def p_postfix_expr_3(self, p):
#         '''postfix_expr : function_call'''

    
#     def p_postfix_expr_4(self, p):
#         '''postfix_expr : constant'''


#     def p_constant_1(self, p):
#         '''constant : CONST_INT'''

                
#     def p_constant_2(self, p):
#         '''constant : CONST_REAL'''


#     def p_constant_3(self, p):
#         '''constant : CONST_CHAR'''

    
#     def p_constant_4(self, p):
#         '''constant : constant_bool'''

    
#     def p_constant_bool_1(self, p):
#         '''constant_bool : TRUE'''

    
#     def p_constant_bool_2(self, p):
#         '''constant_bool : FALSE'''

    
#     def p_type_1(self, p):
#         '''type : INT'''


#     def p_type_2(self, p):
#         '''type : REAL'''


#     def p_type_3(self, p):
#         '''type : CHAR'''


#     def p_type_4(self, p):
#         '''type : BOOL'''

    
#     def p_empty(self, p):
#         'empty :'
#         pass


#     def p_error(self, p):
#         if p:
#             # Just discard the token and tell the parser it's okay.
#             self.parser.errok()
#             raise SyntaxError('Syntax error at token', p)
#         else:
#           raise SyntaxError('Error at EOF')


class ParserCodeGenerator(object):
    tokens = Lexer.tokens

    def __init__(self) -> None:
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)

        self.function_builder = FunctionBuilder()
        self.function_director = FunctionDirector()
        self.variable_builder = VariableBuilder()
        self.semantic_table = SemanticTable()

        self.function_directory = None
        self.operator_stack = None
        self.operand_stack = None
        self.avail_counter = None
        self.quadruple_list = None

        self.function_director.builder = self.function_builder

    
    def reset(self):
        self.function_directory = FunctionDirectory()
        self.operator_stack = OperatorStack()
        self.operand_stack = OperandStack()
        self.avail_counter = defaultdict(int)
        self.quadruple_list = QuadrupleList()

        self.function_builder.reset()
        self.variable_builder.reset()

        self.function_scope = None
        self.shared_variable_declaration_type = None


    def parse(self, input):
        self.reset()
        return self.parser.parse(input)

    
    def p_program(self, p):
        '''program : init start'''
        print(self.function_directory.__str__())
        print(self.quadruple_list.__str__())
        # print(self.operator_stack.__str__())
        # print(self.operand_stack.__str__())


    def p_init(self, p):
        '''init :'''
        self.create_global_scope()
        self.create_main_function()


    def p_start_1(self, p):
        '''start : global_variables_declaration functions_definition entry_point_definition'''

    
    def p_start_2(self, p):
        '''start : global_variables_declaration entry_point_definition'''

    
    def p_start_3(self, p):
        '''start : functions_definition entry_point_definition'''
        

    def p_start_4(self, p):
        '''start : entry_point_definition'''


    def p_global_variables_declaration(self, p):
        '''global_variables_declaration : GLOBAL parsed_global_scope variables_declaration'''

    
    def p_parsed_global_scope(self, p):
        '''parsed_global_scope :'''
        self.set_function_scope('global')

    
    def p_functions_definition_1(self, p):
        '''functions_definition : functions_definition single_function_definition'''
    

    def p_functions_definition_2(self, p):
        '''functions_definition : single_function_definition'''

    
    def p_single_function_definition_primitive_type_1(self, p):
        '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


    def p_single_function_definition_primitive_type_2(self, p):
        '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_block'''

    
    def p_single_function_definition_primitive_type_3(self, p):
        '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_single_function_definition_primitive_type_4(self, p):
        '''single_function_definition : FUNCTION type parsed_function_return_type ID parsed_function_id LPAREN RPAREN instruction_block'''


    def p_single_function_definition_void_type_1(self, p):
        '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN local_variables_declaration instruction_block'''


    def p_single_function_definition_void_type_2(self, p):
        '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN function_definition_params RPAREN instruction_block'''


    def p_single_function_definition_void_type_3(self, p):
        '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_single_function_definition_void_type_4(self, p):
        '''single_function_definition : FUNCTION VOID parsed_function_void_return_type ID parsed_function_id LPAREN RPAREN instruction_block'''


    def p_parsed_function_id(self, p):
        '''parsed_function_id :'''
        function_id = p[-1]
        self.function_builder.set_id(function_id)
        self.set_function_scope(function_id)

        function = self.function_builder.build()

        self.function_directory.insert_function(function_id, function)


    def p_parsed_function_return_type(self, p):
        '''parsed_function_return_type :'''
        function_return_type = p[-1]
        self.function_builder.set_return_type(function_return_type)

    
    def p_parsed_function_void_return_type(self, p):
        '''parsed_function_void_return_type  :'''
        function_return_type = 'void'
        self.function_builder.set_return_type(function_return_type)


    def p_function_definition_params_1(self, p):
        '''function_definition_params : function_definition_params COMMA single_function_definition_param'''

    
    def p_function_definition_params_2(self, p):
        '''function_definition_params : single_function_definition_param'''


    def p_single_function_definition_param(self, p):
        '''single_function_definition_param : type ID'''
        variable_type = p[1]
        variable_id = p[2]

        self.variable_builder.set_type(variable_type)
        self.variable_builder.set_id(variable_id)

        variable = self.variable_builder.build()
        variable_declaration_scope = self.get_function_scope()

        self.function_directory.insert_function_variable(variable_declaration_scope, variable_id, variable)

    
    def p_entry_point_definition_1(self, p):
        '''entry_point_definition : START parsed_main_id LPAREN RPAREN local_variables_declaration instruction_block'''

    
    def p_entry_point_definition_2(self, p):
        '''entry_point_definition : START parsed_main_id LPAREN RPAREN instruction_block'''

 
    def p_parsed_main_id(self, p):
        '''parsed_main_id :'''
        self.set_function_scope('main')


    def p_local_variables_declaration(self, p):
        '''local_variables_declaration : LOCAL variables_declaration'''

    
    def p_variables_declaration(self, p):
        '''variables_declaration : VARIABLES COLON distinct_type_variables_declaration'''

    
    def p_distinct_type_variables_declaration_1(self, p):
        '''distinct_type_variables_declaration : distinct_type_variables_declaration shared_type_variables_declaration'''


    def p_distinct_type_variables_declaration_2(self, p):
        '''distinct_type_variables_declaration : shared_type_variables_declaration'''


    def p_shared_type_variables_declaration(self, p):
        '''shared_type_variables_declaration : type parsed_type shared_type_variables_declaration_list SEMI'''

    
    def p_parsed_type(self, p):
        '''parsed_type :'''
        variable_type = p[-1]
        self.set_shared_variable_type(variable_type)

    
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
        variable_id = p[1]
        variable_type = self.get_shared_variable_type()

        self.variable_builder.set_id(variable_id)
        self.variable_builder.set_type(variable_type)
        
        variable = self.variable_builder.build()
        variable_declaration_scope = self.get_function_scope()
        function_id = variable_declaration_scope

        self.function_directory.insert_function_variable(function_id, variable_id, variable)


    def p_dim_definition(self, p):
        '''dim_definition : LBRACKET CONST_INT RBRACKET'''

    
    def p_instruction_block_1(self, p):
        '''instruction_block : LBRACE statements RBRACE'''

    
    def p_instruction_block_2(self, p):
        '''instruction_block : LBRACE RBRACE'''

    
    def p_statements_1(self, p):
        '''statements : statements single_statement'''

    
    def p_statements_2(self, p):
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
        '''assignment : variable_access ASGMT parsed_asgmt expr SEMI'''
        self.create_assignment_quadruple()


    def p_assignment_2(self, p):
        '''assignment : variable_access ASGMT parsed_asgmt read'''

    
    def p_parsed_asgmt(self, p):
        '''parsed_asgmt :'''
        self.operator_stack.push(Operator.ASGMT)


    def p_variable_access(self, p):
        '''variable_access : ID parsed_id_variable_access dims_access'''

    
    def p_parsed_id_variable_access(self, p):
        '''parsed_id_variable_access :'''
        variable_id = p[-1]
        function_id = self.function_scope

        variable = self.function_directory.get_function_variable(function_id, variable_id)

        self.operand_stack.push(variable)


    def p_dims_access_1(self, p):
        '''dims_access : single_dim_access single_dim_access'''


    def p_dims_access_2(self, p):
        '''dims_access : single_dim_access'''

    
    def p_dims_access_3(self, p):
        '''dims_access : empty'''


    def p_single_dim_access(self, p):
        '''single_dim_access : LBRACKET expr RBRACKET'''

    
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
        '''additive_expr : additive_expr PLUS parsed_plus multiplicative_expr'''
        top_operator = self.operator_stack.top()
        if top_operator == Operator.PLUS:
            self.create_arithmetic_quadruple(top_operator)
    

    def p_parsed_plus(self, p):
        '''parsed_plus :'''
        self.operator_stack.push(Operator.PLUS)

    
    def p_additive_expr_2(self, p):
        '''additive_expr : additive_expr MINUS parsed_minus multiplicative_expr'''
        top_operator = self.operator_stack.top()
        if top_operator == Operator.MINUS:
            self.create_arithmetic_quadruple(top_operator)

    
    def p_parsed_minus(self, p):
        '''parsed_minus :'''
        self.operator_stack.push(Operator.MINUS)

    
    def p_additive_expr_3(self, p):
        '''additive_expr : multiplicative_expr'''


    def p_multiplicative_expr_1(self, p):
        '''multiplicative_expr : multiplicative_expr TIMES parsed_times unary_expr'''
        top_operator = self.operator_stack.top()
        if top_operator == Operator.TIMES:
            self.create_arithmetic_quadruple(top_operator)

    
    def p_parsed_times(self, p):
        '''parsed_times :'''
        self.operator_stack.push(Operator.TIMES)

    
    def p_multiplicative_expr_2(self, p):
        '''multiplicative_expr : multiplicative_expr DIVIDE parsed_divide unary_expr'''
        top_operator = self.operator_stack.top()
        if top_operator == Operator.DIVIDE:
            self.create_arithmetic_quadruple(top_operator)

    
    def p_parsed_divide(self, p):
        '''parsed_divide :'''
        self.operator_stack.push(Operator.DIVIDE)


    def p_multiplicative_expr_3(self, p):
        '''multiplicative_expr : multiplicative_expr MODULO parsed_modulo unary_expr'''
        top_operator = self.operator_stack.top()
        if top_operator == Operator.MODULO:
            self.create_arithmetic_quadruple(top_operator)

    
    def p_parsed_modulo(self, p):
        '''parsed_modulo :'''
        self.operator_stack.push(Operator.MODULO)


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
        p[0] = Type.INT


    def p_type_2(self, p):
        '''type : REAL'''
        p[0] = Type.REAL


    def p_type_3(self, p):
        '''type : CHAR'''
        p[0] = Type.CHAR


    def p_type_4(self, p):
        '''type : BOOL'''
        p[0] = Type.BOOL

    
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


    def create_global_scope(self):
        self.function_director.build_global_scope()
        function = self.function_builder.build()

        self.function_directory.insert_function(function.get_id(), function)
    

    def create_main_function(self):
        self.function_director.build_main_function()
        function = self.function_builder.build()

        self.function_directory.insert_function(function.get_id(), function)

    
    def create_next_temp_variable(self, variable_type: Type) -> Variable:
        count = self.avail_counter[variable_type]
        variable_id = f't_{variable_type.name}_{count}'

        self.variable_builder.set_id(variable_id)
        self.variable_builder.set_type(variable_type)
        variable = self.variable_builder.build()
        return variable

    
    def create_assignment_quadruple(self):
        operator = self.operator_stack.pop()
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()

        result_type = self.semantic_table.search_operation_result_type(
            right_operand.get_type(),
            left_operand.get_type(),
            operator
        )

        if result_type == Type.ERROR:
            raise TypeMismatchException()

        quadruple = Quadruple(operator, right_operand, None, left_operand)
        self.quadruple_list.insert_quadruple(quadruple)

    
    def create_arithmetic_quadruple(self, operator: Operator) -> None:
        self.operator_stack.pop()
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()

        result_type = self.semantic_table.search_operation_result_type(
            right_operand.get_type(),
            left_operand.get_type(),
            operator
        )

        if result_type == Type.ERROR:
            raise TypeMismatchException()

        result_variable = self.create_next_temp_variable(result_type)
        quadruple = Quadruple(operator, left_operand, right_operand, result_variable)
        
        self.quadruple_list.insert_quadruple(quadruple)
        self.operand_stack.push(result_variable)
        self.avail_counter[result_type] += 1


    def set_function_scope(self, scope: str) -> None:
        self.function_scope = scope


    def get_function_scope(self) -> str:
        return self.function_scope

    
    def set_shared_variable_type(self, type: str) -> None:
        self.shared_variable_declaration_type = type

    
    def get_shared_variable_type(self) -> str:
        return self.shared_variable_declaration_type


class TypeMismatchException(RuntimeError):
    pass


class SyntaxError(Exception):
    pass