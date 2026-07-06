from visitorAbstrato import VisitorAbstrato

class PrettyPrinter(VisitorAbstrato):
    def __init__(self):
        self._indent_level = 0

    def visit(self, no):
        return no.accept(self)
    
    def indent(self):
        self._indent_level += 1

    def dedent(self):
        self._indent_level -= 1
    
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
    
#FUNÇÕES
    def visitFuncDeclSignatureBody(self, vfdsb):
        vfdsb.signature.accept(self)
        vfdsb.body.accept(self)
    
    def visitSignatureFunc(self, vsf):
        print(f"fn {vsf.id}", end="")
        vsf.signaturei.accept(self)
    
    def visitSignatureISigP(self, vsigp):
        vsigp.signaturep.accept(self)

    def visitSignatureISigNP(self, vsignp):
        vsignp.signaturenp.accept(self)
    
    def visitSignatureFuncP(self, vsigfp):
        print("(", end="")
        vsigfp.sigparams.accept(self)
        print(") -> ", end="")
        vsigfp.type.accept(self)

    def visitSignatureFuncPVoid(self, vsigfpv):
        print("(", end="")
        vsigfpv.sigparams.accept(self)
        print(")", end="")
    
    def visitSignatureFuncNP(self, vsigfnp):
        print("() -> ", end="")
        vsigfnp.type.accept(self)
    
    def visitSignatureFuncNPVoid(self, vsigfnpv):
        print("()", end="")
    
    def visitSigParamsSingle(self, vsp):
        vsp.sigparam.accept(self)
    
    def visitSigParamsMulti(self, vsmp):
        vsmp.sigparam.accept(self)
        print(", ", end="")
        vsmp.sigparams.accept(self)
    
    def visitSigParamConcrete(self, vspc):
        print(f"{vspc.id}: ", end="")
        vspc.type.accept(self)
    
    def visitBodyConcrete(self, vbc):
        print(" {")
        self.indent()
        vbc.stmts.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}}")
    
#STRUCT E TRAIT
    def visitStructDeclConcrete(self, vsdc):
        print(f"struct {vsdc.id}", end="")
        print(" {")
        self.indent()
        vsdc.structfields.accept(self)
        self.dedent()
        print(f"\n{"\t"*self._indent_level}}}")
    
    def visitStructFieldsSingle(self, vsfs):
        print("\t"*self._indent_level, end="")
        vsfs.structfield.accept(self)
    
    def visitStructFieldsMulti(self, vsfm):
        print("\t"*self._indent_level, end="")
        vsfm.structfield.accept(self)
        print(",")
        vsfm.structfields.accept(self)
    
    def visitStructFieldConcrete(self, vsfc):
        print(f"{vsfc.id}: ", end="")
        vsfc.type.accept(self)
    
    def visitTraitDeclConcrete(self, vtdc):
        print(f"trait {vtdc.id}", end="")
        print(" {")
        self.indent()
        vtdc.traitbody.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}}")
    
    def visitTraitBodySingle(self, vtbs):
        print("\t"*self._indent_level, end="")
        vtbs.traitsignatures.accept(self)
    
    def visitTraitBodyMulti(self, vtbm):
        print("\t"*self._indent_level, end="")
        vtbm.traitsignatures.accept(self)
        vtbm.traitbody.accept(self)
    
    def visitTraitSignaturesSignature(self, vtss):
        vtss.signature.accept(self)
        print(";")
    
    def visitTraitSignaturesFuncDecl(self, vtsfd):
        vtsfd.funcdecl.accept(self)
    
    def visitTraitSignaturesTraitMethod(self, vtstm):
        vtstm.traitmethod.accept(self)
    
    def visitTraitMethodConcrete(self, vtmc):
        print(f"fn {vtmc.id}", end="")
        vtmc.traitsignature.accept(self)
        print(";")
    
    def visitTraitSignatureConcrete(self, vtsc):
        vtsc.traitsignaturep.accept(self)
        if vtsc.body is not None:
            vtsc.body.accept(self)
        
    def visitTraitSignaturePSingleP(self, vtspsp):
        print(f"(&self) -> ", end="")
        vtspsp.type.accept(self)
    
    def visitTraitSignaturePSinglePV(self, vtspspv):
        print(f"(&self)", end="")
    
    def visitTraitSignaturePMultiP(self, vtspmp):
        print(f"(&self, ", end="")
        vtspmp.sigparams.accept(self)
        print(f") -> ", end="")
        vtspmp.type.accept(self)
    
    def visitTraitSignaturePMultiPV(self, vtspmpv):
        print(f"(&self, ", end="")
        vtspmpv.sigparams.accept(self)
        print(f")", end="")
    
