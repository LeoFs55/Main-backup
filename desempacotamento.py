#Desempacotamento em chamadas 
string = 'ABC'
lista = ['Leonardo', 'Helena', 1,2,3,'Eduarda']
tuplas = ('python','é','legal')
salas = [['Maria','Helena'],['Elaine'],['Luiz', 'João', 'Eduarda']]


# a,*_,ultimo = lista
# print(a,ultimo)

print(*lista, sep='\n')
# print(*string)
# print(*tuplas)

# print(*salas,sep='\n')