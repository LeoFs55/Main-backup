# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
#
#São a mesma coisa porem é igual o x = ''
#                                  variavel = tuple(x)
#
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# nome = input('Digite seu nome: ')
# sobrenome = input('Digite seu sobrenome: ')
# idade = input('Digite sua idade: ')
# altura = input('Digite a sua altura: ')
import copy
pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Figorelli',
    'idade': 18,
    'altura': 1.8,
}
# for i in pessoa:
#     print(i, pessoa[i])

# print(len(pessoa))
# print(pessoa.keys())
# print(list(pessoa.values()))
# for i in pessoa.values():
#     print(i)
# print(pessoa.items())
# for classe, objeto in pessoa.items():
#     print(classe,': ',objeto, sep='')
# pessoa.setdefault('endereco', 'Sem teto')
# print(pessoa['endereco'])
# pessoa2.copy(pessoa['nome'])
# pessoa2 = {
#     'c1': 1,
#     'c2': 2,
#     'c3': [1,2,3]
# }
# pessoa3 = pessoa2.copy()#shallow copy/copia só dados imutaveis

# pessoa3['c1'] = 200
# # pessoa3['c3'][0] = 4#dados mutaveis serão só linkados

# print(pessoa2)
# print(pessoa3)
# pessoa3  = copy.deepcopy(pessoa2) # agora uma copia profunda, a lista n é afetada

# pessoa3['c1'] = 200
# pessoa3['c3'][0] = 4#dados mutaveis serão só linkados
# print(pessoa2)
# print(pessoa3)

# # print(pessoa.get('nome2','Não-Existe'))
# chave = pessoa.pop('nome')
# for i,a in pessoa.items():
#     print(i,a)

# print(chave)#assim o nome da chave se perde

# ultima_chave = pessoa.popitem()
# for i,a in pessoa.items():
#     print(i,a)

# print(ultima_chave[1])#assim a chave n se perde
# pessoa.update({
#     'nome':'Angela',
#     'sexualidade':'Trans-sexual'
# })
# print(pessoa)
# pessoa.update(nome='Angela',sexualidade='Bi-sexual')
tupla = (('nome','Angela'),('sexualidade','Bi-sexual'))
lista = [['nome','Angela'],['sexualidade','Bi-sexual']]
pessoa.update(lista)
print(pessoa)#mesma coisa