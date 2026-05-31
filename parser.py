import ply.yacc as yacc
import ply.lex as lex
import lexer

# Token fictício usado apenas para resolver problema de precedência 
tokens = lexer.tokens + ['UMINUS']

precedence = (
    ('right', 'ATTRIB', 'PLUSATTRIB', 'MINUSATTRIB', 'TIMESATTRIB', 'DIVIDEATTRIB'),
    ('left',  'LOGOR'),
    ('left',  'LOGAND'),
    ('nonassoc', 'EQUALS', 'NEQUALS', 'LESS', 'GRTR', 'LESSEQ', 'GRTREQ'),
    ('left',  'BITOR'),
    ('left',  'BITXOR'),
    ('left',  'BITAND'),
    ('left',  'LSHIFT', 'RSHIFT'),
    ('left',  'PLUS', 'MINUS'),
    ('left',  'TIMES', 'DIVIDE', 'MODL'),
    ('right', 'LOGNOT', 'UMINUS'),
)

#PRORAMA
def p_program_single(p):
 

def p_program_multi(p):
    
 
def p_topdecl_func(p):
    
 
def p_topdecl_struct(p):
    
 
def p_topdecl_trait(p):
    
 

#FUNCOES 
def p_funcdecl(p):
    
 
def p_signature(p):
    
 
def p_rettype_arrow(p):
    


def p_rettype_empty(p):
    
 
def p_sigparams_some(p):
    

def p_sigparams_empty(p):
    
 
def p_sigparam_single(p):
    
 
def p_sigparam_multi(p):
    

def p_body(p):
    
 
def p_body_expr(p):
    
 
def p_body_only_expr(p):
    
 

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
    'exp : MINUS exp %prec UMINUS'
    p[0] = ('unary', '-', p[2])
 
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