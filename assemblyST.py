symbolTable = []
INT = 'i32'
BOOL = 'bool'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
VARIABLE = 'var'
SCOPE = 'scope'
SCOPE_GLOBAL = 'global'
SCOPE_MAIN = 'main'
OFFSET = 'offset'
SP = 'sp'
STR = '.asciiz'
DEBUG = 0


def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope
    symbolTable[-1][SP] = 0
    printTable()

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]
    printTable()

def beginInnerScope():
    global symbolTable
    spAntigo = symbolTable[-1][SP]
    nameScopeAntigo = symbolTable[-1][SCOPE]
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScopeAntigo
    symbolTable[-1][SP] = spAntigo
    printTable()

def endInnerScope():
    endScope()

def getCurrentST():
    global symbolTable
    return symbolTable[-1]

def addVar(name, type):
    global symbolTable
    if not name in symbolTable[-1]:
        symbolTable[-1][SP] -= 4 
        symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type, OFFSET: symbolTable[-1][SP]}
    else:
        symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type, OFFSET: symbolTable[-1][name][OFFSET]}
    printTable()

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}
    printTable()

def addSP(value):
    global symbolTable
    symbolTable[-1][SP] += value   

def getSP():
    return symbolTable[-1][SP]

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def getBindableCurrentScope(bindableName):
    global symbolTable
    if (bindableName in symbolTable[-1].keys()):
        return symbolTable[-1][bindableName]
    return None

def getScope(bindableName = None):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][SCOPE]
    return symbolTable[-1][SCOPE]