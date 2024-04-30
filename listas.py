# cadastro = [['leonardo','alvaro','albert','milena'],[18,18,17,18]]#tem como criar uma lista com list() e suporta qualquer tipo até outra 
# numero = list('Leonardo') #dessa forma só funciona com str
# for i in range(5):
#     entrada = input('Digite o seu nome: ')
#     cadastro[0].append(entrada)

# for i in range(5):
#     entrada = input('Digite a sua idade: ')
#     cadastro[1].append(entrada)
# del cadastro[0][2]
# del cadastro[1][2]#quando ele deleta o indice o indice posterior ao deletado se 'toma' o local do indice deletado
# e tipo imagina q essa porra de lista tem 10000 indices e vc vai e dela o 1 o python vai ter q mudar 9999 indices
#e isso vai ocupar muito processamento
# cadastro[0].pop()
# cadastro[1].pop()#remove o ultimo item da lista, e ele retorna esse valor
# e para listas pequenas tambem tem como fazer isso aq
# aluno_bom = cadastro[0].pop(0)#posso detalhar qual indice ele ira remover da lista e retonar compara ao del ele n retorna esse indice
# try:
#     for i in range(4):
#         print(f'O nome {i+1}o nome foi: {cadastro[0][i]} e sua idade é {cadastro[1][i]}')
#         print(aluno_bom)
# except:
#     ...     
# E coisa nova: Uma string é MUTAVEL quando está dentro de lista
lista = [0,1,2,3,4,5]
lista_a = [1,5,6,8]
#clear limpa a lista
# lista.insert(0, 5)
# lista_b = lista.extend(lista_a) n vai funcionar
# lista_b = lista + lista_a (ele n vai fazer isso
lista.extend(lista_a)#como ele age diretamente na lista n tem como voce gerar uma atribuição de uma ação 
lista_b = lista
print(lista_b)
# cadastro[0].insert(0,'vai se fuder')
# print(cadastro[0][0])
print(1370%11)