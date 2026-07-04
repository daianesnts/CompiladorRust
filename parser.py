import ply.yacc as yacc
from lexer import *
from sintaxeAbstrata import *

#PROGRAMA
def p_program_single(p):
    '''program : topdecl'''
    p[0] = ProgramTopDecl(p[1])

def p_program_multi(p):
    '''program : topdecl program'''
    p[0] = ProgramTopDeclProgram(p[1], p[2])

def p_topdecl_func(p):
    '''topdecl : funcdecl'''
    p[0] = TopDeclFuncDecl(p[1])

def p_topdecl_struct(p):
    '''topdecl : structdecl'''
    p[0] = TopDeclStructDecl(p[1])

def p_topdecl_trait(p):
    '''topdecl : traitdecl'''
    p[0] = TopDeclTraitDecl(p[1])


#FUNÇÕES
def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = FuncDeclSignatureBody(p[1], p[2])

def p_signature(p):
    '''signature : FN ID signaturei'''
    p[0] = SignatureFunc(p[2], p[3])

def p_signaturei_p(p):
    '''signaturei : signaturep'''
    p[0] = SignatureISigP(p[1])

def p_signaturei_np(p):
    '''signaturei : signaturenp'''
    p[0] = SignatureISigNP(p[1])

def p_signaturep_arrow(p):
    '''signaturep : LPAREN sigparams RPAREN ARROW type'''
    p[0] = SignatureFuncP(p[2], p[5])

def p_signaturep_no_arrow(p):
    '''signaturep : LPAREN sigparams RPAREN'''
    p[0] = SignatureFuncPVoid(p[2])

def p_signaturenp_arrow(p):
    '''signaturenp : LPAREN RPAREN ARROW type'''
    p[0] = SignatureFuncNP(p[4])

def p_signaturenp_no_arrow(p):
    '''signaturenp : LPAREN RPAREN'''
    p[0] = SignatureFuncNPVoid()

def p_sigparams_single(p):
    '''sigparams : sigparam'''
    p[0] = SigParamsSingle(p[1])

def p_sigparams_multi(p):
    '''sigparams : sigparam COMMA sigparams'''
    p[0] = SigParamsMulti(p[1], p[3])

def p_sigparam(p):
    '''sigparam : ID COLON type'''
    p[0] = SigParamConcrete(p[1], p[3])

def p_body(p):
    '''body : LBRACE stmts RBRACE'''
    p[0] = BodyConcrete(p[2])


#STRUCT E TRAIT
def p_structdecl(p):
    '''structdecl : STRUCT ID LBRACE structfields RBRACE'''
    p[0] = StructDeclConcrete(p[2], p[4])

def p_structfields_single(p):
    '''structfields : structfield'''
    p[0] = StructFieldsSingle(p[1])

def p_structfields_multi(p):
    '''structfields : structfield COMMA structfields'''
    p[0] = StructFieldsMulti(p[1], p[3])

def p_structfield(p):
    '''structfield : ID COLON type'''
    p[0] = StructFieldConcrete(p[1], p[3])

def p_traitdecl(p):
    '''traitdecl : TRAIT ID LBRACE traitbody RBRACE'''
    p[0] = TraitDeclConcrete(p[2], p[4])

"""
def p_traitbody_single(p):
    '''traitbody : signature'''
    p[0] = TraitBodySingle(p[1])

def p_traitbody_multi(p):
    '''traitbody : signature SCOLON traitbody'''
    p[0] = TraitBodyMulti(p[1], p[3])
"""
def p_traitbody_single(p):
    '''traitbody : traitsignatures'''
    p[0] = TraitBodySingle(p[1])

def p_traitbody_multi(p):
    '''traitbody : traitsignatures traitbody'''
    p[0] = TraitBodyMulti(p[1], p[2])

def p_traitsignatures_signature(p):
    '''traitsignatures : signature SCOLON'''
    p[0] = TraitSignaturesSignature(p[1])

def p_traitsignatures_funcdecl(p):
    '''traitsignatures : funcdecl'''
    p[0] = TraitSignaturesFuncDecl(p[1])

def p_traitsignatures_traitmethod(p):
    '''traitsignatures : traitmethod'''
    p[0] = TraitSignaturesTraitMethod(p[1])

