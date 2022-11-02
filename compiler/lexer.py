import ply.lex as lex

class Lexer(object):
    def __init__(self):
        self.lexer = lex.lex(module=self)

    reserved = {
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
        "malvera": "BOOL_FALSE",
        "ne": "NOT",
        "reel": "REAL",
        "skribi": "PRINT",
        "se": "IF",
        "tutmondaj": "GLOBAL",
        "variabloj": "VARIABLES", 
        "vera": "BOOL_TRUE",
    }

    tokens = [
        "ID",
        "CONST_FLOAT",
        "CONST_INT",
        "CONST_CHAR",
        "CONST_STRING",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "MODULO",
        'EQUAL',
        "NEQUAL",
        "LTHAN_EQUAL",
        "GTHAN_EQUAL",
        "LTHAN",
        "GTHAN",
        "ASGMT",
        "LPAREN",
        "RPAREN",
        'LBRACKET',
        'RBRACKET',
        "LBRACE",
        "RBRACE",
        "COLON",
        "SEMI",
        "COMMA",
     ] + list(reserved.values())

    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_MODULO = r"%"
    t_EQUAL = r'=='
    t_NEQUAL = r"!="
    t_LTHAN_EQUAL = r"<="
    t_GTHAN_EQUAL = r">="
    t_LTHAN = r"<"
    t_GTHAN = r">"
    t_ASGMT = r"="
    t_LPAREN = r"\("
    t_RPAREN = r"\)"
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBRACE = r"\{"
    t_RBRACE = r"\}"
    t_COLON = r":"
    t_SEMI = r";"
    t_COMMA = r","

    # t_ignore = ' \t\n\r\f\v'
    t_ignore = ' \t'

    
    def t_ID(self, t):
        r"[a-zA-Z_][a-zA-Z_0-9]*"
        t.type = self.reserved.get(t.value, "ID")
        return t


    def t_CONST_FLOAT(self, t):
        r"\d+\.\d+"
        t.value = float(t.value)
        return t


    def t_CONST_INT(self, t):
        r"\d+"
        t.value = int(t.value)
        return t

    
    def t_CONST_CHAR(self, t):
        r"'[ -~]'"
        return t


    def t_CONST_STRING(self, t):
        r'"([^"\\]|\\.)*"'
        return t


    # def t_COMMENT(self, t):
    #     r'[#].*'
    #     pass


    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])


    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
    

    def scan_single_token(self, data):
        self.lexer.input(data)
        tok = self.lexer.token()
        return tok


    def scan_multiple_tokens(self, data):
        tokens = []
        self.lexer.input(data)
        for tok in self.lexer:
            tokens.append(tok)
        
        return tokens

    def get_token_type(self, token: lex.LexToken) -> str:
        return token.type


    def get_token_value(self, token):
        return token.value


    def get_tokens_types(self, tokens):
        return [tok.type for tok in tokens]


    def get_tokens_values(self, tokens):
        return [tok.value for tok in tokens]
    