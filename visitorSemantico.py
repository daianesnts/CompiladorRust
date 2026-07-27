from visitorAbstrato import VisitorAbstrato
import tabelaSimbolos as ts

def coercao(tipo1, tipo2):
    if tipo1 == tipo2 and tipo1 in ts.SignedNumber + ts.UnsignedNumber:
        return tipo1
    if tipo1 in ts.SignedNumber and tipo2 in ts.SignedNumber:
        return ts.SignedNumber[max(ts.SignedNumber.index(tipo1), ts.SignedNumber.index(tipo2))]
    if tipo1 in ts.UnsignedNumber and tipo2 in ts.UnsignedNumber:
        return ts.UnsignedNumber[max(ts.UnsignedNumber.index(tipo1), ts.UnsignedNumber.index(tipo2))]
    if (tipo1 in ts.SignedNumber and tipo2 in ts.UnsignedNumber) or (tipo1 in ts.UnsignedNumber and tipo2 in ts.SignedNumber):
        raise ValueError(f"Erro semântico:\nNão é possível realizar operações entre tipos '{tipo1}' e '{tipo2}'.")
    raise ValueError(f"Erro semântico:\nTipos incompatíveis: '{tipo1}' e '{tipo2}'.")

def atribuicaoValida(simboloEsq, simboloDir):
    if simboloEsq.tipo == simboloDir.tipo:
        return True
    if simboloEsq.tipo in ts.SignedNumber and simboloDir.tipo in ts.SignedNumber:
        return ts.SignedNumber.index(simboloDir.tipo) <= ts.SignedNumber.index(simboloEsq.tipo)
    if simboloEsq.tipo in ts.UnsignedNumber and simboloDir.tipo in ts.UnsignedNumber:
        return ts.UnsignedNumber.index(simboloDir.tipo) <= ts.UnsignedNumber.index(simboloEsq.tipo)
    return False

