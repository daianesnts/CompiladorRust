import ply.yacc as yacc
import ply.lex as lex
import lexer

#PROGRAMA
def p_program_single(p):
 'program : topdecl'
 p[0] = ('program', [p[1]]))

def p_program_multi(p):
 'program : topdecl program'
 p[0] = ('program', [p[1]] + p[2][1])
 
def p_topdecl_func(p):
 'topdecl : funcdecl'
 p[0] = p[1]
 
def p_topdecl_struct(p):
 'topdecl : structdecl'
 p[0] = p[1]

def p_topdecl_trait(p):
 'topdecl : traitdecl'
 p[0] = p[1]
 

#FUNCOES 
def p_funcdecl(p):
 'funcdecl : signature body'
 p[0] = ('funcdecl', p[1], p[2])
 
def p_signature(p):
 'signature : FN ID signaturei'
 p[0] = ('signature', p[2], p[3])
 
def p_signaturei_p(p):
 'signaturei : signaturep'
 p[0] = p[1]

def p_signaturei_np(p):
 'signaturei : signaturenp'
 p[0] = p[1]

def p_signaturep_arrow(p):
 'signaturep : LPAREN sigparams RPAREN ARROW TYPE'
 p[0] = ('signaturep', p[2], p[5])

def p_signaturep_no_arrow(p):
 'signaturep : FN ID LPAREN sigparams RPAREN'
 p[0] = ('signaturep', p[4], None)

def p_signaturenp_arrow(p):
 'signaturenp : LPAREN RPAREN ARROW TYPE'
 p[0] = ('signaturenp', [], p[4])

def p_signaturenp_no_arrow(p):
 'signaturenp : FN ID LPAREN RPAREN'
 p[0] = ('signaturenp', [], None)

def p_sigparams_empty(p):
 'sigparams : sigparam'
 p[0] = [p[1]]

def p_sigparams_COMMA(p):
 'sigparams : sigparam COMMA sigparams'
 p[0] = [p[1]] + p[3]

def p_sigparam_single(p):
 'sigparam : ID COLON TYPE'
 p[0] = ('param', p[1], p[3])
def p_body(p):
 'body : LBRACE stmts RBRACE'
 p[0] = ('body', p[2])


#STRUCT E TRAIT 
def p_structdecl(p):
    
 
def p_structfields_empty(p):
    
 
def p_structfields_single(p):
    
 
def p_structfields_multi(p):
    
 
def p_structfield(p):
 

def p_traitdecl(p):
    
 
def p_traitbody_empty(p):
    
 
def p_traitbody(p):
    
 

#COMANDOS 
def p_stmts_single(p):
    
 
def p_stmts_multi(p):
    
 
def p_stm_decl(p):
    
 
def p_stm_exp(p):
    
 
def p_stm_ifr(p):
    
 
def p_stm_loop(p):
    
 
def p_stm_while(p):
    
 
def p_stm_return(p):
    
 
def p_stm_break(p):
    
 
def p_stm_continue(p):

 

#IFELSE
def p_ifr_no_else(p):
   '''ifr : IF expr block'''
   p[0] = ('if', p[2], p[3], None)
    
def p_ifr_else(p):
   '''ifr : IF expr block ELSE block'''
   p[0] = ('if', p[2], p[3], 'else', p[5])
 
def p_ifr_elseif(p):
   '''ifr : IF expr block ELSE ifr'''
   p[0] = ('if', p[2], p[3], 'else', p[5])
 
#DECLARACOES
def p_decl_let(p):
    
 
def p_decl_mut(p):
    
 
def p_decl_const(p):
    

def p_decl_exp(p):
    
 
def p_typedecl_typed(p):
    
 
def p_typedecl_empty(p):
    
 
#EXPRESSOES
def p_exp_binop(p):
   '''expr : expr PLUS  expr
   | expr MINUS expr
   | expr TIMES expr
   | expr DIVIDE expr
   | expr EQUALS expr
   | expr NEQUALS expr
   | expr LESS expr
   | expr GRTR expr'''
   p[0] = ('binop', p[2], p[1], p[3])
 
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
