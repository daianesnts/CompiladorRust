import ply.yacc as yacc
import ply.lex as lex
import lexer

#PROGRAMA
def p_program_single(p):
    '''program : topdecl'''
    p[0] = ('program', [p[1]])

def p_program_multi(p):
    '''program : topdecl program'''
    p[0] = ('program', [p[1]] + p[2][1])

def p_topdecl_func(p):
    '''topdecl : funcdecl'''
    p[0] = p[1]

def p_topdecl_struct(p):
    '''topdecl : structdecl'''
    p[0] = p[1]

def p_topdecl_trait(p):
    '''topdecl : traitdecl'''
    p[0] = p[1]


#FUNÇÕES
def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = ('funcdecl', p[1], p[2])

def p_signature(p):
    '''signature : FN ID signaturei'''
    p[0] = ('signature', p[2], p[3])

def p_signaturei_p(p):
    '''signaturei : signaturep'''
    p[0] = p[1]

def p_signaturei_np(p):
    '''signaturei : signaturenp'''
    p[0] = p[1]

def p_signaturep_arrow(p):
    '''signaturep : LPAREN sigparams RPAREN ARROW TYPE'''
    p[0] = ('signaturep', p[2], p[5])

def p_signaturep_no_arrow(p):
    '''signaturep : LPAREN sigparams RPAREN'''
    p[0] = ('signaturep', p[2], None)

def p_signaturenp_arrow(p):
    '''signaturenp : LPAREN RPAREN ARROW TYPE'''
    p[0] = ('signaturenp', [], p[4])

def p_signaturenp_no_arrow(p):
    '''signaturenp : LPAREN RPAREN'''
    p[0] = ('signaturenp', [], None)

def p_sigparams_single(p):
    '''sigparams : sigparam'''
    p[0] = [p[1]]

def p_sigparams_multi(p):
    '''sigparams : sigparam COMMA sigparams'''
    p[0] = [p[1]] + p[3]

def p_sigparam(p):
    '''sigparam : ID COLON TYPE'''
    p[0] = ('param', p[1], p[3])

def p_body(p):
    '''body : LBRACE stmts RBRACE'''
    p[0] = ('body', p[2])


#STRUCT E TRAIT 
def p_structdecl(p):
    '''structdecl : STRUCT ID LBRACE structfields RBRACE'''
    p[0] = ('structdecl', p[2], p[4])


def p_structfields_empty(p):
    '''structfields : empty'''
    p[0] = []


def p_structfields_single(p):
    '''structfields : structfield'''
    p[0] = [p[1]]


def p_structfields_multi(p):
    '''structfields : structfield COMMA structfields'''
    p[0] = [p[1]] + p[3]


def p_structfield(p):
    '''structfield : ID COLON TYPE'''
    p[0] = ('structfield', p[1], p[3])


def p_traitdecl(p):
    '''traitdecl : TRAIT ID LBRACE traitbody RBRACE'''
    p[0] = ('traitdecl', p[2], p[4])


def p_traitbody_empty(p):
    '''traitbody : empty'''
    p[0] = None


def p_traitbody(p):
    '''traitbody : signature SEMICOLON traitbody'''
    p[0] = [p[1]] + p[3]  


#COMANDOS 
def p_stmts_single(p):
   '''stmts : stmt'''
   p[0] = [p[1]]

def p_stmts_multi(p):
   '''stmts : stmts stmt'''
   p[0] = p[1] + [p[2]]

def p_stm_decl(p):
   '''stmt : decl'''
   p[0] = p[1]
 
def p_stm_exp(p):
   '''stmt : expr SCOLON'''
   p[0] = ('exp', p[1])
 
def p_stm_ifr(p):
   '''stmt : ifr'''
   p[0] = p[1]
 
def p_stm_loop(p):
   '''stmt : LOOP LBRACE expr RBRACE'''
   p[0] = ('loop', p[2])
 
def p_stm_while(p):
   '''stmt : WHILE expr LBRACE stmts RBRACE'''
   p[0] = ('while',p[2],p[3])
 
def p_stm_return(p):
   '''stmt : RETURN expr SCOLON'''
   p[0] = ('return', p[2])
 
def p_stm_break(p):
   '''stmt : BREAK SCOLON'''
   p[0] = ('break',)

def p_stm_continue(p):
   '''stmt : CONTINUE SCOLON'''
   p[0] = ('continue',)

#IFELSE
def p_ifr_no_else(p):
   '''ifr : IF expr LBRACE stmts RBRACE'''
   p[0] = ('if', p[2], p[3], None)
    
def p_ifr_else(p):
   '''ifr : IF expr LBRACE stmts RBRACE ELSE LBRACE stmts RBRACE'''
   p[0] = ('if', p[2], p[3], 'else', p[5])
 
def p_ifr_elseif(p):
    '''ifr : IF expr LBRACE stmts RBRACE ELSE ifr'''
    p[0] = ('if', p[2], p[3], 'else', p[5])
 
