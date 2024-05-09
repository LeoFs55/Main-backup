
def somando_lista(lista1, lista2):
    # delta = min(len(lista1),len(lista2)) if len(lista1) < len(lista2) else min(len(lista2),len(lista1))
    # lista_soma = [(lista1[i]+lista2[i])for i in range(delta)]
    lista_soma = [(x+y)for x ,y in zip(lista1, lista2)]
    return lista_soma
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]


print(somando_lista(lista_a, lista_b))
