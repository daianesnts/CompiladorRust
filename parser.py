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

def p_traitbody_single(p):
    '''traitbody : signature'''
    p[0] = []

def p_traitbody_multi(p):
    '''traitbody : signature SCOLON traitbody'''
    p[0] = [p[1]] + p[3]


#COMANDOS
def p_stmts_single(p):
    '''stmts : stmt'''
    p[0] = [p[1]]

def p_stmts_multi(p):
    '''stmts : stmt stmts'''
    p[0] = p[1] + [p[2]]

def p_stm_decl(p):
    '''stmt : decl'''
    p[0] = p[1]

def p_stm_exp(p):
    '''stmt : exp SCOLON'''
    p[0] = ('exp', p[1])

def p_stm_ifr(p):
    '''stmt : ifr'''
    p[0] = p[1]

def p_stm_loop(p):
    '''stmt : LOOP LBRACE stmts RBRACE'''
    p[0] = ('loop', p[3])

def p_stm_while(p):
    '''stmt : WHILE exp LBRACE stmts RBRACE'''
    p[0] = ('while', p[2], p[4])

def p_stm_return(p):
    '''stmt : RETURN exp SCOLON'''
    p[0] = ('return', p[2])

def p_stm_break(p):
    '''stmt : BREAK SCOLON'''
    p[0] = ('break',)

def p_stm_continue(p):
    '''stmt : CONTINUE SCOLON'''
    p[0] = ('continue',)

#IF ELSE
def p_ifr_no_else(p):
    '''ifr : IF exp LBRACE stmts RBRACE'''
    p[0] = ('if', p[2], p[4], None)

def p_ifr_else(p):
    '''ifr : IF exp LBRACE stmts RBRACE ELSE LBRACE stmts RBRACE'''
    p[0] = ('if', p[2], p[4], 'else', p[8])

def p_ifr_elseif(p):
    '''ifr : IF exp LBRACE stmts RBRACE ELSE ifr'''
    p[0] = ('if', p[2], p[4], 'else', p[7])


#DECLARAÇÕES
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
    '''decllet : LET ID typedecl ATTRIB exp SCOLON'''
    p[0] = ('decllet', p[2], p[3], p[5])

def p_decl_mut(p):
    '''declmut : LET MUT ID typedecl ATTRIB exp SCOLON'''
    p[0] = ('declmut', p[3], p[4], p[6])

def p_decl_const(p):
    '''declcons : CONST ID COLON TYPE ATTRIB exp SCOLON'''
    p[0] = ('declcons', p[2], p[4], p[6])

def p_decl_exp(p):
    '''declexp : ID ATTRIB exp SCOLON'''
    p[0] = ('declexp', p[1], p[3])

def p_typedecl_typed(p):
    '''typedecl : COLON TYPE'''
    p[0] = ('typedecl', p[2])

#EXPRESSÕES
def p_exp(p):
    '''exp : exp_assign'''
    p[0] = p[1]

def p_exp_assign_equals(p):
    '''exp_assign : ID ATTRIB exp_assign'''
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
    '''exp_and : exp_and LOGAND exp_rel'''
    p[0] = ('exp_and', p[1], p[3])

def p_exp_and_rel(p):
    '''exp_and : exp_rel'''
    p[0] = p[1]

def p_exp_rel_equals(p):
    '''exp_rel : exp_bitor EQUALS exp_bitor'''
    p[0] = ('exp_rel', p[1], p[3])

def p_exp_rel_nequals(p):
    '''exp_rel : exp_bitor NEQUALS exp_bitor'''
    p[0] = ('exp_rel', p[1], p[3])

def p_exp_rel_less(p):
    '''exp_rel : exp_bitor LESS exp_bitor'''
    p[0] = ('exp_rel', p[1], p[3])

def p_exp_rel_grtr(p):
    '''exp_rel : exp_bitor GRTR exp_bitor'''
    p[0] = ('exp_rel', p[1], p[3])

def p_exp_rel_lesseq(p):
    '''exp_rel : exp_bitor LESSEQ exp_bitor'''
    p[0] = ('exp_rel', p[1], p[3])

def p_exp_rel_grtreq(p):
    '''exp_rel : exp_bitor GRTREQ exp_bitor'''
    p[0] = ('exp_rel', p[1], p[3])

def p_exp_rel_bitor(p):
    '''exp_rel : exp_bitor'''
    p[0] = p[1]

