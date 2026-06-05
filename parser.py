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
    
 
def p_ifr_else(p):
    
 
def p_ifr_elseif(p):
    
 
#DECLARACOES
def p_decl_let(p):
    
 
def p_decl_mut(p):
    
 
def p_decl_const(p):
    

def p_decl_exp(p):
    
 
def p_typedecl_typed(p):
    
 
def p_typedecl_empty(p):
    
 
#EXPRESSOES
def p_exp_binop(p):

 
def p_exp_attrib(p):
   
 
def p_exp_compound(p):
   
 
def p_exp_unary_not(p):
   
 
def p_exp_unary_minus(p):
 
 
def p_exp_paren(p):
    
 
def p_exp_block_expr(p):
    
 
def p_exp_block_stmts(p):
    
 
def p_exp_call(p):
   
 
def p_exp_number(p):
    
 
def p_exp_true(p):
   
 
def p_exp_false(p):
    
 
def p_exp_id(p):
    

#CHAMADA DE FUNÇÃO
def p_call_with_params(p):
    
 
def p_call_no_params(p):
    
 
def p_params_single(p):
    
 
def p_params_multi(p):
   


def p_error(p):
   if p:
    print(f"Illegal character {p.value[0]}")
   else:
      print("Syntax error: unexpected end of file")

def main():
 
 
if __name__ == '__main__':
    main()
