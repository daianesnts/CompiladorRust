from sintaxeAbstrataABC import *


#PROGRAMA
class ProgramTopDecl(Program):
    def __init__(self, topdecl):
        self.topdecl = topdecl

    def accept(self, visitor):
        return visitor.visitProgramTopDecl(self)
    
class ProgramTopDeclProgram(Program):
    def __init__(self, topdecl, program):
        self.topdecl = topdecl
        self.program = program

    def accept(self, visitor):
        return visitor.visitProgramTopDeclProgram(self)
    
class TopDeclFuncDecl(TopDecl):
    def __init__(self, funcdecl):
        self.funcdecl = funcdecl

    def accept(self, visitor):
        return visitor.visitTopDeclFuncDecl(self)

class TopDeclStructDecl(TopDecl):
    def __init__(self, structdecl):
        self.structdecl = structdecl

    def accept(self, visitor):
        return visitor.visitTopDeclStructDecl(self)

class TopDeclTraitDecl(TopDecl):
    def __init__(self, traitdecl):
        self.traitdecl = traitdecl

    def accept(self, visitor):
        return visitor.visitTopDeclTraitDecl(self)


#FUNCOES
class FuncDeclSignatureBody(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body

    def accept(self, visitor):
        return visitor.visitFuncDeclSignatureBody(self)
    
class SignatureFunc(Signature):
    def __init__(self, id, signaturei):
        self.id = id
        self.signaturei = signaturei

    def accept(self, visitor):
        return visitor.visitSignatureFunc(self)
    
class SignatureISigP(SignatureI):
    def __init__(self, signaturep):
        self.signaturep = signaturep

    def accept(self, visitor):
        return visitor.visitSignatureISigP(self)
    
class SignatureISigNP(SignatureI):
    def __init__(self, signaturenp):
        self.signaturenp = signaturenp

    def accept(self, visitor):
        return visitor.visitSignatureISigNP(self)
    
class SignatureFuncP(SignatureP):
    def __init__(self, sigparams, type):
        self.sigparams = sigparams
        self.type = type

    def accept(self, visitor):
        return visitor.visitSignatureFuncP(self)
    
class SignatureFuncPVoid(SignatureP):
    def __init__(self, sigparams):
        self.sigparams = sigparams

    def accept(self, visitor):
        return visitor.visitSignatureFuncPVoid(self)
    
class SignatureFuncNP(SignatureNP):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        return visitor.visitSignatureFuncNP(self)
    
class SignatureFuncNPVoid(SignatureNP):
    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitSignatureFuncNPVoid(self)
    
class SigParamsSingle(SigParams):
    def __init__(self, sigparam):
        self.sigparam = sigparam

    def accept(self, visitor):
        return visitor.visitSigParamsSingle(self)
    
class SigParamsMulti(SigParams):
    def __init__(self, sigparam, sigparams):
        self.sigparam = sigparam
        self.sigparams = sigparams

    def accept(self, visitor):
        return visitor.visitSigParamsMulti(self)
    
class SigParam(SigParam):
    def __init__(self, id, type):
        self.id = id
        self.type = type

    def accept(self, visitor):
        return visitor.visitSigParam(self)
    
class BodyConcrete(Body):
    def __init__(self, stmts):
        self.stmts = stmts

    def accept(self, visitor):
        return visitor.visitBodyConcrete(self)


#STRUCT E TRAIT  
class StructDeclConcrete(StructDecl):
    def __init__(self, id, structfields):
        self.id = id
        self.structfields = structfields

    def accept(self, visitor):
        return visitor.visitStructDeclConcrete(self)

class StructFieldsField(StructFields):
    def __init__(self, structfield):
        self.structfield = structfield

    def accept(self, visitor):
        return visitor.visitStructFieldsField(self)
    
class StructFieldsMulti(StructFields):
    def __init__(self, structfield, structfields):
        self.structfield = structfield
        self.structfields = structfields

    def accept(self, visitor):
        return visitor.visitStructFieldsMulti(self)
    
class StructFieldConcrete(StructField):
    def __init__(self, id, type):
        self.id = id
        self.type = type

    def accept(self, visitor):
        return visitor.visitStructFieldConcrete(self)
    
class TraitDeclConcrete(TraitDecl):
    def __init__(self, id, traitbody):
        self.id = id
        self.traitbody = traitbody

    def accept(self, visitor):
        return visitor.visitTraitDeclConcrete(self)

class TraitBodySingle(TraitBody):
    def __init__(self, signature):
        self.signature = signature
        

    def accept(self, visitor):
        return visitor.visitTraitBodySingle(self)
    
class TraitBodyMulti(TraitBody):
    def __init__(self, signature, traitbody):
        self.signature = signature
        self.traitbody = traitbody

    def accept(self, visitor):
        return visitor.visitTraitBodyMulti(self)
    

#COMANDOS
class StmtsSingle(Stmts):
    def __init__(self, stm):
        self.stm = stm

    def accept(self, visitor):
        return visitor.visitStmtsSingle(self)

class StmtsMulti(Stmts):
    def __init__(self, stmts, stm):
        self.stmts = stmts
        self.stm = stm

    def accept(self, visitor):
        return visitor.visitStmtsMulti(self)
    
class StmDecl(Stm):
    def __init__(self, decl):
        self.decl = decl

    def accept(self, visitor):
        return visitor.visitStmDecl(self)
    
class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmExp(self)
    
class StmIfr(Stm):
    def __init__(self, ifr):
        self.ifr = ifr

    def accept(self, visitor):
        return visitor.visitStmIfr(self)
    
class StmLoop(Stm):
    def __init__(self, stmts):
        self.stmts = stmts

    def accept(self, visitor):
        return visitor.visitStmLoop(self)
    
class StmWhile(Stm):
    def __init__(self, exp, stmts):
        self.exp = exp
        self.stmts = stmts

    def accept(self, visitor):
        return visitor.visitStmWhile(self)
    
class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmReturn(self)
    
class StmBreak(Stm):
    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitStmBreak(self)
    
class StmContinue(Stm):
    def __init__(self):
        pass

    def accept(self, visitor):
        return visitor.visitStmContinue(self)
    
class IfNoElse(Ifr):
    def __init__(self, exp, stmts):
        self.exp = exp
        self.stmts = stmts

    def accept(self, visitor):
        return visitor.visitIfNoElse(self)
    
class IfElse(Ifr):
    def __init__(self, exp, stmts, stmtselse):
        self.exp = exp
        self.stmtsif = stmts
        self.stmtselse = stmtselse

    def accept(self, visitor):
        return visitor.visitIfElse(self)
    
class IfElseIf(Ifr):
    def __init__(self, exp, stmts, ifr):
        self.exp = exp
        self.stmtsif = stmts
        self.ifr = ifr

    def accept(self, visitor):
        return visitor.visitIfElseIf(self)
    

#DECLARACOES
class DeclLet(Decl):
    def __init__(self, id, typedecl, exp):
        self.id = id
        self.typedecl = typedecl
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitDeclLet(self)
    
class DeclMut(Decl):
    def __init__(self, id, typedecl, exp):
        self.id = id
        self.typedecl = typedecl
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitDeclMut(self)
    
class DeclCons(Decl):
    def __init__(self, id, type, exp):
        self.id = id
        self.type = type
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitDeclConst(self)
    
class DeclExp(Decl):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitDeclExp(self)
    
class TypeDeclConcrete(TypeDecl):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        return visitor.visitTypeDeclConcrete(self) 
    

#EXPRESSOES
class ExpAssign(Exp):
    def __init__(self, exp_assign):
        self.exp_assign = exp_assign

    def accept(self, visitor):
        return visitor.visitExpAssign(self)
    
class ExpAtrib(ExpAssign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpAtrib(self)
    
class ExpAtribuiSoma(ExpAssign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpAtribuiSoma(self)
    
class ExpAtribuiSubtracao(ExpAssign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpAtribuiSubtracao(self)
    
class ExpAtribuiMultiplicacao(ExpAssign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpAtribuiMultiplicacao(self)  

class ExpAtribuiDivisao(ExpAssign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpAtribuiDivisao(self) 

class ExpExpOU(ExpAssign):
    def __init__(self, exp_or):
        self.exp_or = exp_or

    def accept(self, visitor):
        return visitor.visitExpOU(self)
    
class ExpOU(ExpOr):
    def __init__(self, exp_or, exp_and):
        self.exp_or = exp_or
        self.exp_and = exp_and

    def accept(self, visitor):
        return visitor.visitExpOU(self)
    
class ExpExpE(ExpOr):
    def __init__(self, exp_and):
        self.exp_and = exp_and

    def accept(self, visitor):
        return visitor.visitExpE(self)
    
class ExpE(ExpAnd):
    def __init__(self, exp_and, exp_rel):
        self.exp_and = exp_and
        self.exp_eq = exp_rel

    def accept(self, visitor):
        return visitor.visitExpE(self)
    
class ExpExpRel(ExpAnd):
    def __init__(self, exp_rel):
        self.exp_rel = exp_rel

    def accept(self, visitor):
        return visitor.visitExpExpRel(self)

class ExpRel(ExpRel):
    def __init__(self, exp_bitor, op, exp_bitor2):
        self.exp_bitor = exp_bitor
        self.op = op
        self.exp_bitor2 = exp_bitor2

    def accept(self, visitor):
        return visitor.visitExpRel(self)
    
class ExpExpBitor(ExpRel):
    def __init__(self, exp_bitor):
        self.exp_bitor = exp_bitor

    def accept(self, visitor):
        return visitor.visitExpExpBitor(self)

class ExpBitOr(ExpBitOr):
    def __init__(self, exp_bitor, exp_bitxor):
        self.exp_bitor = exp_bitor
        self.exp_bitxor = exp_bitxor

    def accept(self, visitor):
        return visitor.visitExpBitOr(self)

class ExpExpBitXor(ExpBitOr):
    def __init__(self, exp_bitxor):
        self.exp_bitxor = exp_bitxor

    def accept(self, visitor):
        return visitor.visitExpExpBitXor(self)
    
class ExpBitXor(ExpBitXor):
    def __init__(self, exp_bitxor, exp_bitand):
        self.exp_bitxor = exp_bitxor
        self.exp_bitand = exp_bitand

    def accept(self, visitor):
        return visitor.visitExpBitXor(self)

class ExpExpBitAnd(ExpBitXor):
    def __init__(self, exp_bitand):
        self.exp_bitand = exp_bitand

    def accept(self, visitor):
        return visitor.visitExpExpBitAnd(self)

class ExpBitAnd(ExpBitAnd):
    def __init__(self, exp_bitand, exp_shift):
        self.exp_bitand = exp_bitand
        self.exp_shift = exp_shift

    def accept(self, visitor):
        return visitor.visitExpBitAnd(self)

class ExpExpShift(ExpBitAnd):
    def __init__(self, exp_shift):
        self.exp_shift = exp_shift

    def accept(self, visitor):
        return visitor.visitExpExpShift(self)

class ExpShift(ExpShift):
    def __init__(self, exp_shift, op, exp_add):
        self.exp_shift = exp_shift
        self.op = op
        self.exp_add = exp_add

    def accept(self, visitor):
        return visitor.visitExpShift(self)

class ExpExpAdd(ExpShift):
    def __init__(self, exp_add):
        self.exp_add = exp_add

    def accept(self, visitor):
        return visitor.visitExpExpAdd(self)

class ExpAdd(ExpAdd):
    def __init__(self, exp_add, op, exp_mul):
        self.exp_add = exp_add
        self.op = op
        self.exp_mul = exp_mul

    def accept(self, visitor):
        return visitor.visitExpAdd(self)

class ExpExpMul(ExpAdd):
    def __init__(self, exp_mul):
        self.exp_mul = exp_mul

    def accept(self, visitor):
        return visitor.visitExpExpMul(self)

class ExpMul(ExpMul):
    def __init__(self, exp_mul, op, exp_unary):
        self.exp_mul = exp_mul
        self.op = op
        self.exp_unary = exp_unary

    def accept(self, visitor):
        return visitor.visitExpMul(self)

class ExpExpUnary(ExpMul):
    def __init__(self, exp_unary):
        self.exp_unary = exp_unary

    def accept(self, visitor):
        return visitor.visitExpExpUnary(self)

class ExpUnaryNot(ExpUnary):
    def __init__(self, exp_unary):
        self.exp_unary = exp_unary

    def accept(self, visitor):
        return visitor.visitExpUnaryNot(self)

class ExpUnaryNeg(ExpUnary):
    def __init__(self, exp_unary):
        self.exp_unary = exp_unary

    def accept(self, visitor):
        return visitor.visitExpUnaryNeg(self)

class ExpPrimary(ExpUnary):
    def __init__(self, exp_primary):
        self.exp_primary = exp_primary

    def accept(self, visitor):
        return visitor.visitExpPrimary(self)

class ExpPrimaryNum(ExpPrimary):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitExpPrimaryNum(self)

class ExpPrimaryId(ExpPrimary):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitExpPrimaryId(self)

class ExpPrimaryBool(ExpPrimary):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitExpPrimaryBool(self)

class ExpPrimaryParen(ExpPrimary):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpPrimaryParen(self)

class ExpPrimaryBlocoExp(ExpPrimary):
    def __init__(self, stmts, exp):
        self.stmts = stmts
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitExpPrimaryBlocoExp(self)

class ExpPrimaryBloco(ExpPrimary):
    def __init__(self, stmts):
        self.stmts = stmts

    def accept(self, visitor):
        return visitor.visitExpPrimaryBloco(self)
    
    
#CHAMADAS DE FUNÇÃO
class CallFuncParams(Call):
    def __init__(self, id, params):
        self.id = id
        self.params = params 

    def accept(self, visitor):
        return visitor.visitCallFunc(self)
    
class CallFunc(Call):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitCallFunc(self)

class ParamExpParams(Param):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params

    def accept(self, visitor):
        return visitor.visitParamExpParams(self)
    
class ParamExp(Param):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitParamExp(self)
