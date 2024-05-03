from copy import deepcopy

def organizador_por_preco(lista):
    lista_oraganizado_por_preco = list()
    for ind, i in enumerate(lista_por_preco(lista)):
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