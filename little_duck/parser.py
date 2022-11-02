import tokrules
import ply.lex as lex
import ply.yacc as yacc
import sys
from tokrules import tokens
from utils import read_file

def p_start(p):
    '''program : PROGRAM ID SEMI vars block
    | PROGRAM ID SEMI block
    '''

def p_vars(p):
    'vars : VAR var_decl'

def p_var_decl(p):
    '''var_decl : var_list COLON type SEMI
    | var_decl var_decl
    '''

def p_var_list(p):
    '''var_list : var_list COMMA ID
    | ID
    '''

def p_type(p):
    '''type : INT
    | FLOAT
    '''

def p_block(p):
    '''block : LBRACE statement_list RBRACE
    | LBRACE RBRACE
    '''

def p_statement_list(p):
    '''statement_list : statement_list statement
    | statement
    '''

def p_statement(p):
    '''statement : assignment
    | conditional
    | print
    '''

def p_assignment(p):
    'assignment : ID ASGMT expression SEMI'

def p_expression(p):
    '''expression : exp NEQUAL exp
    | exp LTHAN exp
    | exp GTHAN exp
    | exp
    '''

def p_conditional(p):
    '''conditional : IF LPAREN expression RPAREN block ELSE block SEMI
    | IF LPAREN expression RPAREN block SEMI
    '''

def p_print(p):
    'print : PRINT LPAREN print_args RPAREN SEMI'
def p_print_args(p):
    '''print_args : print_args COMMA print_args
    | expression
    | CONST_STRING
    '''

def p_exp(p):
    '''exp : exp PLUS term
    | expression MINUS term
    | term
    '''

def p_term(p):
    '''term : term TIMES factor
    | term DIVIDE factor
    | factor
    '''

def p_factor(p):
    '''factor : LPAREN expression RPAREN
    | PLUS constant
    | MINUS constant
    | constant
    '''

def p_constant(p):
    '''constant : ID
    | CONST_INT
    | CONST_FLOAT
    '''
def p_error(p):
    if p:
        print('Syntax error at token', p.type)
        parser.errok()
    else:
        print('Syntax error at EOF')

if len(sys.argv) == 3:
    mode = sys.argv[1]
    fname = sys.argv[2]
    data = read_file(fname)
    lexer = lex.lex(module=tokrules)
    parser = yacc.yacc()
    # Execute lexical analysis and print all tokens
    if mode == 'lexer':
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
    # Execute syntax analysis
    elif mode == 'parser':
        result = parser.parse(data)
    else:
        print('Usage: python little_duck.py <mode> <file>')