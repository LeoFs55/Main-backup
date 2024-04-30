def achar(lista):#Ex:lista == [1,2,3]
    conj = set(lista)
    quant_set = len(conj)
    quant_lista = len(lista)
    quant = 0 #Quantidade de Repetições
    rep_num = 0 #Numero repitido
    rep_num_prox = -1 #
    ind_num = 0
    ind_num_min = len(lista)
    if quant_lista>quant_set:
        for ind, i in enumerate(lista):
            for comp in lista[ind+1:]:
                quant +=1
                if i == comp:
                    rep_num = i
                    ind_num = quant
                    if ind_num<ind_num_min:
                        ind_num_min = ind_num
                        rep_num_prox = rep_num  
            quant = 0
        return rep_num_prox 
    else:
        return rep_num_prox

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado
   
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    #[3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    #[5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
            



for lista in lista_de_listas_de_inteiros:
    print(f'Função 1: {achar(lista)} Função 2: {encontra_primeiro_duplicado(lista)}')

