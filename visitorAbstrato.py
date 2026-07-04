from abc import ABC, abstractmethod

class VisitorAbstrato(ABC):
    @abstractmethod
    def visit(self, no):
        pass

#PROGRAMA
    @abstractmethod
    def visitProgramTopDecl(self, vptd):
        pass

    @abstractmethod
    def visitProgramTopDeclProgram(self, vptdp):
        pass

    @abstractmethod
    def visitTopDeclFuncDecl(self, vtdfd):
        pass

    @abstractmethod
    def visitTopDeclStructDecl(self, vtdsd):
        pass

    @abstractmethod
    def visitTopDeclTraitDecl(self, vtdtd):
        pass

#FUNÇÕES
    @abstractmethod
    def visitFuncDeclSignatureBody(self, vfdsb):
        pass

    @abstractmethod
    def visitSignatureFunc(self, vsf):
        pass

    @abstractmethod
    def visitSignatureISigP(self, vsigp):
        pass

    @abstractmethod
    def visitSignatureISigNP(self, vsignp):
        pass

    @abstractmethod
    def visitSignatureFuncP(self, vsigfp):
        pass

    @abstractmethod
    def visitSignatureFuncPVoid(self, vsigfpv):
        pass

    @abstractmethod
    def visitSignatureFuncNP(self, vsigfnp):
        pass

    @abstractmethod
    def visitSignatureFuncNPVoid(self, vsigfnpv):
        pass

    @abstractmethod
    def visitSigParamsSingle(self, vsp):
        pass

    @abstractmethod
    def visitSigParamsMulti(self, vspm):
        pass

    @abstractmethod
    def visitSigParamConcrete(self, vspc):
        pass

    @abstractmethod
    def visitBodyConcrete(self, vbc):
        pass

#STRUCT E TRAIT

    @abstractmethod
    def visitStructDeclConcrete(self, vsdc):
        pass

    @abstractmethod
    def visitStructFieldsSingle(self, vsfs):
        pass

    @abstractmethod
    def visitStructFieldsMulti(self, vsfm):
        pass

    @abstractmethod
    def visitStructFieldConcrete(self, vsfc):
        pass

    @abstractmethod
    def visitTraitDeclConcrete(self, vtdc):
        pass

    @abstractmethod
    def visitTraitBodySingle(self, vtbs):
        pass

    @abstractmethod
    def visitTraitBodyMulti(self, vtbm):
        pass

    @abstractmethod
    def visitTraitSignaturesSignature(self, vtss):
        pass

    @abstractmethod
    def visitTraitSignaturesFuncDecl(self, vtsfd):
        pass

    @abstractmethod
    def visitTraitSignaturesTraitMethod(self, vtstm):
        pass
    
    @abstractmethod
    def visitTraitMethodConcrete(self, vtmc):
        pass

    @abstractmethod
    def visitTraitSignatureConcrete(self, vtsc):
        pass
    
    @abstractmethod
    def visitTraitSignaturePSingleP(self, vtspsp):
        pass

    @abstractmethod
    def visitTraitSignaturePSinglePV(self, vtspspv):
        pass
    
    @abstractmethod
    def visitTraitSignaturePMultiP(self, vtspmp):
        pass

    @abstractmethod
    def visitTraitSignaturePMultiPV(self, vtspmpv):
        pass
#COMANDOS
    @abstractmethod
    def visitStmtsSingle(self, vss):
        pass

    @abstractmethod
    def visitStmtsMulti(self, vsm):
        pass

    @abstractmethod
    def visitStmDecl(self, vsd):
        pass

    @abstractmethod
    def visitStmExp(self, vse):
        pass

    @abstractmethod
    def visitStmIfr(self, vsif):
        pass

    @abstractmethod
    def visitStmLoop(self, vsl):
        pass

    @abstractmethod
    def visitStmWhile(self, vsw):
        pass

    @abstractmethod
    def visitStmReturn(self, vsr):
        pass

    @abstractmethod
    def visitStmBreak(self, vsb):
        pass

    @abstractmethod
    def visitStmContinue(self, vsc):
        pass

    @abstractmethod
    def visitIfNoElse(self, vifne):
        pass

    @abstractmethod
    def visitIfElse(self, vife):
        pass

    @abstractmethod
    def visitIfElseIfr(self, vifei):
        pass

