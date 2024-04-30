frase = 'Calculadora'
print(f'''
{len(frase)*'='}
{frase}    
{len(frase)*'='}
''')
instrucao = (""" 
|==================|
|Soma = 1          |
|Subtração = 2     |
|Multiplicação = 3 |
|Divisão = 4       |
|==================|
""")
val1 = input('Digite um numero: ')
val2 = input('Digite outro numero: ')
val1int = float(val1)
val2int = float(val2)
print(instrucao)
operacao = input('Digite o indice o operador: ')
operacaoint = int(operacao)
soma = operacaoint == 1
subtração = operacaoint == 2
multiplicação = operacaoint == 3
divisao = operacaoint == 4
# if soma:
#     resultado = val1int+val2int
# elif subtração:
#     resultado = val1int-val2int
# elif multiplicação:
#     resultado = val1int*val2int
# elif divisão:
#     resultado = val1int/val2int
# else:
#     print('Você não digitou nenhum indice corresondente.')
resultado = val1int+val2int if soma else\
            val1int-val2int if subtração  else\
            val1int*val2int if multiplicação else\
            val1int/val2int if divisao else\
            print('Você não digitou nenhum indice corresondente.')
print(f'O resultado dessa operação é {resultado}')
