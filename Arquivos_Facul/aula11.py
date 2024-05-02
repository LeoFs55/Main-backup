#apresentando o input
name = input('Digite seu nome: ')
print(f'O seu nome é {name}') # colocan do um = dps da variavel ele retornar isso: name='Leonrado'

# input sempre retorna em str então tem que ser feito uma coercion, mas algo que sempre fiz foi add o int no input
# Mas isso caso o usuario digitasse algo que não fosse um int o programa seria morto então adicionar uma verificação após o usuario adicionar o valor
# seria mais correto, como? ads ele vai falar mas por enquanto só atribuindo o valor a outra variavel e nela colocar o coercion tipo isso
inp0 = input('Digite um numero: ')
inp1 = input('Digite outro número: ')
# talves seria assim:
num_int0 = int(inp0)
num_int1 = int(inp1)
print(f'A soma desses numeros é {num_int0+num_int1}')