from copy import deepcopy
def uniao_lista(locais, estados):
    # lista_menor = deepcopy(locais) if len(locais) < len(estados) else deepcopy(estados)
    # lista_maior = deepcopy(locais) if len(locais) > len(estados) else deepcopy(estados)
    # listas_unidas = [(i,lista_maior[ind]) for ind, i in enumerate(lista_menor)]
    intervalo = min(len(locais),len(estados))
    return [(locais[i], estados[i])for i in range(intervalo)]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

lista1e2 = uniao_lista
print(list(zip(lista1,lista2)))

lista1.pop(0)

print(list(zip(lista1,lista2)))
