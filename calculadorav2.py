from math import sqrt
import os
frase = 'Calculadora'
print(f'''
{len(frase)*'='}
{frase}    
{len(frase)*'='}
''')
calculos = [[],[],[]]
x = 0
instrucao = (""" 
|==================|
|Soma = 1          |
|Subtração = 2     |
|Multiplicação = 3 |
|Divisão = 4       |
|Exponenciação = 5 |
|Radiciação = 6    |
|Sair = 0          |
|==================|
""")
def calculo(soma):
    ...
while True:
    try:
        numero1 = input(f'Digite o {x+1}o numero: ')
        numero1float = numero1
        calculos[0].append(numero1float)
        print(instrucao)
        operacao = input(f'Digite o operador: ')
        operacaoint = int(operacao)
        soma = operacaoint == 1
        subtração = operacaoint == 2
        multiplicação = operacaoint == 3
        divisão = operacaoint == 4
        exponenciação = operacaoint == 4
        radiciação = operacaoint == 5
        sair = operacaoint == 5
        x += 1
        os.system('cls')
        numero2 = input(f'Digite o {x+1}o numero: ')
        numero2float = numero2
        calculos[1].append(numero2float)

        break
    except:
        ...