def p_traitmethod(p):
    '''traitmethod : FN ID traitsignature'''
    p[0] = TraitMethodConcrete(p[2], p[3])

def p_traitsignature(p):
    '''traitsignature : traitsignaturep SCOLON'''
    p[0] = TraitSignatureConcrete(p[1], None)

def p_traitsignature_body(p):
    '''traitsignature : traitsignaturep body'''
    p[0] = TraitSignatureConcrete(p[1], p[2])

def p_traitsignaturep_singlep(p):
    '''traitsignaturep : LPAREN BITAND SELFTYPE RPAREN ARROW type'''
    p[0] = TraitSignaturePSingleP(p[6])

def p_traitsignaturep_singlepv(p):
    '''traitsignaturep : LPAREN BITAND SELFTYPE RPAREN'''
    p[0] = TraitSignaturePSinglePV()

def p_traitsignaturep_multip(p):
    '''traitsignaturep : LPAREN BITAND SELFTYPE COMMA sigparams RPAREN ARROW type'''
    p[0] = TraitSignaturePMultiP(p[5], p[8])

def p_traitsignaturep_multipv(p):
    '''traitsignaturep : LPAREN BITAND SELFTYPE COMMA sigparams RPAREN'''
    p[0] = TraitSignaturePMultiPV(p[5])

#COMANDOS
def p_stmts_single(p):
    '''stmts : stmt'''
    p[0] = StmtsSingle(p[1])

def p_stmts_multi(p):
    '''stmts : stmt stmts'''
    p[0] = StmtsMulti(p[1], p[2])

def p_stm_decl(p):
    '''stmt : decl'''
    p[0] = StmDecl(p[1])

def p_stm_exp(p):
    '''stmt : exp SCOLON'''
    p[0] = StmExp(p[1])

def p_stm_ifr(p):
    '''stmt : ifr'''
    p[0] = StmIfr(p[1])

def p_stm_loop(p):
    '''stmt : LOOP LBRACE stmts RBRACE'''
    p[0] = StmLoop(p[3])

def p_stm_while(p):
    '''stmt : WHILE exp LBRACE stmts RBRACE'''
    p[0] = StmWhile(p[2], p[4])

def p_stm_return(p):
    '''stmt : RETURN exp SCOLON'''
    p[0] = StmReturn(p[2])

def p_stm_break(p):
    '''stmt : BREAK SCOLON'''
    p[0] = StmBreak()

def p_stm_continue(p):
    '''stmt : CONTINUE SCOLON'''
    p[0] = StmContinue()

#IF ELSE
def p_ifr_no_else(p):
    '''ifr : IF exp LBRACE stmts RBRACE'''
    p[0] = IfNoElse(p[2], p[4])

def p_ifr_else(p):
    '''ifr : IF exp LBRACE stmts RBRACE ELSE LBRACE stmts RBRACE'''
    p[0] = IfElse(p[2], p[4], p[8])

def p_ifr_elseif(p):
    '''ifr : IF exp LBRACE stmts RBRACE ELSE ifr'''
    p[0] = IfElseIfr(p[2], p[4], p[7])


#DECLARAÇÕES
"""
def p_decllet(p):
    '''decl : decllet'''
    p[0] = DeclLet(p[1])

def p_declmut(p):
    '''decl : declmut'''
    p[0] = p[1]

def p_declcons(p):
    '''decl : declcons'''
    p[0] = p[1]

def p_declexp(p):
    '''decl : declexp'''
    p[0] = p[1]
"""

def p_decl_let(p):
    '''decl : LET ID typedecl ATTRIB exp SCOLON'''
    p[0] = DeclLet(p[2], p[3], p[5])

def p_decl_mut(p):
    '''decl : LET MUT ID typedecl ATTRIB exp SCOLON'''
    p[0] = DeclMut(p[3], p[4], p[6])

def p_decl_const(p):
    '''decl : CONST ID COLON type ATTRIB exp SCOLON'''
    p[0] = DeclCons(p[2], p[4], p[6])

"""
def p_decl_exp(p):
    '''decl : ID ATTRIB exp SCOLON'''
    p[0] = DeclExp(p[1], p[3])
"""

def p_typedecl_typed(p):
    '''typedecl : COLON type'''
    p[0] = TypeDeclConcrete(p[2])

