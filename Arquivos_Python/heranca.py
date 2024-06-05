class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf) -> None:
        super().__init__(nome, sobrenome)
        self.cpf = cpf

    def cadastro_de_cartao(self,nome, numero):
        self.nome_card = nome
        self.numero_card = numero
    ...



cliente = Cliente('Leonardo', 'Figorelli Santana', 484848981)
# cliente.falar()
print(cliente.cpf)
# cliente.cadastro_de_cartao('Visa', '1235626315251')
# print(cliente.nome_card)

#Super e sobreposição
class MinhaString(str):
    def lower(self):
        print('Chamou lower')
        return super().lower()
    

# strr = MinhaString('OI')
# print(strr.lower())

class A:
    a = 'val a'
    def metodo(self):
        print('A')

class B(A):
    b = 'val b'
    def metodo(self):
        
        print('B')

class C(B):
    c = 'val c'
    def metodo(self):
        super(B,self).metodo()
        super().metodo()
        print('C')

c = C()
print(c.a)
print(c.b)
print(c.c)
c.metodo()