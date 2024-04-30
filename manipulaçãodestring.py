#Split e join

# nome = '   Leonardo Figorelli, Santana    '
# nome_cru = nome.strip().split(', ' )
# for i, nome in enumerate(nome_cru):
#     print(nome_cru[i])

#O que seria uma poa pratica:
    
nome = '   Leonardo,Figorelli, Santana    '
nome_cru = nome.split(',' )

lista_nome = []
for i, nome in enumerate(nome_cru):
    lista_nome.append(nome_cru[i].strip())

# print(nome_cru)
# print(lista_nome)
nome_unidos = '-'.join(lista_nome)#separador.metodo e dps o iteralvel - usadado para unir palavras
print(nome_unidos)