#COMANDOS
    def visitStmtsSingle(self, vss):
        print("\t"*self._indent_level, end="")
        vss.stm.accept(self)
    
    def visitStmtsMulti(self, vsm):
        print("\t"*self._indent_level, end="")
        vsm.stm.accept(self)
        vsm.stmts.accept(self)
    
    def visitStmDecl(self, vsd):
        vsd.decl.accept(self)
    
    def visitStmExp(self, vse):
        vse.exp.accept(self)
        print(";")
    
    def visitStmIfr(self, vsif):
        vsif.ifr.accept(self)

    def visitStmLoop(self, vsl):
        vsl.stmts.accept(self)
    
    def visitStmWhile(self, vsw):
        print("while ", end="")
        vsw.exp.accept(self)
        self.indent()
        print(" {")
        vsw.stmts.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}}")

    def visitStmReturn(self, vsr):
        print("return ", end="")
        vsr.exp.accept(self)
        print(";", end="")
    
    def visitStmBreak(self, vsbr):
        print("break;", end="")
    
    def visitStmContinue(self, vsc):
        print("continue;", end="")
    
    def visitIfNoElse(self, vifne):
        print("if ", end="")
        vifne.exp.accept(self)
        print(" {")
        self.indent()
        vifne.stmts.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}}")
    
    def visitIfElse(self, vife):
        print("if ", end="")
        vife.exp.accept(self)
        print(" {")
        self.indent()
        vife.stmtsif.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}} else {{")
        self.indent()
        vife.stmtselse.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}}")
    
    def visitIfElseIfr(self, vifei):
        print("if ", end="")
        vifei.exp.accept(self)
        print(" {")
        self.indent()
        vifei.stmtsif.accept(self)
        self.dedent()
        print(f"{"\t"*self._indent_level}}} else ", end="")
        vifei.ifr.accept(self)

#DECLARAÇÔES
    def visitDeclLet(self, vdl):
        print(f"let {vdl.id}", end="")
        vdl.typedecl.accept(self)
        print(" = ", end="")
        vdl.exp.accept(self)
        print(";")
    
    def visitDeclMut(self, vdm):
        print(f"let mut {vdm.id}", end="")
        vdm.typedecl.accept(self)
        print(" = ", end="")
        vdm.exp.accept(self)
        print(";")
    
    def visitDeclConst(self, vdc):
        print(f"const {vdc.id}", end="")
        vdc.type.accept(self)
        print(" = ", end="")
        vdc.exp.accept(self)
        print(";")

    def visitTypeDeclConcrete(self, vtdc):
        if vtdc.type is not None:
            print(f": {vtdc.type}", end="")

