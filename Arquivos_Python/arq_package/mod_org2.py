from copy import deepcopy

def organizador_por_nome(lista):
    quantidade = len(lista)
    lista_ordenada = list()
    lista_classificada = [{'nome': (i['nome'].split())[0],'classificacao':int(i['nome'].split()[1]), 'preco': i['preco']}for i in lista]
    for ind in range(quantidade,0,-1):
        for i in lista_classificada:
            if i['classificacao'] == ind:
                lista_ordenada.append(deepcopy(i))
    return lista_ordenada