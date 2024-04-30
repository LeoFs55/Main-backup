nomes = ['Leonardo','Leonardo', 'Alvaro', 'Albert']
conjunto = set(nomes)
# print(conjunto)
conjunto_vazio = set()
# print(conjunto_vazio)
numeros = 1,2,3,4,4,4,4,5#ele remove numeros repetidos
numeros_n_repetidos = list(set(numeros))
# print(numeros_n_repetidos)
s1 = set()
s1.add('Leonardo')#só aceita um parametro
s1.update(('Figorelli', 'Santana'))#aceita mais de um, mas para aparecer como vc quer ele precisa de uma tupla
# print(s1)
s1.discard('Figorelli')#como não existe 2 coisas iguais em um set se vc digitar em discard ele elimina ou usa o clear
# print(s1)

#Operadores
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #União
s4 = s1 & s2 #Intersecção
s5 = s1 - s2 #Diferença só o da esquerda
s7 = s2 - s1 #Diferença só o da esquerda
s6 = s1 ^ s2 #Dif simetrica = itens que não estão em ambas
print(s3,s4,s5,s7,s6)
