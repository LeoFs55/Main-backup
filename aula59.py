""" 
Estrutura de Repetições 
while == enquanto 
Executa uma condição enquato for verdadeira
"""
# Abecedario_m = ('abcdefghijklmnopqrstuvwxyz')
# x = 0
# while x<=11:
#     print(Abecedario_m[x])
#     x+=1
# x=0
# while x<=4:
#     print(' ',Abecedario_m[x])
#     x+=1    
# x=0
# while x<=14:
#     print('  ',Abecedario_m[x])
#     x+=1 
# while True:
#     ...
# print(123)#Esse codigo nunca será lido por se tratar de um loop infinito
# x=0
# while x<10:
#     x+=1  
#     print(x)
# x=0
# while x>-10:
#     x-=1  
#     print(x)
# x=1
# y=0
# while y<10:
#     y+=1 
#     x*=y
#     print(x)
# x=2
# y=0
# while y<5:
#     y+=1
#     x**=y  
#     print(f'{x:,.2f}')
# x=1
# y=0
# while y<10:
#     y+=1
#     x/=2  
# print(x)
# x=1
# y=0
# while y<10:
#     y+=1
#     x//=2  
#     print(x)
# x=0
# while x<10:
#     x%=1  
#     print(x)
# while x<3:
#     idade = input('Diga a sua idade: ')
#     try:
#         idade_int = int(idade)
#         x+=1
#     except:
#         print('Você não digitou um numero')
# while dentro de while 
x = 0 
y = 0
while x<10:
    x+=1
    while y<x:
        y+=1
        print(x,(y*2))