lista = ['prego','falar','ouvir','jogar']
# lista_enumerada = enumerate(lista)
# for i in enumerate(lista, start=1):#ele transforma em iteravel a lista e é melhor ddeixar dentro do for pra a variavel n se esgotar e n dar pra repetir
#     print(i[1],i[0])
# mesma coisa
for indice, palavra in enumerate(lista, start=1):
    print(indice, palavra)
print(enumerate(lista))
print(list(enumerate(lista)))