#EXPRESSOES
    def visitExpAssign(self, vea):
        vea.exp_assign.accept(self)
    
    def visitExpAtrib(self, vea):
        print(f"{vea.id} = ", end="")
        vea.exp.accept(self)
    
    def visitExpAtribuiSoma(self, vas):
        print(f"{vas.id} += ", end="")
        vas.exp.accept(self)
    
    def visitExpAtribuiSubtracao(self, vas):
        print(f"{vas.id} -= ", end="")
        vas.exp.accept(self)
    
    def visitExpAtribuiMultiplicacao(self, vam):
        print(f"{vam.id} *= ", end="")
        vam.exp.accept(self)
    
    def visitExpAtribuiDivisao(self, vad):
        print(f"{vad.id} /= ", end="")
        vad.exp.accept(self)
    
    def visitExpExpOU(self, veu):
        veu.exp_or.accept(self)
    
    def visitExpOU(self, veu):
        veu.exp_or.accept(self)
        print(" || ", end="")
        veu.exp_and.accept(self)
    
    def visitExpExpE(self, vee):
        vee.exp_and.accept(self)
    
    def visitExpE(self, vee):
        vee.exp_and.accept(self)
        print(" && ", end="")
        vee.exp_rel.accept(self)
    
    def visitExpExpRel(self, ver):
        ver.exp_rel.accept(self)
    
    def visitExpRel(self, ver):
        ver.exp_bitor.accept(self)
        print(f" {ver.op} ", end="")
        ver.exp_bitor2.accept(self)
    
    def visitExpExpBitOr(self, vebo):
        vebo.exp_bitor.accept(self)

    def visitExpBitOr(self, vebo):
        vebo.exp_bitor.accept(self)
        print(" | ", end="")
        vebo.exp_bitxor.accept(self)
    
    def visitExpExpBitXor(self, vebx):
        vebx.exp_bitxor.accept(self)

    def visitExpBitXor(self, vebx):
        vebx.exp_bitxor.accept(self)
        print(" ^ ", end="")
        vebx.exp_bitand.accept(self)
    
    def visitExpExpBitAnd(self, veba):
        veba.exp_bitand.accept(self)
    
    def visitExpBitAnd(self, veba):
        veba.exp_bitand.accept(self)
        print(" & ", end="")
        veba.exp_shift.accept(self)
    
    def visitExpExpShift(self, ves):
        ves.exp_shift.accept(self)
    
    def visitExpShift(self, ves):
        ves.exp_shift.accept(self)
        print(f" {ves.op} ", end="")
        ves.exp_add.accept(self)
    
    def visitExpExpAdd(self, vea):
        vea.exp_add.accept(self)
    
    def visitExpAdd(self, vea):
        vea.exp_add.accept(self)
        print(f" {vea.op} ", end="")
        vea.exp_mul.accept(self)
    
    def visitExpExpMul(self, vem):
        vem.exp_mul.accept(self)

    def visitExpMul(self, vem):
        vem.exp_mul.accept(self)
        print(f" {vem.op} ", end="")
        vem.exp_unary.accept(self)
    
    def visitExpExpUnary(self, veu):
        veu.exp_unary.accept(self)
    
    def visitExpUnaryNot(self, venu):
        print("!", end="")
        venu.exp_unary.accept(self)
    
    def visitExpUnaryNeg(self, venu):
        print("-", end="")
        venu.exp_unary.accept(self)

    def visitExpPrimary(self, vep):
        vep.exp_primary.accept(self)
    
    def visitExpPrimaryCall(self, vepc):
        vepc.call.accept(self)
    
    def visitExpPrimaryNum(self, vepn):
        print(vepn.value, end="")
    
    def visitExpPrimaryId(self, vepi):
        print(vepi.id, end="")

    def visitExpPrimaryString(self, veps):
        print(f'"{veps.value}"', end="")
    
    def visitExpPrimaryBool(self, vepb):
        print(vepb.value, end="")
    
    def visitExpPrimaryParen(self, vepp):
        print("(", end="")
        vepp.exp.accept(self)
        print(")", end="")
    
    def visitExpPrimaryBlocoExp(self, vepbe):
        print("{", end="")
        vepbe.stmts.accept(self)
        vepbe.exp.accept(self)
        print("}", end="")
    
    def visitExpPrimaryBloco(self, vepb):
        print("{", end="")
        vepb.stmts.accept(self)
        print("}", end="")
    
#CHAMADAS DE FUNÇÂO
    def visitCallFuncArgs(self, vcfa):
        print(f"{vcfa.id}(", end="")
        vcfa.args.accept(self)
        print(")", end="")
    
    def visitCallFunc(self, vcf):
        print(f"{vcf.id}()", end="")

    def visitArgsExpArgs(self, vaea):
        vaea.exp.accept(self)
        print(", ", end="")
        vaea.args.accept(self)
    
    def visitArgsExp(self, vae):
        vae.exp.accept(self)
    
    def visitTypeID(self, vtid):
        print(vtid.type, end="")
