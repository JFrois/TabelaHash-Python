class ElementoListaEncadeada:
    def __init__(self, siglaEstado=None, nomeEstado=None):
        self.siglaEstado = siglaEstado
        self.nomeEstado = nomeEstado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def adicionar(self, siglaEstado, nomeEstado):
        nodo = ElementoListaEncadeada (siglaEstado, nomeEstado)
        if self.head is None:
            self.head = nodo
        else:
            nodo.proximo = self.head
            self.head = nodo

    def listar(self):
        atual = self.head
        elementos = []
        while atual:
            elementos.append (f"{atual.siglaEstado}\t{atual.nomeEstado}")
            atual = atual.proximo
        return elementos


class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.hash = [ListaEncadeada () for _ in range (self.tamanho)]

    def hashfuncao(self, k):
        if k == "DF":
            return 7
        else:
            return (ord (k[0]) + ord (k[1])) % self.tamanho

    def inserir(self, siglaEstado, nomeEstado):
        posicao = self.hashfuncao (siglaEstado)
        self.hash[posicao].adicionar (siglaEstado, nomeEstado)

    def listar(self):
        for i in range (self.tamanho):
            elementos = self.hash[i].listar ()
            print (f"Posição {i}: {',  [->]'.join (elementos) if elementos else 'None'}")


def inserirEstados(tabela):
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
        ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
        ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
        ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
        ("SE", "Sergipe"), ("TO", "Tocantins")
    ]
    for sigla, nome in estados:
        tabela.inserir (sigla, nome)


def menu():
    tabela = TabelaHash ()
    while True:
        print ("\nSeja bem vindo ao nosso programa de tabela Hash\nAbaixo são as opções do nosso programa:")
        print (
            "Opções:\n1 - Listar posições tabela hash\n2 - Listar estados\n3 - Adicionar a sigla do seu nome\n4 - Listar tabela hash com os estados e suas siglas e meu nome e sigla respectivamente\n5 - Sair do programa")
        opcao = int (input ("Escolha o que deseja: "))

        if opcao == 1:
            print ("[-->] Você escolheu a opção 1 - Listar posições tabela hash")
            tabela.listar ()
        elif opcao == 2:
            print ("[-->] Você escolheu a opção 2 - Listar tabela hash")
            inserirEstados (tabela)
            tabela.listar ()
        elif opcao == 3:
            print ("[-->] Você escolheu a opção 3 - Adicionar a sigla do meu nome(JF - Juan Frois)")
            tabela.inserir ("JF", "Juan Frois")
            tabela.listar ()
        elif opcao == 4:
            print (
                "[-->] Você escolheu a opção 4 - Listar tabela hash com os estados e suas siglas e meu nome e sigla respectivamente")
            inserirEstados (tabela)
            tabela.inserir ("JF", "Juan Frois")
            tabela.listar ()
        elif opcao == 5:
            print ("[-->] Você escolheu a opção 5 - Sair do programa")
            break
        else:
            print (
                "[-->] Desculpe, a opção escolhida não está disponível, por favor tente novamente uma opção de 1 a 5")


menu ()