def p_typedecl_empty(p):
    '''typedecl :'''
    p[0] = TypeDeclConcrete(None)

#EXPRESSÕES
def p_exp(p):
    '''exp : exp_assign'''
    p[0] = ExpAssignConcrete(p[1])

def p_exp_assign_equals(p):
    '''exp_assign : ID ATTRIB exp_assign'''
    p[0] = ExpAtrib(p[1], p[3])

def p_exp_assign_plusattrib(p):
    '''exp_assign : ID PLUSATTRIB exp_assign'''
    p[0] = ExpAtribuiSoma(p[1], p[3])

def p_exp_assign_minusattrib(p):
    '''exp_assign : ID MINUSATTRIB exp_assign'''
    p[0] = ExpAtribuiSubtracao(p[1], p[3])

def p_exp_assign_timesattrib(p):
    '''exp_assign : ID TIMESATTRIB exp_assign'''
    p[0] = ExpAtribuiMultiplicacao(p[1], p[3])

def p_exp_assign_divideattrib(p):
    '''exp_assign : ID DIVIDEATTRIB exp_assign'''
    p[0] = ExpAtribuiDivisao(p[1], p[3])

def p_exp_assign_or(p):
    '''exp_assign : exp_or'''
    p[0] = ExpExpOU(p[1])

def p_exp_or_logor(p):
    '''exp_or : exp_or LOGOR exp_and'''
    p[0] = ExpOU(p[1], p[3])

def p_exp_or_and(p):
    '''exp_or : exp_and'''
    p[0] = ExpExpE(p[1])

def p_exp_and_logand(p):
    '''exp_and : exp_and LOGAND exp_rel'''
    p[0] = ExpE(p[1], p[3])

def p_exp_and_rel(p):
    '''exp_and : exp_rel'''
    p[0] = ExpExpRel(p[1])

def p_exp_rel_equals(p):
    '''exp_rel : exp_bitor EQUALS exp_bitor'''
    p[0] = ExpRelConcrete(p[1], p[2], p[3])

def p_exp_rel_nequals(p):
    '''exp_rel : exp_bitor NEQUALS exp_bitor'''
    p[0] = ExpRelConcrete(p[1], p[2], p[3])

def p_exp_rel_less(p):
    '''exp_rel : exp_bitor LESS exp_bitor'''
    p[0] = ExpRelConcrete(p[1], p[2], p[3])

def p_exp_rel_grtr(p):
    '''exp_rel : exp_bitor GRTR exp_bitor'''
    p[0] = ExpRelConcrete(p[1], p[2], p[3])

def p_exp_rel_lesseq(p):
    '''exp_rel : exp_bitor LESSEQ exp_bitor'''
    p[0] = ExpRelConcrete(p[1], p[2], p[3])

def p_exp_rel_grtreq(p):
    '''exp_rel : exp_bitor GRTREQ exp_bitor'''
    p[0] = ExpRelConcrete(p[1], p[2], p[3])

def p_exp_rel_bitor(p):
    '''exp_rel : exp_bitor'''
    p[0] = ExpExpBitor(p[1])

def p_exp_bitor_or(p):
    '''exp_bitor : exp_bitor BITOR exp_bitxor'''
    p[0] = ExpBitOrConcrete(p[1], p[3])

def p_exp_bitor_bitxor(p):
    '''exp_bitor : exp_bitxor'''
    p[0] = ExpExpBitXor(p[1])

def p_exp_bitxor_xor(p):
    '''exp_bitxor : exp_bitxor BITXOR exp_bitand'''
    p[0] = ExpBitXorConcrete(p[1], p[3])

def p_exp_bitxor_bitand(p):
    '''exp_bitxor : exp_bitand'''
    p[0] = ExpExpBitAnd(p[1])

def p_exp_bitand_and(p):
    '''exp_bitand : exp_bitand BITAND exp_shift'''
    p[0] = ExpBitAndConcrete(p[1], p[3])

def p_exp_bitand_shift(p):
    '''exp_bitand : exp_shift'''
    p[0] = ExpExpShift(p[1])

def p_exp_shift_lshift(p):
    '''exp_shift : exp_shift LSHIFT exp_add'''
    p[0] = ExpShiftConcrete(p[1], p[2], p[3])

