from visitorAbstrato import VisitorAbstrato
import assemblyST as ast

def getAssemblyType(type = None):
    if type == ast.STR:
        return ".asciiz"
    return ".word"

class VisitorAssembly(VisitorAbstrato):

    def __init__(self):
        ast.beginScope(ast.SCOPE_GLOBAL)
        self.funcs = []  
        self.text = []  
        self.text.append(".text")
        self.text.append("    move $fp, $sp")
        self.data = set()
        self.rotulos = {}
        self.println = False

    def visit(self, no):
        return no.accept(self)

    def novo_rotulo(self, string):
        if not string in self.rotulos:
            self.rotulos[string] = 0
        rotulo = f"{string}_{self.rotulos[string]}"
        self.rotulos[string] += 1
        return rotulo

    def getList(self):
        return self.text if ast.getScope() in [ast.SCOPE_GLOBAL, ast.SCOPE_MAIN] else self.funcs

    def sairEscopoInterno(self):
        tabelaAntiga = ast.getCurrentST()
        ast.endInnerScope()
        tabelaAtual = ast.getCurrentST()
        diffSp = tabelaAtual[ast.SP] - tabelaAntiga[ast.SP]
        code = self.getList()
        code.append(f"    addi $sp, $sp, {diffSp}")

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
        name = vtdds.declstatic.id
        vtdds.declstatic.exp.accept(self)
        self.data.add((name, getAssemblyType()))
        ast.addVar(name, getAssemblyType())
        code = self.getList()
        code.append(f"    sw $v0, {name}($zero)") 

    # FUNCOES
    def visitFuncDeclSignatureBody(self, vfdsb):
        vfdsb.signature.accept(self)
        vfdsb.body.accept(self)
        ast.endScope()

    def visitSignatureFunc(self, vsf):
        params, retorno = vsf.signaturei.accept(self)
        ast.addFunction(vsf.id, params, retorno)
        ast.beginScope(vsf.id)
        code = self.getList()
        code.append(f"{vsf.id}:")
        code.append("    move $fp, $sp")
        if params:
            for i in range(0, len(params), 2):
                ast.addVar(params[i], params[i+1])
        code.append(f"    addi $sp, $sp, {ast.getSP()}")

    def visitSignatureISigP(self, vsigp):
        return vsigp.signaturep.accept(self)

    def visitSignatureISigNP(self, vsignp):
        return vsignp.signaturenp.accept(self)

    def visitSignatureFuncP(self, vsigfp):
        params = vsigfp.sigparams.accept(self)
        #tipo_retorno = vsigfp.type.accept(self)
        return params, getAssemblyType()

    def visitSignatureFuncPVoid(self, vsigfpv):
        params = vsigfpv.sigparams.accept(self)
        return params, None

    def visitSignatureFuncNP(self, vsigfnp):
        #tipo_retorno = vsigfnp.type.accept(self)
        return [], getAssemblyType()

    def visitSignatureFuncNPVoid(self, vsigfnpv):
        return [], None

    def visitSigParamsSingle(self, vsp):
        return vsp.sigparam.accept(self)

    def visitSigParamsMulti(self, vspm):
        return vspm.sigparam.accept(self) + vspm.sigparams.accept(self)

    def visitSigParamConcrete(self, vspc):
        tipo = vspc.type.accept(self)
        return [vspc.id, getAssemblyType()]

    def visitBodyConcrete(self, vbc):
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
        #rotulo_inicial = self.novo_rotulo("loop")
        #rotulo_final = self.novo_rotulo("fim_loop")
        #code = self.getList()
        #code.append(f"{rotulo_inicial}:")
        #vsl.stmts.accept(self)
        #code.append(f"    j {rotulo_inicial}")
        #code.append(f"{rotulo_final}:")
        pass

    def visitStmWhile(self, vsw):
        rotulo_inicial = self.novo_rotulo("while")
        rotulo_final = self.novo_rotulo("fim_while")
        code = self.getList()
        code.append(f"{rotulo_inicial}:")
        vsw.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_final}")
        ast.beginInnerScope()
        vsw.stmts.accept(self)
        self.sairEscopoInterno()
        code.append(f"    j {rotulo_inicial}")
        code.append(f"{rotulo_final}:")

    def visitStmReturn(self, vsr):
        vsr.exp.accept(self)
        code = self.getList()
        code.append(f"    move $sp, $fp")
        code.append(f"    jr $ra")

    def visitStmBreak(self, vsb):
        pass

    def visitStmContinue(self, vsc):
        pass

    # IF/ELSE
    def visitIfNoElse(self, vifne):
        rotulo_final = self.novo_rotulo("fim_if")
        code = self.getList()
        vifne.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_final}")
        ast.beginInnerScope()
        vifne.stmts.accept(self)
        self.sairEscopoInterno()
        code.append(f"{rotulo_final}:")

    def visitIfElse(self, vife):
        rotulo_final = self.novo_rotulo("fim_if")
        rotulo_else = self.novo_rotulo("else")
        code = self.getList()
        vife.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_else}")
        ast.beginInnerScope()
        vife.stmts.accept(self)
        self.sairEscopoInterno()
        code.append(f"    j {rotulo_final}")
        code.append(f"{rotulo_else}:")
        ast.beginInnerScope()
        vife.else_stmts.accept(self)
        self.sairEscopoInterno()
        code.append(f"{rotulo_final}:")

    def visitIfElseIfr(self, vifei):
        rotulo_final = self.novo_rotulo("fim_if")
        rotulo_else = self.novo_rotulo("else")
        code = self.getList()
        vifei.exp.accept(self)
        code.append(f"    beq $v0, $zero, {rotulo_else}")
        ast.beginInnerScope()
        vifei.stmts.accept(self)
        self.sairEscopoInterno()
        code.append(f"    j {rotulo_final}")
        code.append(f"{rotulo_else}:")
        ast.beginInnerScope()
        vifei.ifr.accept(self)
        self.sairEscopoInterno()
        code.append(f"{rotulo_final}:")

    # DECLARACOES
    def visitDeclLet(self, vdl):
        code = self.getList()
        vdl.exp.accept(self)
        ast.addVar(vdl.id, getAssemblyType())
        bind = ast.getBindable(vdl.id)
        code.append(f"    sw $v0, {bind[ast.OFFSET]}($fp)")
        code.append(f"    addi $sp, $sp, -4")

    def visitDeclMut(self, vdm):
        code = self.getList()
        vdm.exp.accept(self)
        ast.addVar(vdm.id, getAssemblyType())
        bind = ast.getBindable(vdm.id)
        code.append(f"    sw $v0, {bind[ast.OFFSET]}($fp)")
        code.append(f"    addi $sp, $sp, -4")

    def visitDeclStatic(self, vds):
        pass

    def visitDeclConst(self, vdc):
        pass

    def visitTypeDeclConcrete(self, vtdc):
        pass

    # EXPRESSOES
    def visitExpAssign(self, vea):
        return vea.exp_assign.accept(self)

    def visitExpAtrib(self, vea):
        code = self.getList()
        vea.exp.accept(self)
        bind = ast.getBindable(vea.id)
        code.append(f"    sw $v0, {bind[ast.OFFSET]}($fp)")

    def visitExpAtribuiSoma(self, vas):
        pass

    def visitExpAtribuiSubtracao(self, vas):
        pass

    def visitExpAtribuiMultiplicacao(self, vam):
        pass

    def visitExpAtribuiDivisao(self, vad):
        pass

    def visitExpExpOU(self, veu):
        return veu.exp_or.accept(self)

    def visitExpOU(self, veu):
        code = self.getList()
        veu.exp_or.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        veu.exp_and.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        code.append("    or $v0, $v0, $t0")

    def visitExpExpE(self, vee):
        return vee.exp_and.accept(self)

    def visitExpE(self, vee):
        code = self.getList()
        vee.exp_and.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        vee.exp_rel.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        code.append("    and $v0, $v0, $t0")

    def visitExpExpRel(self, ver):
        return ver.exp_rel.accept(self)

    def visitExpRel(self, ver):
        code = self.getList()
        ver.exp_bitor.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        ver.exp_bitor2.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        if ver.op == '==':
            code.append("    seq $v0, $t0, $v0")
        elif ver.op == '!=':
            code.append("    sne $v0, $t0, $v0")
        elif ver.op == '<':
            code.append("    slt $v0, $t0, $v0")
        elif ver.op == '<=':
            code.append("    sle $v0, $t0, $v0")
        elif ver.op == '>':
            code.append("    sgt $v0, $t0, $v0")
        elif ver.op == '>=':
            code.append("    sge $v0, $t0, $v0")

    def visitExpExpBitOr(self, vebo):
        return vebo.exp_bitor.accept(self)

    def visitExpBitOr(self, vebo):
        code = self.getList()
        vebo.exp_bitor.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        vebo.exp_bitxor.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        code.append("    or $v0, $v0, $t0")

    def visitExpExpBitXor(self, vebx):
        return vebx.exp_bitxor.accept(self)

    def visitExpBitXor(self, vebx):
        code = self.getList()
        vebx.exp_bitxor.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        vebx.exp_bitand.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        code.append("    xor $v0, $v0, $t0")

    def visitExpExpBitAnd(self, veba):
        return veba.exp_bitand.accept(self)

    def visitExpBitAnd(self, veba):
        code = self.getList()
        veba.exp_bitand.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        veba.exp_shift.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        code.append("    and $v0, $v0, $t0")

    def visitExpExpShift(self, ves):
        return ves.exp_shift.accept(self)

    def visitExpShift(self, ves):
        code = self.getList()
        ves.exp_shift.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        ves.exp_add.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        if ves.op == '<<':
            code.append("    sllv $v0, $t0, $v0")
        elif ves.op == '>>':
            code.append("    srlv $v0, $t0, $v0")

    def visitExpExpAdd(self, vea):
        return vea.exp_add.accept(self)

    def visitExpAdd(self, vea):
        code = self.getList()
        vea.exp_add.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        vea.exp_mul.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        if vea.op == '+':
            code.append("    add $v0, $t0, $v0")
        elif vea.op == '-':
            code.append("    sub $v0, $t0, $v0")

    def visitExpExpMul(self, vem):
        return vem.exp_mul.accept(self)

    def visitExpMul(self, vem):
        code = self.getList()
        vem.exp_mul.accept(self)
        code.append("    addi $sp, $sp, -4")
        ast.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        vem.exp_unary.accept(self)
        code.append("    lw $t0, 0($sp)")
        code.append("    addi $sp, $sp, 4")
        ast.addSP(4)
        if vem.op == '*':
            code.append("    mul $v0, $t0, $v0")
        elif vem.op == '/':
            code.append("    div $t0, $v0")
            code.append("    mflo $v0")
        elif vem.op == '%':
            code.append("    div $t0, $v0")
            code.append("    mfhi $v0")

    def visitExpExpUnary(self, veu):
        return veu.exp_unary.accept(self)

    def visitExpUnaryNot(self, venu):
        code = self.getList()
        venu.exp_unary.accept(self)
        code.append("    not $v0, $v0")

    def visitExpUnaryNeg(self, venu):
        code = self.getList()
        venu.exp_unary.accept(self)
        code.append("    neg $v0, $v0")

    def visitExpPrimary(self, vep):
        return vep.exp_primary.accept(self)

    def visitExpPrimaryCall(self, vepc):
        code = self.getList()
        code.append("    addi $sp, $sp, -8")
        ast.addSP(-8)
        oldSP = ast.getSP()
        code.append("    sw $ra, 0($sp)")
        code.append("    sw $fp, 4($sp)")
        vepc.call.accept(self)
        code.append(f"    lw $ra, 0($sp)")
        code.append(f"    lw $fp, 4($sp)")
        code.append(f"    addi $sp, $sp, 8")
        ast.addSP(oldSP - ast.getSP())
        ast.addSP(8)
        return ('', ast.INT)

    def visitExpPrimaryNum(self, vepn):
        code = self.getList()
        code.append(f"    li $v0, {vepn.value}")
        return ('', ast.INT)

    def visitExpPrimaryId(self, vepi):
        code = self.getList()
        idName = ast.getBindable(vepi.id)
        if idName:
            if ast.getScope(vepi.id) == ast.SCOPE_GLOBAL:
                code.append(f"    lw $v0, {vepi.id}($zero)")
            else:
                code.append(f"    lw $v0, {idName[ast.OFFSET]}($fp)")
        return ('', ast.INT)

    def visitExpPrimaryString(self, veps):
        rotulo_str = self.novo_rotulo("STR")
        str_final = veps.value
        self.data.add((rotulo_str, getAssemblyType(ast.STR), str_final))
        return (rotulo_str, ast.STR)

    def visitExpPrimaryBool(self, vepb):
        pass

    def visitExpPrimaryParen(self, vepp):
        pass

    def visitExpPrimaryBlocoExp(self, vepbe):
        pass

    def visitExpPrimaryBloco(self, vepb):
        pass

    # CHAMADAS DE FUNCAO
    def visitCallFuncArgs(self, vcfa):
        code = self.getList()
        if vcfa.id == "println":
            self.println = True
            str_addr, tipo = vcfa.args.accept(self)
            if tipo == ast.STR:
                code.append(f"    li $v0, 4")
                code.append(f"    la $a0, {str_addr}")
            else:
                code.append(f"    move $a0, $v0")
                code.append(f"    li $v0, 1")
            code.append(f"    syscall")
            code.append(f"    li $v0, 11")
            code.append(f"    li $a0, 10")
            code.append("    syscall")
            self.println = False
        else:
            vcfa.args.accept(self)
            code.append(f"    jal {vcfa.id}")

    def visitCallFunc(self, vcf):
        code = self.getList()
        code.append(f"    jal {vcf.id}")

    def visitArgsExpArgs(self, vaea):
        code = self.getList()
        vaea.exp.accept(self)
        ast.addSP(-4)
        code.append(f"    sw $v0, {ast.getSP()}($fp)")
        vaea.args.accept(self)

    def visitArgsExp(self, vae):
        code = self.getList()
        if self.println:
            return vae.exp.accept(self)
        else:
            vae.exp.accept(self)
            ast.addSP(-4)
            code.append(f"    sw $v0, {ast.getSP()}($fp)")

    # TIPO
    def visitTypeID(self, vtid):
        return vtid.type

    def get_code(self):
        finalcode = []
        if self.data:
            for globalVar in self.data:
                if globalVar[1] == ".word":
                    finalcode.insert(0, f"    {globalVar[0]}: {globalVar[1]} 0")
                else:
                    finalcode.insert(0, f'    {globalVar[0]}: {globalVar[1]} "{globalVar[2]}"')
            finalcode.insert(0,".data")
        finalcode = finalcode + self.text
        finalcode.append("    j end")
        finalcode = finalcode + self.funcs
        finalcode.append("\nend:\n    li $v0, 10\n    syscall")
        return "\n".join(finalcode)
