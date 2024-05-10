#count
from itertools import count

c1 = count()
ranges = list(range(10))
print(ranges)
for i in c1:
    print(i)
    if i> 99:
        break

# print("""
# Calculadora de soma e subtração
#     0 - Sair
#     """)
# while True:
#     valor = input(
#             'Digite o indice do calculo que deseja fazer e os dois numero dessa forma: X+Y ou X-Y: '
#         )
#     numeros = valor.split('+') if '+' in valor else valor.split('-')
#     calculo = (int(numeros[0])+int(numeros[1])) if '+' in valor else (int(numeros[0])-int(numeros[1]))
#     print(calculo)
#     continuar = input('Continuar 1, Parar 2:')
#     tentativas = (c1)
#     if continuar == '1':
#         continue
#     else:
#         print(f'Numero de tentativas {tentativas}')
#         break