def p_exp_shift_rshift(p):
    '''exp_shift : exp_shift RSHIFT exp_add'''
    p[0] = ExpShiftConcrete(p[1], p[2], p[3])

def p_exp_shift_add(p):
    '''exp_shift : exp_add'''
    p[0] = ExpExpShift(p[1])

def p_exp_add_plus(p):
    '''exp_add : exp_add PLUS exp_mul'''
    p[0] = ExpAddConcrete(p[1], p[2], p[3])

def p_exp_add_minus(p):
    '''exp_add : exp_add MINUS exp_mul'''
    p[0] = ExpAddConcrete(p[1], p[2], p[3])

def p_exp_add_mul(p):
    '''exp_add : exp_mul'''
    p[0] = ExpExpMul(p[1])

def p_exp_mul_times(p):
    '''exp_mul : exp_mul TIMES exp_unary'''
    p[0] = ExpMulConcrete(p[1], p[2], p[3])

def p_exp_mul_divide(p):
    '''exp_mul : exp_mul DIVIDE exp_unary'''
    p[0] = ExpMulConcrete(p[1], p[2], p[3])

def p_exp_mul_modl(p):
    '''exp_mul : exp_mul MODL exp_unary'''
    p[0] = ExpMulConcrete(p[1], p[2], p[3])

def p_exp_mul_unary(p):
    '''exp_mul : exp_unary'''
    p[0] = ExpExpUnary(p[1])

def p_exp_unary_not(p):
    '''exp_unary : LOGNOT exp_unary'''
    p[0] = ExpUnaryNot(p[2])

def p_exp_unary_neg(p):
    '''exp_unary : MINUS exp_unary'''
    p[0] = ExpUnaryNeg(p[2])

def p_exp_unary_primary(p):
    '''exp_unary : exp_primary'''
    p[0] = ExpPrimaryConcrete(p[1])

def p_exp_primary_call(p):
    '''exp_primary : call'''
    p[0] = ExpPrimaryCall(p[1])

def p_exp_primary_num(p):
    '''exp_primary : NUMBER'''
    p[0] = ExpPrimaryNum(p[1])

def p_exp_primary_id(p):
    '''exp_primary : ID'''
    p[0] = ExpPrimaryId(p[1])

def p_exp_primary_string(p):
    '''exp_primary : STRING'''
    p[0] = ExpPrimaryString(p[1])

def p_exp_primary_true(p):
    '''exp_primary : TRUE'''
    p[0] = ExpPrimaryBool(True)

def p_exp_primary_false(p):
    '''exp_primary : FALSE'''
    p[0] = ExpPrimaryBool(False)

def p_exp_primary_paren(p):
    '''exp_primary : LPAREN exp RPAREN'''
    p[0] = ExpPrimaryParen(p[2])

def p_exp_primary_block_exp(p):
    '''exp_primary : LBRACE stmts exp RBRACE'''
    p[0] = ExpPrimaryBlocoExp(p[2], p[3])

def p_exp_primary_block(p):
    '''exp_primary : LBRACE stmts RBRACE'''
    p[0] = ExpPrimaryBloco(p[2])


#CHAMADAS DE FUNÇÃO
def p_call_with_params(p):
    '''call : ID LPAREN args RPAREN'''
    p[0] = CallFuncArgs(p[1], p[3])

def p_call_no_params(p):
    '''call : ID LPAREN RPAREN'''
    p[0] = CallFunc(p[1])

def p_args_single(p):
    '''args : exp'''
    p[0] = ArgsExp(p[1])

def p_args_multi(p):
    '''args : exp COMMA args'''
    p[0] = ArgsExpArgs(p[1], p[3])

def p_type(p):
    '''type : ID'''
    p[0] = TypeID(p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error: unexpected end of file")

def create_parser():
    return yacc.yacc()

def main():
    if len(sys.argv) < 2:
        print("Use: python lexer.py <arquivo_rust.rs>")
        exit(1)
    
    with open(sys.argv[1], 'r') as f:
        sourceCode = f.read()
    the_lexer = create_lexer()
    the_parser = create_parser()

    result = the_parser.parse(sourceCode, lexer=the_lexer)

    print(result)

if __name__ == '__main__':
    main()