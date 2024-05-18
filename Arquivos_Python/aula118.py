def adiciona(nome, lista=None):#O python sempre vai usar a essa lista dps que declarado 
    lista = [] if lista == None else lista
    lista.append(nome)
    return lista

lista = adiciona('Leo')
adiciona('Albert', lista)
print(lista)

lista2 = adiciona('Leo2')
adiciona('Albert2', lista2)
print(lista2)
