from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def alteracao_de_preco(lista):
    lista_alterada = [{'nome':i['nome'],'preco':(i['preco']*1.1)} for i in lista]
    return lista_alterada

produtos_reformulados = alteracao_de_preco(produtos)

novos_produtos = [deepcopy(i) for i in produtos_reformulados]

def organizador_por_nome(lista):
    quantidade = len(lista)
    lista_ordenada = list()
    lista_classificada = [{'nome': (i['nome'].split())[0],'classificacao':int(i['nome'].split()[1]), 'preco': i['preco']}for i in lista]
    for ind in range(quantidade,0,-1):
        for i in lista_classificada:
            if i['classificacao'] == ind:
                lista_ordenada.append(deepcopy(i))
    return lista_ordenada

def organizador_por_preco(lista, lista_de_preco):
    lista_oraganizado_por_preco = list()
    for ind, i in enumerate(lista_de_preco):
        for i_dict in lista:
            if i_dict['preco'] == i:
                lista_oraganizado_por_preco.append(deepcopy(i_dict))
    return lista_oraganizado_por_preco


def lista_por_preco(lista):
    valores = [i['preco'] for i in lista]
    lista_cobaia = deepcopy(valores)
    quant = len(lista)
    menor_valor = 1000000
    ind_menor_valor = 0
    lista_crescente = list()
    for i in valores:    
        for ind, i in enumerate(lista_cobaia):
            if i<menor_valor:
                menor_valor = i
                ind_menor_valor = ind
        lista_crescente.append(lista_cobaia.pop(ind_menor_valor))
        menor_valor = 1000000
    return lista_crescente


lista_crescrente = lista_por_preco(novos_produtos)

print(organizador_por_preco(novos_produtos, lista_crescrente))