#DECLARACOES
def p_decllet(p):
    '''decl : decllet'''
    p[0] = p[1]
def p_declmut(p):
    '''decl : declmut'''
    p[0] = p[1]
def p_declcons(p):
    '''decl : declcons'''
    p[0] = p[1]
def p_declexp(p):
    '''decl : declexp'''
    p[0] = p[1]
def p_decl_let(p):
    '''decllet : LET ID typedecl EQUALS exp SEMICOLON'''
    p[0] = ('decllet', p[2], p[3], p[5])
 
def p_decl_mut(p):
    '''declmut : LET MUT ID typedecl EQUALS exp SEMICOLON'''
    p[0] = ('declmut', p[3], p[4],p[6])
 
def p_decl_const(p):
    '''declcons : CONST ID EQUALS TYPE EQUALS NUM SEMICOLON'''
    p[0] = ('declcons', p[2],p[4], p[6])

def p_decl_exp(p):
    '''declexp : ID EQUALS exp SEMICOLON'''
    p[0] = ('declexp', p[1], p[3])
 
def p_typedecl_typed(p):
    '''typedecl : COLON TYPE'''
    p[0] = ('typedecl', p[2])
    
def p_typedecl_empty(p):
    '''typedecl : empty'''
    p[0] = None
 
#EXPRESSOES
def p_exp_assign(p):
    '''exp : exp_assign'''
    p[0] = [p[1]]
    
def p_exp_assign_equals(p):
    '''exp_assign : ID EQUALS exp_assign'''
    p[0] = ('exp_assign', p[1], p[3])

def p_exp_assign_plusattrib(p):
    '''exp_assign : ID PLUSATTRIB exp_assign'''
    p[0] = ('exp_assign', p[1], p[3])
    
def p_exp_assign_minusattrib(p):
    '''exp_assign : ID MINUSATTRIB exp_assign'''
    p[0] = ('exp_assign', p[1], p[3])

def p_exp_assign_timesattrib(p):
    '''exp_assign : ID TIMESATTRIB exp_assign'''
    p[0] = ('exp_assign', p[1], p[3]) 

def p_exp_assign_divideattrib(p):
    '''exp_assign : ID DIVIDEATTRIB exp_assign'''
    p[0] = ('exp_assign', p[1], p[3])
    
def p_exp_assign_or(p):
    '''exp_assign : exp_or'''
    p[0] = p[1]


def p_exp_or_logor(p):
    '''exp_or : exp_or LOGOR exp_and'''
    p[0] = ('exp_or', p[1], p[3])

def p_exp_or_and(p):
    '''exp_or : exp_and'''
    p[0] = p[1]

def p_exp_and_logand(p):
    '''exp_and: exp_and LOGAND exp_rel'''
    p[0] = ('exp_and', p[1], p[3])
#Correção ate aqui
def p_exp_attrib(p):
   '''attrib : ID EQUALS expr'''
   p[0] = ('attrib', p[1],p[3])
 
def p_exp_compound(p):
   '''compound : LBRACE stmts RBRACE'''
   p[0] = ('compound', p[2])
 
def p_exp_unary_not(p):
   '''expr : LOGNOT expr'''
   p[0] = ('unary not', p[2])
 
def p_exp_unary_minus(p):
   '''expr : MINUS expr'''
   p[0] = ('unary minus', p[2])
 
def p_exp_paren(p):
   '''expr : LPAREN expr RPAREN'''
   p[0] = ('exp paren', p[2])
 
def p_exp_block_expr(p):
   '''expr : LBRACE stmts expr RBRACE'''
   p[0] = ('block expr', p[2], p[3])
 
def p_exp_block_stmts(p):
   '''expr : LBRACE stmts RBRACE'''
   p[0] = ('block stmts', p[2])

def p_exp_call(p):
   '''expr : ID LPAREN args RPAREN'''
   p[0] = ('exp call', p[1], p[3])
 
def p_exp_number(p):
   '''expr : NUMBER'''
   p[0] = ('number', p[1])
 
def p_exp_true(p):
   '''expr : TRUE'''
   p[0] = ('boolean', True)
 
def p_exp_false(p):
   '''expr : FALSE'''
   p[0] = ('boolean', False)    
 
def p_exp_id(p):
   '''expr : ID'''
   p[0] = ('id', p[1])

#CHAMADA DE FUNÇÃO
def p_call_with_params(p):
   '''expr : ID LPAREN args RPAREN'''
   p[0] = ('call with params',p[1],p[3])
 
def p_call_no_params(p):
   '''expr : ID LPAREN RPAREN'''
   p[0] = ('call no params', p[1])
 
def p_params_single(p):
   '''args : ID'''
   p[0] = [p[1]]
 
def p_params_multi(p):
   '''args : args COMMA ID'''
   p[0] = p[1] + [p[3]]


def p_error(p):
   if p:
    print(f"Illegal character {p.value[0]}")
   else:
      print("Syntax error: unexpected end of file")

def main():
 
 
    if __name__ == '__main__':
        main()
