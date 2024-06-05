#Associação
class Escritor:
    def __init__(self,nome) -> None:
        self.nome = nome
        self._tool = None

    @property
    def nome(self):
        return self._name
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, name):
        self._tool = name
        

    
class Tools:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo...'
    
# escritor = Escritor('Leo')
# caneta = Tools('Caneta')
# maquina = Tools('Maquina')
# escritor.tool = caneta
# # escritor.tool = maquina
# print(escritor.tool.escrever())
#Agregação
class Carrinho:
    def __init__(self) -> None:
        self._produtos = list()

    # @property
    # def produtos(self):
    #     return self._produtos
    
    # @produtos.setter
    # def produtos(self,produto):
    #     self._produtos = list()
    #     self._produtos.append(produto)
    
    # @property
    # def quantidade(self):
    #     return self._quantidade
    
    # @quantidade.setter
    # def quantidade(self):
    #     self._quantidade = len(self._produtos)
    
    # @property
    # def valor(self):
    #     return self._valor
    
    # @valor.setter
    # def valor(self,preco):
    #     self._valor = int()
    #     self._valor += preco

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def adicionar_produto(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto) 
        
    


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

# carrinho = Carrinho()

# p1, p2 = Produto('Bolo', 17), Produto('Pão', 5.5)
# carrinho.adicionar_produto(p1,p2)
# print(carrinho.total())

#Composição

class Cliente:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.enderecos = list()

    def add_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def __del__(self):
            print('Pagando cliente: ',self.nome)

class Endereco:
    def __init__(self,rua,numero) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Pagando endereco: ',self.rua,self.numero)

cliente = Cliente('Leonardo')
cliente.add_endereco('Mario graccho', 119)
print(cliente.enderecos[0])
cliente2 = Cliente('alvaro')
cliente2.add_endereco('Mario graccho', 119)
print(cliente2.enderecos[0])
del cliente