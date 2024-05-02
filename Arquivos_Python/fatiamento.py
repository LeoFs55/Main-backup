#Fatiamento de Strings
# ele começa explicando a relação de cada elemento com a contagem
# 012345678
# Olá mundo
#-987654321
variavel = 'Olá mundo'
print(variavel[8])
print(variavel[-1])
print(variavel[4:10])#obs importante quando é pra declarar o final ele sempre pega um antes do final
print(len(variavel[4:]))
print(variavel[::-1])
a = range(10,2)
for i in range(10,2):
    print(i)