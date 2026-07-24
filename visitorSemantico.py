from visitorAbstrato import VisitorAbstrato
from tabelaSimbolos import TabelaSimbolos, Simbolo


class VisitorSemanticoFirst(VisitorAbstrato):

    def __init__(self):
        self.tabela = TabelaSimbolos()

    def visit(self, no):
        return no.accept(self)

    #PROGRAMA
    def visitProgramTopDecl(self, vptd):
        vptd.topdecl.accept(self)

    def visitProgramTopDeclProgram(self, vptdp):
        vptdp.topdecl.accept(self)
        vptdp.program.accept(self)

    def visitTopDeclFuncDecl(self, vtdfd):
        vtdfd.funcdecl.accept(self)

    def visitTopDeclStructDecl(self, vtdsd):
        vtdsd.structdecl.accept(self)

    def visitTopDeclTraitDecl(self, vtdtd):
        vtdtd.traitdecl.accept(self)
    
    def visitTopDeclDecl(self, vtdd):
        vtdd.decl.accept(self)

    # FUNCOES
    def visitFuncDeclSignatureBody(self, vfdsb):
        vfdsb.signature.accept(self)

    def visitSignatureFunc(self, vsf):
        params, tipo_retorno = vsf.signaturei.accept(self)
        simbolo = Simbolo(nome=vsf.id, categoria='funcao', tipo=tipo_retorno, params=params)
        self.tabela.inserir(simbolo)

    def visitSignatureISigP(self, vsigp):
        return vsigp.signaturep.accept(self)

    def visitSignatureISigNP(self, vsignp):
        return vsignp.signaturenp.accept(self)

    def visitSignatureFuncP(self, vsigfp):
        params = vsigfp.sigparams.accept(self)
        tipo_retorno = vsigfp.type.accept(self)
        return params, tipo_retorno

    def visitSignatureFuncPVoid(self, vsigfpv):
        params = vsigfpv.sigparams.accept(self)
        return params, None

    def visitSignatureFuncNP(self, vsigfnp):
        tipo_retorno = vsigfnp.type.accept(self)
        return [], tipo_retorno

    def visitSignatureFuncNPVoid(self, vsigfnpv):
        return [], None

    def visitSigParamsSingle(self, vsp):
        return [vsp.sigparam.accept(self)]

    def visitSigParamsMulti(self, vspm):
        return [vspm.sigparam.accept(self)] + vspm.sigparams.accept(self)

    def visitSigParamConcrete(self, vspc):
        tipo = vspc.type.accept(self)
        return (vspc.id, tipo)

    def visitBodyConcrete(self, vbc):
        pass  

    # STRUCT E TRAIT
    def visitStructDeclConcrete(self, vsdc):
        pass

    def visitStructFieldsSingle(self, vsfs):
        pass

    def visitStructFieldsMulti(self, vsfm):
        pass

    def visitStructFieldConcrete(self, vsfc):
        pass

    def visitTraitDeclConcrete(self, vtdc):
        pass

    def visitTraitBodySingle(self, vtbs):
        pass

    def visitTraitBodyMulti(self, vtbm):
        pass

    def visitTraitSignaturesSignature(self, vtss):
        pass

    def visitTraitSignaturesFuncDecl(self, vtsfd):
        pass

    def visitTraitSignaturesTraitMethod(self, vtstm):
        pass

    def visitTraitMethodConcrete(self, vtmc):
        pass

    def visitTraitSignatureConcrete(self, vtsc):
        pass

    def visitTraitSignaturePSingleP(self, vtspsp):
        pass

    def visitTraitSignaturePSinglePV(self, vtspspv):
        pass

    def visitTraitSignaturePMultiP(self, vtspmp):
        pass

    def visitTraitSignaturePMultiPV(self, vtspmpv):
        pass

    # COMANDOS
    def visitStmtsSingle(self, vss):
        vss.stm.accept(self)

    def visitStmtsMulti(self, vsm):
        vsm.stm.accept(self)
        vsm.stmts.accept(self)

    def visitStmDecl(self, vsd):
        vsd.decl.accept(self)

    def visitStmExp(self, vse):
        vse.exp.accept(self)

    def visitStmIfr(self, vsif):
        vsif.ifr.accept(self)

    def visitStmLoop(self, vsl):
        self.tabela.pushEscopo()
        vsl.stmts.accept(self)
        self.tabela.popEscopo()

    def visitStmWhile(self, vsw):
        pass

    def visitStmReturn(self, vsr):
        pass

    def visitStmBreak(self, vsb):
        pass

    def visitStmContinue(self, vsc):
        pass

    # IF/ELSE
    def visitIfNoElse(self, vifne):
        pass

    def visitIfElse(self, vife):
        pass

    def visitIfElseIfr(self, vifei):
        pass

    # DECLARACOES
    def visitDeclLet(self, vdl):
        if self.tabela.buscarEscopoAtual(vdl.id):
            raise ValueError(f"Erro semântico:\n'{vdl.id}' já declarado neste escopo.")
        self.tabela.inserir(Simbolo(nome=vdl.id, categoria='variavel'))

    def visitDeclMut(self, vdm):
        if self.tabela.buscarEscopoAtual(vdm.id):
            raise ValueError(f"Erro semântico:\n'{vdm.id}' já declarado neste escopo.")
        self.tabela.inserir(Simbolo(nome=vdm.id, categoria='variavel_mut'))

    def visitDeclConst(self, vdc):
        if self.tabela.buscarEscopoAtual(vdc.id):
            raise ValueError(f"Erro semântico:\n'{vdc.id}' já declarado neste escopo.")
        self.tabela.inserir(Simbolo(nome=vdc.id, categoria='const'))

    def visitTypeDeclConcrete(self, vtdc):
        pass

    # EXPRESSOES
    def visitExpAssign(self, vea):
        return vea.exp_assign.accept(self)

    def visitExpAtrib(self, vea):
        if not self.tabela.existe(vea.id):
            raise ValueError(f"Erro semântico:\nVariável '{vea.id}' não foi declarada.")
        return vea.exp.accept(self)

    def visitExpAtribuiSoma(self, vas):
        if not self.tabela.existe(vas.id):
            raise ValueError(f"Erro semântico:\nVariável '{vas.id}' não foi declarada.")
        return vas.exp.accept(self)

    def visitExpAtribuiSubtracao(self, vas):
        if not self.tabela.existe(vas.id):
            raise ValueError(f"Erro semântico:\nVariável '{vas.id}' não foi declarada.")
        return vas.exp.accept(self)

    def visitExpAtribuiMultiplicacao(self, vam):
        if not self.tabela.existe(vam.id):
            raise ValueError(f"Erro semântico:\nVariável '{vam.id}' não foi declarada.")
        return vam.exp.accept(self)

    def visitExpAtribuiDivisao(self, vad):
        if not self.tabela.existe(vad.id):
            raise ValueError(f"Erro semântico:\nVariável '{vad.id}' não foi declarada.")
        return vad.exp.accept(self)

    def visitExpExpOU(self, veu):
        return veu.exp_or.accept(self)

    def visitExpOU(self, veu):
        veu.exp_or.accept(self)
        veu.exp_and.accept(self)

    def visitExpExpE(self, vee):
        return vee.exp_and.accept(self)

    def visitExpE(self, vee):
        vee.exp_and.accept(self)
        vee.exp_rel.accept(self)

    def visitExpExpRel(self, ver):
        return ver.exp_rel.accept(self)

    def visitExpRel(self, ver):
        ver.exp_bitor.accept(self)
        ver.exp_bitor2.accept(self)

    def visitExpExpBitOr(self, vebo):
        return vebo.exp_bitor.accept(self)

    def visitExpBitOr(self, vebo):
        vebo.exp_bitor.accept(self)
        vebo.exp_bitxor.accept(self)

    def visitExpExpBitXor(self, vebx):
        return vebx.exp_bitxor.accept(self)

    def visitExpBitXor(self, vebx):
        vebx.exp_bitxor.accept(self)
        vebx.exp_bitand.accept(self)

    def visitExpExpBitAnd(self, veba):
        return veba.exp_bitand.accept(self)

    def visitExpBitAnd(self, veba):
        veba.exp_bitand.accept(self)
        veba.exp_shift.accept(self)

    def visitExpExpShift(self, ves):
        return ves.exp_shift.accept(self)

    def visitExpShift(self, ves):
        ves.exp_shift.accept(self)
        ves.exp_add.accept(self)

    def visitExpExpAdd(self, vea):
        return vea.exp_add.accept(self)

    def visitExpAdd(self, vea):
        vea.exp_add.accept(self)
        vea.exp_mul.accept(self)

    def visitExpExpMul(self, vem):
        return vem.exp_mul.accept(self)

    def visitExpMul(self, vem):
        vem.exp_mul.accept(self)
        vem.exp_unary.accept(self)

    def visitExpExpUnary(self, veu):
        return veu.exp_unary.accept(self)

    def visitExpUnaryNot(self, venu):
        return venu.exp_unary.accept(self)

    def visitExpUnaryNeg(self, venu):
        return venu.exp_unary.accept(self)

    def visitExpPrimary(self, vep):
        return vep.exp_primary.accept(self)

    def visitExpPrimaryCall(self, vepc):
        return vepc.call.accept(self)

    def visitExpPrimaryNum(self, vepn):
        pass

    def visitExpPrimaryId(self, vepi):
        if not self.tabela.existe(vepi.id):
            raise ValueError(f"Erro semântico:\nIdentificador '{vepi.id}' não foi declarado.")

    def visitExpPrimaryString(self, veps):
        pass

    def visitExpPrimaryBool(self, vepb):
        pass

    def visitExpPrimaryParen(self, vepp):
        return vepp.exp.accept(self)

    def visitExpPrimaryBlocoExp(self, vepbe):
        self.tabela.pushEscopo()
        vepbe.stmts.accept(self)
        vepbe.exp.accept(self)
        self.tabela.popEscopo()

    def visitExpPrimaryBloco(self, vepb):
        self.tabela.pushEscopo()
        vepb.stmts.accept(self)
        self.tabela.popEscopo()

    # CHAMADAS DE FUNCAO
    def visitCallFuncArgs(self, vcfa):
        pass

    def visitCallFunc(self, vcf):
        pass

    def visitArgsExpArgs(self, vaea):
        pass

    def visitArgsExp(self, vae):
        pass

    # TIPO
    def visitTypeID(self, vtid):
        return vtid.type


