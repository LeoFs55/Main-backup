lista = [1,2,351,612,62,12]
lista.sort()
# print(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista.sort(key=lambda item: item['nome'])Essa muda diretamente a lista
def exibir(lista):
    for i in lista:
        print(i)

# exibir(lista)

# print()

lista = sorted(lista, key=lambda item: item['nome'])#essa é uma funcao que retorna a lista ordenada

# exibir(lista)

def executa(funcao, *args):
    return funcao(*args)

def somar(x,y):
    return x + y

# print(executa(lambda x, y: x+y, 10, 20))

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

multi_2 = executa(lambda multiplicador: lambda numero: numero*multiplicador,2)
# print(multi_2(4))

print(executa(lambda *args: sum(args), 1,2,351,612,62,12))# que bglh louco véi
