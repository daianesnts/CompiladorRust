import sys
import ply.lex as lex
from indentstack import IndentStack

indentStack = IndentStack()

states = (
    ('mltlncomnt', 'exclusive'), # Comentário de múltiplas linhas
    ('sgnlncomnt', 'exclusive'), # Comentário de linha única
)

reserved = {
    'as':       'AS',
    'break':    'BREAK',
    'const':    'CONST',
    'continue': 'CONTINUE',
    'else':     'ELSE',
    'enum':     'ENUM',
    'false':    'FALSE',
    'fn':       'FN',
    'for':      'FOR',
    'if':       'IF',
    'impl':     'IMPL',
    'in':       'IN',
    'let':      'LET',
    'loop':     'LOOP',
    'mut':      'MUT',
    'pub':      'PUB',
    'ref':      'REF',
    'return':   'RETURN',
    'Self':     'SELFTYPE',
    'static':   'STATIC',
    'struct':   'STRUCT',
    'trait':    'TRAIT',
    'true':     'TRUE',
    'union':    'UNION',
    'where':    'WHERE',
    'while':    'WHILE',
}

tokens = ['ID', 'NUMBER', # Operadores aritméticos
          'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODL', 
          'ATTRIB', 'PLUSATTRIB', 'MINUSATTRIB', 'TIMESATTRIB', 'DIVIDEATTRIB', # Operadores de atribuição simples e compostos
          'EQUALS', 'NEQUALS', 'LESSEQ', 'GRTREQ', 'LESS', 'GRTR', # Operadores relacionais
          'LOGAND', 'LOGOR', "LOGNOT", # Operadores lógicos
          'BITAND', 'BITOR', 'BITXOR', 'LSHIFT', 'RSHIFT', # Operadores bit a bit
          'ARROW', #Seta de retorno
          'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', # Delimitadores
          'COLON', 'DCOLON', 'SCOLON', 'COMMA', 
          'INDENT', 'DEINDENT', # Indentação
          ]+ list(reserved.values())

t_ignore    = ' \t'

# Atribuição composta
t_PLUSATTRIB    = r'\+='
t_MINUSATTRIB   = r'-='
t_TIMESATTRIB   = r'\*='
t_DIVIDEATTRIB  = r'/='

# Operadores relacionais compostos
t_EQUALS    = r'=='
t_NEQUALS   = r'!='
t_LESSEQ    = r'<='
t_GRTREQ    = r'>='

# Operadores lógicos compostos
t_LOGAND    = r'&&'
t_LOGOR     = r'\|\|'

# Bit a bit compostos
t_LSHIFT        = r'<<'
t_RSHIFT        = r'>>'
 
# Seta de retorno
t_ARROW         = r'->'
 
# Namespace duplo 
t_DCOLON        = r'::'

# Operadores simples
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ATTRIB    = r'='
t_MODL      = r'%'
t_LESS      = r'<'
t_GRTR      = r'>'
t_LOGNOT    = r'!'      
t_BITOR     = r'\|'
t_BITXOR    = r'\^'

# Delimitadores
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COLON     = r':'
t_SCOLON    = r';'
t_COMMA     = r','

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LBRACE(t):
    r'\{'
    indentStack.push(indentStack.peek() + 1)
    return t

def t_RBRACE(t):
    r'\n[ \t]*\}'
    t.lexer.lineno += 1

    indent_str = t.value[1:]
    if ' ' in indent_str:
        raise Exception(f"Erro linha {t.lexer.lineno}: use tabs para indentação, não espaços")
    indent_level = indent_str.count('\t')
    top = indentStack.peek()
        
    if indent_level >= top or indent_level != top-1:
        raise Exception(
            f"Erro linha {t.lexer.lineno}:\nindentação inválida (esperava {top-1} tab(s), encontrou {indent_level})")
    indentStack.pop()
    t.value = r'\}'
    return t

def t_newline(t):
    r'\n[ \t]*'
    t.lexer.lineno += 1

    indent_str = t.value[1:]
    if ' ' in indent_str:
        raise Exception(f"Erro linha {t.lexer.lineno}: use tabs para indentação, não espaços")
    indent_level = indent_str.count('\t')
    top = indentStack.peek()
        
    if indent_level > top or indent_level < top:
        raise Exception(
            f"Erro linha {t.lexer.lineno}:\nindentação inválida (esperava {top} tab(s), encontrou {indent_level})") 

def t_error(t):
   print(f"Illegal character {t.value[0]}")
   t.lexer.skip(1)

'''
INICIO - ESTADO EXCLUSIVE COMENTÁRIO DE MÚLTIPLAS LINHAS
'''
t_mltlncomnt_ignore = ' \t'

def t_begin_mltlncomnt(t):
    r'/\*'
    t.lexer.begin('mltlncomnt')

def t_mltlncomnt_end_mltlncomnt(t):
    r'\*/'
    t.lexer.begin('INITIAL')

def t_mltlncomnt_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_mltlncomnt_ignoreall(t):
    # Essa regex tem a seguinte explicação:
    # () -> Tudo que tiver dentro é um elemento agrupado
    # ?: -> Indica que o agrupamento não será armazenado em memória
    # ?! -> É um 'negative lookahead' que possibilita ver se os próximos
    # caracteres foram os especificados. O objetivo aqui é parar de ler
    # caracteres caso os próximos dois caracteres sejam o "*/", que é o fim
    # de comentário multilinhas. "*/" não são consumidos e ficarão no buffer
    # para a função t_mltlncomnt_end_mltlncomnt
    # . -> Qualquer caractere (exceto quebra de linha)
    r'(?:(?!\*/).)+'
    pass

def t_mltlncomnt_error(t):
   print(f"Illegal character {t.value[0]}")
   t.lexer.skip(1)
'''
FIM - ESTADO EXCLUSIVE COMENTÁRIO DE MÚLTIPLAS LINHAS
'''

'''
INICIO - ESTADO EXCLUSIVE COMENTÁRIO LINHA ÚNICA
'''
t_sgnlncomnt_ignore = ' \t'

def t_begin_sgnlncomnt(t):
    r'//'
    t.lexer.begin('sgnlncomnt')

def t_sgnlncomnt_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')

def t_sgnlncomnt_ignoreall(t):
    r'(?:(?!\*/).)+'
    pass

def t_sgnlncomnt_error(t):
   print(f"Illegal character {t.value[0]}")
   t.lexer.skip(1)
'''
FIM - ESTADO EXCLUSIVE COMENTÁRIO LINHA ÚNICA
'''

def main():
    if len(sys.argv) < 2:
        print("Use: python lexer.py <arquivo_rust.rs>")
        exit(1)
    f = open(sys.argv[1], 'r')
    lexer = lex.lex(debug=0)
    lexer.input(f.read())
    for tok in lexer:
        print(f'Type: {tok.type}, Value: {tok.value}, Line: {tok.lineno}')

if __name__ == '__main__':
    main()
