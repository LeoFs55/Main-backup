lista = []
def mult(*args):
    resultado = 1
    for numero in args:
        resultado *= numero

    return resultado

def parimpar(a):
    if a == 0:
        return 'o não é par nem impar!'
    elif a%2 == 0:
        return f'o numero {a} é par!'
    return f'o numero {a} é impar!'

for i in range(3):
    entrada = float(input('Digite um numero: '))
    lista.append(entrada)

tupla = tuple(lista)

print(f'O resultado da multiplicação destes valores é: {mult(*tupla)}. E {parimpar(mult(*tupla))}')