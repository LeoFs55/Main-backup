#nessa aula ele somente apresentou o que seria o try e except
# except é basicamente o erro e caso de um erro e será acionado
numero_str = input('Digete um numero: ')

try:
    numero_int = int(numero_str)
    print('Você digitou o numero', numero_int,'e seu dobro é', (numero_int*2),'.')
except:
    print('Você não digitou um numero')