class VisitorSemanticoFirst(VisitorAbstrato):

    def __init__(self):
        self.tabela = ts.TabelaSimbolos()
        self.tabela.inserir(
            ts.Simbolo(
                nome='println',
                categoria='funcao',
                tipo=None,
                params=[("printable", [ts.I32, ts.STR])]
            )
        )

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
    
    def visitTopDeclDeclStatic(self, vtdds):
        vtdds.declstatic.accept(self)

    # FUNCOES
    def visitFuncDeclSignatureBody(self, vfdsb):
        vfdsb.signature.accept(self)

    def visitSignatureFunc(self, vsf):
        params, tipo_retorno = vsf.signaturei.accept(self)
        simbolo = ts.Simbolo(nome=vsf.id, categoria='funcao', tipo=tipo_retorno, params=params)
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
        self.tabela.inserir(ts.Simbolo(nome=vdl.id, categoria='variavel'))

    def visitDeclMut(self, vdm):
        if self.tabela.buscarEscopoAtual(vdm.id):
            raise ValueError(f"Erro semântico:\n'{vdm.id}' já declarado neste escopo.")
        self.tabela.inserir(ts.Simbolo(nome=vdm.id, categoria='variavel_mut'))

    def visitDeclStatic(self, vds):
        if self.tabela.buscarEscopoAtual(vds.id):
            raise ValueError(f"Erro semântico:\n'{vds.id}' já declarado neste escopo.")
        self.tabela.inserir(ts.Simbolo(nome=vds.id, categoria='static', tipo=vds.type.accept(self)))

    def visitDeclConst(self, vdc):
        if self.tabela.buscarEscopoAtual(vdc.id):
            raise ValueError(f"Erro semântico:\n'{vdc.id}' já declarado neste escopo.")
        self.tabela.inserir(ts.Simbolo(nome=vdc.id, categoria='const'))

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

    def visitTopDeclDeclStatic(self, vtdds):
        pass

    # FUNCOES
    def visitFuncDeclSignatureBody(self, vfdsb):
        local_var = vfdsb.signature.accept(self)
        self.tabela.pushEscopo()
        if len(local_var) > 0:
            for var in local_var:
                self.tabela.inserir(var)
        vfdsb.body.accept(self)
        self.tabela.popEscopo()

    def visitSignatureFunc(self, vsf):
        func_simbolo = self.tabela.buscar(vsf.id)
        local_var = []
        for param in func_simbolo.params:
            local_var.append(ts.Simbolo(nome=param[0], categoria='variavel', tipo=param[1]))
        return local_var

    def visitSignatureISigP(self, vsigp):
        pass

    def visitSignatureISigNP(self, vsignp):
        pass

    def visitSignatureFuncP(self, vsigfp):
        pass

    def visitSignatureFuncPVoid(self, vsigfpv):
        pass

    def visitSignatureFuncNP(self, vsigfnp):
        pass

    def visitSignatureFuncNPVoid(self, vsigfnpv):
        pass

    def visitSigParamsSingle(self, vsp):
        pass

    def visitSigParamsMulti(self, vspm):
        pass

    def visitSigParamConcrete(self, vspc):
        pass

    def visitBodyConcrete(self, vbc):
        if vbc.stmts:
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
        vsw.exp.accept(self)
        self.tabela.pushEscopo()
        vsw.stmts.accept(self)
        self.tabela.popEscopo()

    def visitStmReturn(self, vsr):
        if vsr.exp:
            vsr.exp.accept(self)

    def visitStmBreak(self, vsb):
        pass

    def visitStmContinue(self, vsc):
        pass

    # IF/ELSE
    def visitIfNoElse(self, vifne):
        vifne.exp.accept(self)
        self.tabela.pushEscopo()
        vifne.stmts.accept(self)
        self.tabela.popEscopo()

    def visitIfElse(self, vife):
        vife.exp.accept(self)
        
        self.tabela.pushEscopo()
        vife.stmtsif.accept(self)
        self.tabela.popEscopo()
        
        self.tabela.pushEscopo()
        vife.stmtselse.accept(self)
        self.tabela.popEscopo()

    def visitIfElseIfr(self, vifei):
        vifei.exp.accept(self)
        
        self.tabela.pushEscopo()
        vifei.stmtsif.accept(self)
        self.tabela.popEscopo()
        
        vifei.ifr.accept(self)

    # DECLARACOES
    def visitDeclLet(self, vdl):
        if self.tabela.buscarEscopoAtual(vdl.id):
            raise ValueError(f"Erro semântico:\n'{vdl.id}' já declarado neste escopo.")
        tipo = vdl.typedecl.accept(self)
        exp_simbolo = vdl.exp.accept(self)
        if tipo is None:
            tipo = exp_simbolo.tipo
        elif tipo != exp_simbolo.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{exp_simbolo.tipo}' a uma variável do tipo '{tipo}'.")
        self.tabela.inserir(ts.Simbolo(nome=vdl.id, categoria='variavel', tipo=tipo))

    def visitDeclMut(self, vdm):
        if self.tabela.buscarEscopoAtual(vdm.id):
            raise ValueError(f"Erro semântico:\n'{vdm.id}' já declarado neste escopo.")
        tipo = vdm.typedecl.accept(self)
        exp_simbolo = vdm.exp.accept(self)
        if tipo is None:
                tipo = exp_simbolo.tipo
        elif tipo != exp_simbolo.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{exp_simbolo.tipo}' a uma variável mutável do tipo '{tipo}'.")
                
        self.tabela.inserir(ts.Simbolo(nome=vdm.id, categoria='variavel_mut', tipo=tipo))

    def visitDeclConst(self, vdc):
        if self.tabela.buscarEscopoAtual(vdc.id):
            raise ValueError(f"Erro semântico:\n'{vdc.id}' já declarado neste escopo.")
        tipo = vdc.type.accept(self)
        simboloDir = vdc.exp.accept(self)
        if simboloDir.categoria == 'literal':
            if tipo != simboloDir.tipo:
                raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma constante do tipo '{tipo}'.")
        else:
            raise ValueError(f"Erro semântico:\nAtribuição de valor a constante '{vdc.id}' deve ser conhecida em tempo de compilação.")
        self.tabela.inserir(ts.Simbolo(nome=vdc.id, categoria='const', tipo=tipo))

    def visitDeclStatic(self, vds):
        if self.tabela.buscarEscopoAtual(vds.id):
            raise ValueError(f"Erro semântico:\n'{vds.id}' já declarado neste escopo.")
        tipo = vds.type.accept(self)
        simboloDir = vds.exp.accept(self)
        if simboloDir.categoria == 'literal':
            if tipo != simboloDir.tipo:
                raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma variável estática do tipo '{tipo}'.")
        else:
            raise ValueError(f"Erro semântico:\nAtribuição de valor a variável estática '{vds.id}' deve ser conhecida em tempo de compilação.")
        self.tabela.inserir(ts.Simbolo(nome=vds.id, categoria='static', tipo=tipo))

    def visitTypeDeclConcrete(self, vtdc):
        if vtdc.type:
            return vtdc.type.accept(self)

    # EXPRESSOES
    def visitExpAssign(self, vea):
        return vea.exp_assign.accept(self)

    def visitExpAtrib(self, vea):
        simboloEsq = self.tabela.buscar(vea.id)
        if not simboloEsq:
            raise ValueError(f"Erro semântico:\nIdentificador '{vea.id}' não foi declarado.")
        if simboloEsq.categoria != 'variavel_mut':
            raise ValueError(f"Erro semântico:\nIdentificador '{vea.id}' não é uma variável mutável.")
        simboloDir = vea.exp.accept(self)
        if simboloEsq.tipo != simboloDir.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma variável do tipo '{simboloEsq.tipo}'.")
        return simboloEsq


    def visitExpAtribuiSoma(self, vas):
        simboloEsq = self.tabela.buscar(vas.id)
        if not simboloEsq:
            raise ValueError(f"Erro semântico:\nIdentificador '{vas.id}' não foi declarado.")
        if simboloEsq.categoria != 'variavel_mut':
            raise ValueError(f"Erro semântico:\nIdentificador '{vas.id}' não é uma variável mutável.")
        simboloDir = vas.exp.accept(self)
        if simboloEsq.tipo != simboloDir.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma variável do tipo '{simboloEsq.tipo}'.")
        return simboloEsq

    def visitExpAtribuiSubtracao(self, vas):
        simboloEsq = self.tabela.buscar(vas.id)
        if not simboloEsq:
            raise ValueError(f"Erro semântico:\nIdentificador '{vas.id}' não foi declarado.")
        if simboloEsq.categoria != 'variavel_mut':
            raise ValueError(f"Erro semântico:\nIdentificador '{vas.id}' não é uma variável mutável.")
        simboloDir = vas.exp.accept(self)
        if simboloEsq.tipo != simboloDir.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma variável do tipo '{simboloEsq.tipo}'.")
        return simboloEsq

    def visitExpAtribuiMultiplicacao(self, vam):
        simboloEsq = self.tabela.buscar(vam.id)
        if not simboloEsq:
            raise ValueError(f"Erro semântico:\nIdentificador '{vam.id}' não foi declarado.")
        if simboloEsq.categoria != 'variavel_mut':
            raise ValueError(f"Erro semântico:\nIdentificador '{vam.id}' não é uma variável mutável.")
        simboloDir = vam.exp.accept(self)
        if simboloEsq.tipo != simboloDir.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma variável do tipo '{simboloEsq.tipo}'.")
        return simboloEsq

    def visitExpAtribuiDivisao(self, vad):
        simboloEsq = self.tabela.buscar(vad.id)
        if not simboloEsq:
            raise ValueError(f"Erro semântico:\nIdentificador '{vad.id}' não foi declarado.")
        if simboloEsq.categoria != 'variavel_mut':
            raise ValueError(f"Erro semântico:\nIdentificador '{vad.id}' não é uma variável mutável.")
        simboloDir = vad.exp.accept(self)
        if simboloEsq.tipo != simboloDir.tipo:
            raise ValueError(f"Erro semântico:\nNão é possível atribuir um valor do tipo '{simboloDir.tipo}' a uma variável do tipo '{simboloEsq.tipo}'.")
        if simboloDir.categoria == 'literal' and simboloDir.valor == 0:
            raise ValueError("Erro semântico:\nDivisão por zero.")
        return simboloEsq

    def visitExpExpOU(self, veu):
        return veu.exp_or.accept(self)

    def visitExpOU(self, veu):
        simboloEsq = veu.exp_or.accept(self)
        simboloDir = veu.exp_and.accept(self)

        if simboloEsq.tipo != ts.BOOL or simboloDir.tipo != ts.BOOL:
            raise ValueError(f"Erro semântico:\nOperador '||' não pode ser aplicado aos tipos '{simboloEsq.tipo}' e '{simboloDir.tipo}'.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = simboloEsq.valor or simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.BOOL, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.BOOL)

    def visitExpExpE(self, vee):
        return vee.exp_and.accept(self)

    def visitExpE(self, vee):
        simboloEsq = vee.exp_and.accept(self)
        simboloDir = vee.exp_rel.accept(self)

        if simboloEsq.tipo != ts.BOOL or simboloDir.tipo != ts.BOOL:
            raise ValueError(f"Erro semântico:\nOperador '&&' não pode ser aplicado aos tipos '{simboloEsq.tipo}' e '{simboloDir.tipo}'.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = simboloEsq.valor and simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.BOOL, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.BOOL)

    def visitExpExpRel(self, ver):
        return ver.exp_rel.accept(self)

    def visitExpRel(self, ver):
        simboloEsq = ver.exp_bitor.accept(self)
        simboloDir = ver.exp_bitor2.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações relacionais só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = None
            if ver.op == '==':
                valor = simboloEsq.valor == simboloDir.valor
            elif ver.op == '!=':
                valor = simboloEsq.valor != simboloDir.valor
            elif ver.op == '<':
                valor = simboloEsq.valor < simboloDir.valor
            elif ver.op == '<=':
                valor = simboloEsq.valor <= simboloDir.valor
            elif ver.op == '>':
                valor = simboloEsq.valor > simboloDir.valor
            elif ver.op == '>=':
                valor = simboloEsq.valor >= simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.BOOL, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.BOOL)

    def visitExpExpBitOr(self, vebo):
        return vebo.exp_bitor.accept(self)

    def visitExpBitOr(self, vebo):
        simboloEsq = vebo.exp_bitor.accept(self)
        simboloDir = vebo.exp_bitxor.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações de bitwise só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = simboloEsq.valor | simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.I32)

    def visitExpExpBitXor(self, vebx):
        return vebx.exp_bitxor.accept(self)

    def visitExpBitXor(self, vebx):
        simboloEsq = vebx.exp_bitxor.accept(self)
        simboloDir = vebx.exp_bitand.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações de bitwise só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = simboloEsq.valor ^ simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.I32)

    def visitExpExpBitAnd(self, veba):
        return veba.exp_bitand.accept(self)

    def visitExpBitAnd(self, veba):
        simboloEsq = veba.exp_bitand.accept(self)
        simboloDir = veba.exp_shift.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações de bitwise só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = simboloEsq.valor & simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.I32)

    def visitExpExpShift(self, ves):
        return ves.exp_shift.accept(self)

    def visitExpShift(self, ves):
        simboloEsq = ves.exp_shift.accept(self)
        simboloDir = ves.exp_add.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações de shift só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = None
            if simboloDir.valor < 0:
                raise ValueError("Erro semântico:\nOperação de shift com valor negativo.")
            if ves.op == '<<':
                valor = simboloEsq.valor << simboloDir.valor
            elif ves.op == '>>':
                valor = simboloEsq.valor >> simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=valor)
        elif simboloDir.categoria == 'literal' and simboloDir.valor < 0:
            raise ValueError("Erro semântico:\nOperação de shift com valor negativo.")
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.I32)

    def visitExpExpAdd(self, vea):
        return vea.exp_add.accept(self)

    def visitExpAdd(self, vea):
        simboloEsq = vea.exp_add.accept(self)
        simboloDir = vea.exp_mul.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações de adição e subtrção só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = None
            if vea.op == '+':
                valor = simboloEsq.valor + simboloDir.valor
            elif vea.op == '-':
                valor = simboloEsq.valor - simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=valor)
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.I32)

    def visitExpExpMul(self, vem):
        return vem.exp_mul.accept(self)

    def visitExpMul(self, vem):
        simboloEsq = vem.exp_mul.accept(self)
        simboloDir = vem.exp_unary.accept(self)

        if simboloEsq.tipo != ts.I32 or simboloDir.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperações de multiplicação, divisão e módulo só podem ser aplicadas ao tipo inteiro {ts.I32}.")

        if simboloEsq.categoria == 'literal' and simboloDir.categoria == 'literal':
            valor = None
            if vem.op == '*':
                valor = simboloEsq.valor * simboloDir.valor
            elif vem.op == '/':
                if simboloDir.valor == 0:
                    raise ValueError("Erro semântico:\nDivisão por zero.")
                valor = simboloEsq.valor // simboloDir.valor
            elif vem.op == '%':
                if simboloDir.valor == 0:
                    raise ValueError("Erro semântico:\nDivisão por zero.")
                valor = simboloEsq.valor % simboloDir.valor
            return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=valor)
        elif simboloDir.categoria == 'literal' and vem.op in ['/', '%'] and simboloDir.valor == 0:
            raise ValueError("Erro semântico:\nDivisão por zero.")
        return ts.Simbolo(nome=None, categoria='variavel', tipo=ts.I32)

    def visitExpExpUnary(self, veu):
        return veu.exp_unary.accept(self)

    def visitExpUnaryNot(self, venu):
        simbolo = venu.exp_unary.accept(self)
        if simbolo.tipo != ts.BOOL:
            raise ValueError(f"Erro semântico:\nOperador '!' não pode ser aplicado ao tipo '{simbolo.tipo}'.")
        return simbolo

    def visitExpUnaryNeg(self, venu):
        simbolo = venu.exp_unary.accept(self)
        if simbolo.tipo != ts.I32:
            raise ValueError(f"Erro semântico:\nOperador '-' não pode ser aplicado ao tipo '{simbolo.tipo}'.")
        return simbolo

    def visitExpPrimary(self, vep):
        return vep.exp_primary.accept(self)

    def visitExpPrimaryCall(self, vepc):
        return vepc.call.accept(self)

    def visitExpPrimaryNum(self, vepn):
        return ts.Simbolo(nome=None, categoria='literal', tipo=ts.I32, valor=vepn.value)

    def visitExpPrimaryId(self, vepi):
        simbolo = self.tabela.buscar(vepi.id)
        if not simbolo:
            raise ValueError(f"Erro semântico:\nIdentificador '{vepi.id}' não foi declarado.")
        return ts.Simbolo(nome=None, categoria=simbolo.categoria, tipo=simbolo.tipo)

    def visitExpPrimaryString(self, veps):
        return ts.Simbolo(nome=None, categoria='literal', tipo=ts.STR, valor=veps.value)

    def visitExpPrimaryBool(self, vepb):
        return ts.Simbolo(nome=None, categoria='literal', tipo=ts.BOOL, valor=vepb.value)

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
        simbolo = self.tabela.buscar(vcfa.id)
        if not simbolo:
            raise ValueError(f"Erro semântico:\nIdentificador '{vcfa.id}' não foi declarado.")
        if simbolo.categoria != 'funcao':
            raise ValueError(f"Erro semântico:\nIdentificador '{vcfa.id}' não é uma função.")
        
        args_tipos = vcfa.args.accept(self)
        if not isinstance(args_tipos, list):
            args_tipos = [args_tipos] if args_tipos else []
            
        params = simbolo.params or []
        if len(args_tipos) != len(params):
            raise ValueError(f"Erro semântico:\nFunção '{vcfa.id}' espera {len(params)} argumentos, mas recebeu {len(args_tipos)}.")

        if simbolo.nome == 'println' and args_tipos[0].tipo in params[0][1]:
            pass
        else:
            for i, (arg_tipo, (param_nome, param_tipo)) in enumerate(zip(args_tipos, params)):
                if arg_tipo and param_tipo and arg_tipo.tipo != param_tipo:
                    raise ValueError(f"Erro semântico:\nArgumento {i+1} da função '{vcfa.id}' esperava tipo '{param_tipo}', mas recebeu '{arg_tipo}'.")
                
        return simbolo

    def visitCallFunc(self, vcf):
        simbolo = self.tabela.buscar(vcf.id)
        if not simbolo:
            raise ValueError(f"Erro semântico:\nIdentificador '{vcf.id}' não foi declarado.")
        if simbolo.categoria != 'funcao':
            raise ValueError(f"Erro semântico:\nIdentificador '{vcf.id}' não é uma função.")
            
        return simbolo

    def visitArgsExpArgs(self, vaea):
        tipo_arg = vaea.exp.accept(self)
        tipos_restantes = vaea.args.accept(self)
        if not isinstance(tipos_restantes, list):
            tipos_restantes = [tipos_restantes] if tipos_restantes else []
        return [tipo_arg] + tipos_restantes

    def visitArgsExp(self, vae):
        tipo_arg = vae.exp.accept(self)
        return [tipo_arg]

    # TIPO
    def visitTypeID(self, vtid):
        return vtid.type