def p_exp_bitor_or(p):
    '''exp_bitor : exp_bitor BITOR exp_bitxor'''
    p[0] = ('exp_bitor', p[1], p[3])

def p_exp_bitor_bitxor(p):
    '''exp_bitor : exp_bitxor'''
    p[0] = p[1]

def p_exp_bitxor_xor(p):
    '''exp_bitxor : exp_bitxor BITXOR exp_bitand'''
    p[0] = ('exp_bitxor', p[1], p[3])

def p_exp_bitxor_bitand(p):
    '''exp_bitxor : exp_bitand'''
    p[0] = p[1]

def p_exp_bitand_and(p):
    '''exp_bitand : exp_bitand BITAND exp_shift'''
    p[0] = ('exp_bitand', p[1], p[3])

def p_exp_bitand_shift(p):
    '''exp_bitand : exp_shift'''
    p[0] = p[1]

def p_exp_shift_lshift(p):
    '''exp_shift : exp_shift LSHIFT exp_add'''
    p[0] = ('exp_shift', p[1], p[3])

def p_exp_shift_rshift(p):
    '''exp_shift : exp_shift RSHIFT exp_add'''
    p[0] = ('exp_shift', p[1], p[3])

def p_exp_shift_add(p):
    '''exp_shift : exp_add'''
    p[0] = p[1]

def p_exp_add_plus(p):
    '''exp_add : exp_add PLUS exp_mul'''
    p[0] = ('exp_add', p[1], p[3])

def p_exp_add_minus(p):
    '''exp_add : exp_add MINUS exp_mul'''
    p[0] = ('exp_add', p[1], p[3])

def p_exp_add_mul(p):
    '''exp_add : exp_mul'''
    p[0] = p[1]

def p_exp_mul_times(p):
    '''exp_mul : exp_mul TIMES exp_unary'''
    p[0] = ('exp_mul', p[1], p[3])

def p_exp_mul_divide(p):
    '''exp_mul : exp_mul DIVIDE exp_unary'''
    p[0] = ('exp_mul', p[1], p[3])

def p_exp_mul_modl(p):
    '''exp_mul : exp_mul MODL exp_unary'''
    p[0] = ('exp_mul', p[1], p[3])

def p_exp_mul_unary(p):
    '''exp_mul : exp_unary'''
    p[0] = p[1]

def p_exp_unary_not(p):
    '''exp_unary : LOGNOT exp_unary'''
    p[0] = ('exp_unary_not', p[2])

def p_exp_unary_neg(p):
    '''exp_unary : MINUS exp_unary'''
    p[0] = ('exp_unary_neg', p[2])

def p_exp_unary_primary(p):
    '''exp_unary : exp_primary'''
    p[0] = p[1]

def p_exp_primary_call(p):
    '''exp_primary : call'''
    p[0] = p[1]

def p_exp_primary_num(p):
    '''exp_primary : NUMBER'''
    p[0] = ('num', p[1])

def p_exp_primary_id(p):
    '''exp_primary : ID'''
    p[0] = ('id', p[1])

def p_exp_primary_true(p):
    '''exp_primary : TRUE'''
    p[0] = ('bool', True)

def p_exp_primary_false(p):
    '''exp_primary : FALSE'''
    p[0] = ('bool', False)

def p_exp_primary_paren(p):
    '''exp_primary : LPAREN exp RPAREN'''
    p[0] = p[2]

def p_exp_primary_block_exp(p):
    '''exp_primary : LBRACE stmts exp RBRACE'''
    p[0] = ('block', p[2], p[3])

def p_exp_primary_block(p):
    '''exp_primary : LBRACE stmts RBRACE'''
    p[0] = ('block', p[2], None)


#CHAMADAS DE FUNÇÃO
def p_call_with_params(p):
    '''call : ID LPAREN args RPAREN'''
    p[0] = ('call', p[1], p[3])

def p_call_no_params(p):
    '''call : ID LPAREN RPAREN'''
    p[0] = ('call', p[1])

def p_args_single(p):
    '''args : exp'''
    p[0] = [p[1]]

def p_args_multi(p):
    '''args : exp COMMA args'''
    p[0] = [p[1]] + p[3]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error: unexpected end of file")


tokens = lexer.tokens

parser = yacc.yacc()

def main():
 
 
    if __name__ == '__main__':
        main()