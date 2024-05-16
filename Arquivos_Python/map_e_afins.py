from functools import partial
from types import GeneratorType
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(value, porcentagem):
    return round(value * (1+(porcentagem/100)),2)

aumentar_10_porcento = partial(aumentar_porcentagem,porcentagem=10)
# produto = [ {**p, 'preco': aumentar_10_porcento(p['preco'])} for p in produtos]
# print_iter(produto)
def organizador_de_novos_produtos(produto):
    return {**produto, 'preco': aumentar_10_porcento(produto['preco'])}

novos_produtos = (map(organizador_de_novos_produtos,produtos))
# novos_produtos = (x for x in produtos)
# print_iter(novos_produtos)
# print('Esgotada -> ',list(novos_produtos))#o iterador dessa forma se encontra esgotado

#Mas dessa forma não
novos_produtos = list(map(organizador_de_novos_produtos,produtos))
# novos_produtos = (x for x in produtos)
# print_iter(novos_produtos)
# print('Não esgotada -> ',list(novos_produtos))

# print(hasattr(novos_produtos,'__iter__'))
# print(hasattr(novos_produtos,'__next__'))
# print(isinstance(novos_produtos,GeneratorType))

print(list(map(lambda n: n*2,[1,2,3,4])))