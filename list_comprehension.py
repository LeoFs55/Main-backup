import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40 )
# print(list(range(10)))

lista = list(range(10))
# print(lista)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)
gerador = lambda m: list(range(m))
# print(gerador(10))

lista = [numero for numero in range(10)]
# print(lista)

lista2 = [
    numero * 2
    for numero in range(10)
]
# print(lista2)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

produtos_novos = [
    {**produto, 'preco':produto['preco']*1.05}
    if produto['preco']>20 else {**produto}
    for produto in produtos
    if produto['preco']>10
]
# p(produtos_novos)


# p(produtos_novos)

lista = [
    n for n in range(10)
    if n < 5
]

# print(lista)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

lista = [(x,y) for x in range(3) for y in range(3)]  
lista = [[x for y in range(3)] for x in range(3)]

print(lista)