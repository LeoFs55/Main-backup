#For tambem é uma função des estrutura de repetição
# while é utilizado para quando vc sabe a quantidade de repetições

# x = [1,2,3,4,5]
# b = ''
# for i in x: #o i ou qualquer coisa q vc for colocar ali ele serve serve como um contador
#     b += f'*{i}'
#     print(i)
# print(b+'*')

""" 
for + range
"""

# num  = range(-1,-101,-2)
# a = []
# for i in num:
#     a.append(i)
#     print(i)
# print(a)
alunos = ['Leonardo','Alvaro','Albert','Milena','Ricardo','Thales']
atividades = [True,True,False,True,False,False]
check = []
for i in range(6):
    if atividades[i] == True:
        check.append('Realizado')
    else:
        check.append('Não-Realizado')
for i in range(6):
    print(f'O aluno {alunos[i]} teve o resultado da ativade como: {check[i]}')
    print(63*'=')
