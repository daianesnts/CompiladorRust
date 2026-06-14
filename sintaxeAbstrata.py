from abc import abstractmethod
from abc import ABC

#programa

# sintaxeabstrata.py

class Program:
    def __init__(self, topdecls):
        # topdecls será uma lista puramente em Python contendo as declarações do topo
        self.topdecls = topdecls 

    def accept(self, visitor):
        return visitor.visitProgram(self)


#FUNÇÕES
class FuncDecl:
    def __init__(self, signature, body):
        self.signature = signature  # Objeto da classe Signature
        self.body = body            # Objeto da classe Body

    def accept(self, visitor):
        return visitor.visitFuncDecl(self)


class Signature:
    def __init__(self, id, sigparams, return_type):
        self.id = id                # String com o nome da função
        self.sigparams = sigparams  # Lista puramente em Python de objetos SigParam
        self.return_type = return_type  # String com o tipo de retorno, ou None se não houver

    def accept(self, visitor):
        return visitor.visitSignature(self)


class SigParam:
    def __init__(self, id, type):
        self.id = id                # String com o nome do parâmetro
        self.type = type            # String com o tipo do parâmetro

    def accept(self, visitor):
        return visitor.visitSigParam(self)


class Body:
    def __init__(self, stmts):
        self.stmts = stmts          # Lista puramente em Python com os comandos/statements

    def accept(self, visitor):
        return visitor.visitBody(self)
    

#STRUCT E TRAIT 
class StructDecl:
    def __init__(self, id, structfields):
        self.id = id                    # String com o nome da struct
        self.structfields = structfields  # Lista em Python de objetos StructField

    def accept(self, visitor):
        return visitor.visitStructDecl(self)


class StructField:
    def __init__(self, id, type):
        self.id = id                    # String com o nome do campo
        self.type = type                # String com o tipo do campo

    def accept(self, visitor):
        return visitor.visitStructField(self)


class TraitDecl:
    def __init__(self, id, traitbody):
        self.id = id                    # String com o nome do trait
        self.traitbody = traitbody      # Lista em Python de objetos Signature (ou None/Vazia)

    def accept(self, visitor):
        return visitor.visitTraitDecl(self)
    

#COMANDOS 
class StmExp:
    def __init__(self, expr):
        self.expr = expr              # Objeto de expressão

    def accept(self, visitor):
        return visitor.visitStmExp(self)


class StmLoop:
    def __init__(self, expr):
        self.expr = expr              # Objeto de expressão (corpo ou condição do loop)

    def accept(self, visitor):
        return visitor.visitStmLoop(self)


class StmWhile:
    def __init__(self, cond, expr_body):
        self.cond = cond              # Expressão da condição
        self.expr_body = expr_body    # Expressão/Bloco do corpo do while

    def accept(self, visitor):
        return visitor.visitStmWhile(self)


class StmReturn:
    def __init__(self, expr):
        self.expr = expr              # Expressão de retorno

    def accept(self, visitor):
        return visitor.visitStmReturn(self)


class StmBreak:
    def __init__(self):
        pass                          # Não possui parâmetros adicionais

    def accept(self, visitor):
        return visitor.visitStmBreak(self)


class StmContinue:
    def __init__(self):
        pass                          # Não possui parâmetros adicionais

    def accept(self, visitor):
        return visitor.visitStmContinue(self)
    

# IFELSE
class StmIf:
    def __init__(self, cond, then_block, else_block=None):
        self.cond = cond              # Expressão da condição do IF
        self.then_block = then_block  # Bloco executado se a condição for verdadeira
        self.else_block = else_block  # Pode ser outro StmIf (no caso de ELSE IF), um Bloco (no caso de ELSE) ou None

    def accept(self, visitor):
        return visitor.visitStmIf(self)


