from functools import reduce
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# E da forma como eu queria fazer era assim:
# total = sum([i['preco'] for i in produtos])

# total = 0
# for i in produtos:
#     total += i['preco']


#Com reduce
def funcao_do_reduce(acumulador, produto):
    return acumulador + produto['preco']


total = reduce(funcao_do_reduce,produtos,0)
print(f'{total:,.2f}')

#com lambda
total = reduce(lambda a ,p: a + p['preco'],produtos,0)
print(f'{total:,.2f}')

