class Usuario:
    def __init__(self,/,nome,data_nascimento,cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def alterar_nome(self, nome):
        self.nome = nome

# user = Usuario()
# print(user.nome)
# print(user.data_nascimento)
# print(user.cpf)

# class Calculadora:
#     def __init__(self):
#         def somar(n1,n2):
#             return n1+n2
#         def subtrair(n1,n2):
#             return n1-n2
#         self.soma = somar
#         self.subtracao = subtrair

# calculo = Calculadora()

# print(calculo.subtracao(1,2))

usuario1 = Usuario(nome='Leonardo Figorelli Santana',data_nascimento='28/10/2005',cpf='48448072855')
usuario1.alterar_nome('Leonafardo')
print(usuario1.nome)

