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
    def ___init___(self, id, signaturei):
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
    