#DECLARACOES    
class DeclLet:
    def __init__(self, id, type_decl, exp):
        self.id = id                # String com o nome da variável
        self.type_decl = type_decl  # String com o tipo (ex: 'int') ou None se for omitido
        self.exp = exp              # Objeto de expressão do valor inicial

    def accept(self, visitor):
        return visitor.visitDeclLet(self)


class DeclMut:
    def __init__(self, id, type_decl, exp):
        self.id = id                # String com o nome da variável mutável
        self.type_decl = type_decl  # String com o tipo ou None
        self.exp = exp              # Objeto de expressão do valor inicial

    def accept(self, visitor):
        return visitor.visitDeclMut(self)


class DeclCons:
    def __init__(self, id, type_str, num_value):
        self.id = id                # String com o nome da constante
        self.type_str = type_str    # String com o tipo da constante
        self.num_value = num_value  # Valor numérico direto da constante

    def accept(self, visitor):
        return visitor.visitDeclCons(self)


class DeclExp:
    def __init__(self, id, exp):
        self.id = id                # String com o nome da variável sendo reatribuída
        self.exp = exp              # Objeto de expressão com o novo valor

    def accept(self, visitor):
        return visitor.visitDeclExp(self)


#EXPRESSOES
class ExpBinOp:
    def __init__(self, op, left, right):
        self.op = op                  # String do operador (e.g., '+', '-', '==')
        self.left = left              # Objeto de expressão à esquerda
        self.right = right            # Objeto de expressão à direita

    def accept(self, visitor):
        return visitor.visitExpBinOp(self)


class ExpAttrib:
    def __init__(self, id, expr):
        self.id = id                  # String com o nome da variável
        self.expr = expr              # Objeto de expressão com o valor atribuído

    def accept(self, visitor):
        return visitor.visitExpAttrib(self)


class ExpCompound:
    def __init__(self, stmts):
        self.stmts = stmts            # Lista em Python com os comandos do bloco

    def accept(self, visitor):
        return visitor.visitExpCompound(self)


class ExpUnaryNot:
    def __init__(self, expr):
        self.expr = expr              # Objeto de expressão que será negado

    def accept(self, visitor):
        return visitor.visitExpUnaryNot(self)


class ExpUnaryMinus:
    def __init__(self, expr):
        self.expr = expr              # Objeto de expressão que terá o sinal invertido

    def accept(self, visitor):
        return visitor.visitExpUnaryMinus(self)


class ExpBlockExpr:
    def __init__(self, stmts, expr):
        self.stmts = stmts            # Lista de comandos executados antes
        self.expr = expr              # A expressão final que define o valor de retorno do bloco

    def accept(self, visitor):
        return visitor.visitExpBlockExpr(self)


class ExpBlockStmts:
    def __init__(self, stmts):
        self.stmts = stmts            # Lista de comandos do bloco

    def accept(self, visitor):
        return visitor.visitExpBlockStmts(self)


class ExpCall:
    def __init__(self, id, args):
        self.id = id                  # String com o nome da função chamada
        self.args = args              # Lista em Python com os argumentos passados

    def accept(self, visitor):
        return visitor.visitExpCall(self)


class ExpNumber:
    def __init__(self, value):
        self.value = value            # Valor numérico literal (int/float)

    def accept(self, visitor):
        return visitor.visitExpNumber(self)


class ExpBoolean:
    def __init__(self, value):
        self.value = value            # Booleano literal do Python (True ou False)

    def accept(self, visitor):
        return visitor.visitExpBoolean(self)

#CHAMADA DE FUNÇÃO

class ExpId:
    def __init__(self, id):
        self.id = id                  # String com o nome do identificador (variável)

    def accept(self, visitor):
        return visitor.visitExpId(self)

class ExpCall:
    def __init__(self, id, args):
        self.id = id        # String com o nome da função que está sendo chamada
        self.args = args    # Lista puramente em Python com os argumentos (IDs das variáveis)

    def accept(self, visitor):
        return visitor.visitExpCall(self)