class VisitorSemanticoSecond(VisitorAbstrato):

    def __init__(self, tabela):
        self.tabela = tabela

    def visit(self, no):
        return no.accept(self)

    #PROGRAMA
    def visitProgramTopDecl(self, vptd):
        vptd.topdecl.accept(self)

    def visitProgramTopDeclProgram(self, vptdp):
        vptdp.topdecl.accept(self)
        vptdp.program.accept(self)

    def visitTopDeclFuncDecl(self, vtdfd):
        vtdfd.funcdecl.accept(self)

    def visitTopDeclStructDecl(self, vtdsd):
        vtdsd.structdecl.accept(self)

    def visitTopDeclTraitDecl(self, vtdtd):
        vtdtd.traitdecl.accept(self)

    def visitTopDeclDecl(self, vtdd):
        vtdd.decl.accept(self)

    # FUNCOES
    def visitFuncDeclSignatureBody(self, vfdsb):
        vfdsb.pushEscopo()
        vfdsb.signature.accept(self)
        vfdsb.body.accept(self)

    def visitSignatureFunc(self, vsf):
        Simbolo = self.tabela.buscar(vsf.id)
        for param in Simbolo.params:
            a=Simbolo(param[0], 'variavel', None, None)
        
    def visitSignatureISigP(self, vsigp):
        return vsigp.signaturep.accept(self)


    def visitSignatureISigNP(self, vsignp):
        return vsignp.signaturenp.accept(self)

    def visitSignatureFuncP(self, vsigfp):
        return vsigfp.sigparams.accept(self), vsigfp.type.accept(self)

    def visitSignatureFuncPVoid(self, vsigfpv):
        return vsigfpv.sigparams.accept(self), None

    def visitSignatureFuncNP(self, vsigfnp):
        return [], vsigfnp.type.accept(self)

    def visitSignatureFuncNPVoid(self, vsigfnpv):
        return [], None

    def visitSigParamsSingle(self, vsp):
        return [vsp.sigparam.accept(self)]

    def visitSigParamsMulti(self, vspm):
        return [vspm.sigparam.accept(self)] + vspm.sigparams.accept(self)

    def visitSigParamConcrete(self, vspc):
        tipo = vspc.type.accept(self)
        return (vspc.id, tipo)

    def visitBodyConcrete(self, vbc):
        if (vbc.stmts is not None):
            vbc.stmts.accept(self)

    # STRUCT E TRAIT
    def visitStructDeclConcrete(self, vsdc):
        pass

    def visitStructFieldsSingle(self, vsfs):
        pass

    def visitStructFieldsMulti(self, vsfm):
        pass

    def visitStructFieldConcrete(self, vsfc):
        pass

    def visitTraitDeclConcrete(self, vtdc):
        pass

    def visitTraitBodySingle(self, vtbs):
        pass

    def visitTraitBodyMulti(self, vtbm):
        pass

    def visitTraitSignaturesSignature(self, vtss):
        pass

    def visitTraitSignaturesFuncDecl(self, vtsfd):
        pass

    def visitTraitSignaturesTraitMethod(self, vtstm):
        pass

    def visitTraitMethodConcrete(self, vtmc):
        pass

    def visitTraitSignatureConcrete(self, vtsc):
        pass

    def visitTraitSignaturePSingleP(self, vtspsp):
        pass

    def visitTraitSignaturePSinglePV(self, vtspspv):
        pass

    def visitTraitSignaturePMultiP(self, vtspmp):
        pass

    def visitTraitSignaturePMultiPV(self, vtspmpv):
        pass

    # COMANDOS
    def visitStmtsSingle(self, vss):
        vss.stm.accept(self)

    def visitStmtsMulti(self, vsm):
        vsm.stm.accept(self)
        vsm.stmts.accept(self)

    def visitStmDecl(self, vsd):
        vsd.decl.accept(self)

    def visitStmExp(self, vse):
        vse.exp.accept(self)

    def visitStmIfr(self, vsif):
        vsif.ifr.accept(self)

    def visitStmLoop(self, vsl):
        self.tabela.pushEscopo()
        vsl.stmts.accept(self)
        self.tabela.popEscopo()

    def visitStmWhile(self, vsw):
        pass

    def visitStmReturn(self, vsr):
        pass

    def visitStmBreak(self, vsb):
        pass

    def visitStmContinue(self, vsc):
        pass

    # IF/ELSE
    def visitIfNoElse(self, vifne):
        pass

    def visitIfElse(self, vife):
        pass

    def visitIfElseIfr(self, vifei):
        pass

    # DECLARACOES
    def visitDeclLet(self, vdl):
        if self.tabela.buscarEscopoAtual(vdl.id):
            raise ValueError(f"Erro semântico:\n'{vdl.id}' já declarado neste escopo.")
        self.tabela.inserir(Simbolo(nome=vdl.id, categoria='variavel'))

    def visitDeclMut(self, vdm):
        if self.tabela.buscarEscopoAtual(vdm.id):
            raise ValueError(f"Erro semântico:\n'{vdm.id}' já declarado neste escopo.")
        self.tabela.inserir(Simbolo(nome=vdm.id, categoria='variavel_mut'))

    def visitDeclConst(self, vdc):
        if self.tabela.buscarEscopoAtual(vdc.id):
            raise ValueError(f"Erro semântico:\n'{vdc.id}' já declarado neste escopo.")
        self.tabela.inserir(Simbolo(nome=vdc.id, categoria='const'))

    def visitTypeDeclConcrete(self, vtdc):
        pass

    # EXPRESSOES
    def visitExpAssign(self, vea):
        return vea.exp_assign.accept(self)

    def visitExpAtrib(self, vea):
        if not self.tabela.existe(vea.id):
            raise ValueError(f"Erro semântico:\nVariável '{vea.id}' não foi declarada.")
        return vea.exp.accept(self)

    def visitExpAtribuiSoma(self, vas):
        if not self.tabela.existe(vas.id):
            raise ValueError(f"Erro semântico:\nVariável '{vas.id}' não foi declarada.")
        return vas.exp.accept(self)

    def visitExpAtribuiSubtracao(self, vas):
        if not self.tabela.existe(vas.id):
            raise ValueError(f"Erro semântico:\nVariável '{vas.id}' não foi declarada.")
        return vas.exp.accept(self)

    def visitExpAtribuiMultiplicacao(self, vam):
        if not self.tabela.existe(vam.id):
            raise ValueError(f"Erro semântico:\nVariável '{vam.id}' não foi declarada.")
        return vam.exp.accept(self)

    def visitExpAtribuiDivisao(self, vad):
        if not self.tabela.existe(vad.id):
            raise ValueError(f"Erro semântico:\nVariável '{vad.id}' não foi declarada.")
        return vad.exp.accept(self)

    def visitExpExpOU(self, veu):
        return veu.exp_or.accept(self)

    def visitExpOU(self, veu):
        veu.exp_or.accept(self)
        veu.exp_and.accept(self)

    def visitExpExpE(self, vee):
        return vee.exp_and.accept(self)

    def visitExpE(self, vee):
        vee.exp_and.accept(self)
        vee.exp_rel.accept(self)

    def visitExpExpRel(self, ver):
        return ver.exp_rel.accept(self)

    def visitExpRel(self, ver):
        ver.exp_bitor.accept(self)
        ver.exp_bitor2.accept(self)

    def visitExpExpBitOr(self, vebo):
        return vebo.exp_bitor.accept(self)

    def visitExpBitOr(self, vebo):
        vebo.exp_bitor.accept(self)
        vebo.exp_bitxor.accept(self)

    def visitExpExpBitXor(self, vebx):
        return vebx.exp_bitxor.accept(self)

    def visitExpBitXor(self, vebx):
        vebx.exp_bitxor.accept(self)
        vebx.exp_bitand.accept(self)

    def visitExpExpBitAnd(self, veba):
        return veba.exp_bitand.accept(self)

    def visitExpBitAnd(self, veba):
        veba.exp_bitand.accept(self)
        veba.exp_shift.accept(self)

    def visitExpExpShift(self, ves):
        return ves.exp_shift.accept(self)

    def visitExpShift(self, ves):
        ves.exp_shift.accept(self)
        ves.exp_add.accept(self)

    def visitExpExpAdd(self, vea):
        return vea.exp_add.accept(self)

    def visitExpAdd(self, vea):
        vea.exp_add.accept(self)
        vea.exp_mul.accept(self)

    def visitExpExpMul(self, vem):
        return vem.exp_mul.accept(self)

    def visitExpMul(self, vem):
        vem.exp_mul.accept(self)
        vem.exp_unary.accept(self)

    def visitExpExpUnary(self, veu):
        return veu.exp_unary.accept(self)

    def visitExpUnaryNot(self, venu):
        return venu.exp_unary.accept(self)

    def visitExpUnaryNeg(self, venu):
        return venu.exp_unary.accept(self)

    def visitExpPrimary(self, vep):
        return vep.exp_primary.accept(self)

    def visitExpPrimaryCall(self, vepc):
        return vepc.call.accept(self)

    def visitExpPrimaryNum(self, vepn):
        pass

    def visitExpPrimaryId(self, vepi):
        if not self.tabela.existe(vepi.id):
            raise ValueError(f"Erro semântico:\nIdentificador '{vepi.id}' não foi declarado.")

    def visitExpPrimaryString(self, veps):
        pass

    def visitExpPrimaryBool(self, vepb):
        pass

    def visitExpPrimaryParen(self, vepp):
        return vepp.exp.accept(self)

    def visitExpPrimaryBlocoExp(self, vepbe):
        self.tabela.pushEscopo()
        vepbe.stmts.accept(self)
        vepbe.exp.accept(self)
        self.tabela.popEscopo()

    def visitExpPrimaryBloco(self, vepb):
        self.tabela.pushEscopo()
        vepb.stmts.accept(self)
        self.tabela.popEscopo()

    # CHAMADAS DE FUNCAO
    def visitCallFuncArgs(self, vcfa):
        pass

    def visitCallFunc(self, vcf):
        pass

    def visitArgsExpArgs(self, vaea):
        pass

    def visitArgsExp(self, vae):
        pass

    # TIPO
    def visitTypeID(self, vtid):
        return vtid.type
