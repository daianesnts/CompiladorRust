class Simbolo:

    def __init__(self, nome, categoria, tipo=None, params=None):
        self.nome = nome
        self.categoria = categoria
        self.tipo = tipo
        self.params = params


class TabelaSimbolos:

    def __init__(self):
        self.tabela = []
        self.pushEscopo()

    def pushEscopo(self):
        self.tabela.append({})

    def popEscopo(self):
        self.tabela.pop()

    def inserir(self, simbolo):
        if simbolo.nome in self.tabela[-1]:
            raise ValueError(f"Erro semântico:\n'{simbolo.nome}' já foi declarado neste escopo.")
        self.tabela[-1][simbolo.nome] = simbolo

    def buscar(self, nome):
        for escopo in reversed(self.tabela):
            if nome in escopo:
                return escopo[nome]
        return None

    def buscarEscopoAtual(self, nome):
        return self.tabela[-1].get(nome)

    def existe(self, nome):
        return self.buscar(nome) is not None