#DECLARAÇÕES
    @abstractmethod
    def visitDeclLet(self, vdl):
        pass

    @abstractmethod
    def visitDeclMut(self, vdm):
        pass

    @abstractmethod
    def visitDeclConst(self, vdc):
        pass

    @abstractmethod
    def visitTypeDeclConcrete(self, vtdc):
        pass

#EXPRESSÕES
    @abstractmethod
    def visitExpAssign(self, vea):
        pass

    @abstractmethod
    def visitExpAtrib(self, vea):
        pass

    @abstractmethod
    def visitExpAtribuiSoma(self, vas):
        pass

    @abstractmethod
    def visitExpAtribuiSubtracao(self, vas):
        pass

    @abstractmethod
    def visitExpAtribuiMultiplicacao(self, vam):
        pass

    @abstractmethod
    def visitExpAtribuiDivisao(self, vad):
        pass

    @abstractmethod
    def visitExpExpOU(self, veu):
        pass

    @abstractmethod
    def visitExpOU(self, veu):
        pass

    @abstractmethod
    def visitExpExpE(self, vee):
        pass

    @abstractmethod
    def visitExpE(self, vee):
        pass

    @abstractmethod
    def visitExpExpRel(self, ver):
        pass

    @abstractmethod
    def visitExpRel(self, ver):
        pass

    @abstractmethod
    def visitExpExpBitOr(self, vebo):
        pass

    @abstractmethod
    def visitExpBitOr(self, vebo):
        pass

    @abstractmethod
    def visitExpExpBitXor(self, vebx):
        pass

    @abstractmethod
    def visitExpBitXor(self, vebx):
        pass

    @abstractmethod
    def visitExpExpBitAnd(self, veba):
        pass

    @abstractmethod
    def visitExpBitAnd(self, veba):
        pass

    @abstractmethod
    def visitExpExpShift(self, ves):
        pass

    @abstractmethod
    def visitExpShift(self, ves):
        pass

    @abstractmethod
    def visitExpExpAdd(self, vea):
        pass

    @abstractmethod
    def visitExpAdd(self, vea):
        pass

    @abstractmethod
    def visitExpExpMul(self, vem):
        pass

    @abstractmethod
    def visitExpMul(self, vem):
        pass

    @abstractmethod
    def visitExpExpUnary(self, veu):
        pass

    @abstractmethod
    def visitExpUnaryNot(self, venu):
        pass

    @abstractmethod
    def visitExpUnaryNeg(self, venu):
        pass

    @abstractmethod
    def visitExpPrimary(self, vep):
        pass

    @abstractmethod
    def visitExpPrimaryCall(self, vepc):
        pass

    @abstractmethod
    def visitExpPrimaryNum(self, vepn):
        pass

    @abstractmethod
    def visitExpPrimaryId(self, vepi):
        pass

    @abstractmethod
    def visitExpPrimaryString(self, veps):
        pass

    @abstractmethod
    def visitExpPrimaryBool(self, vepb):
        pass

    @abstractmethod
    def visitExpPrimaryParen(self, vepp):
        pass

    @abstractmethod
    def visitExpPrimaryBlocoExp(self, vepbe):
        pass

    @abstractmethod
    def visitExpPrimaryBloco(self, vepb):
        pass

#CHAMADAS DE FUNÇÃO
    @abstractmethod
    def visitCallFuncArgs(self, vcfa):
        pass

    @abstractmethod
    def visitCallFunc(self, vcf):
        pass

    @abstractmethod
    def visitArgsExpArgs(self, vaea):
        pass

    @abstractmethod
    def visitArgsExp(self, vae):
        pass

#TIPO
    @abstractmethod
    def visitTypeID(self, vtid):
        pass