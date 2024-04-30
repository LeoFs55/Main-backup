#Cuidado com dados mútaveis
a = 'Leo'
b = a

a = 'Boi'
print(a , b)
#a diferença entre elas é essa que quando vc atribui um valor de uma lista a outra elas n estão
# em locais diferentes da memoria, logo se voce mudar algo em uma vc vai mudar a outra
# imutais locais !=
# mutaveis locais ==
lista1 = ['Leo','Alvaro','Albert', [1]]
lista2 = lista1[:]
lista3 = lista1.copy()

lista1[0] = 'Boi'

print(lista2, lista3)