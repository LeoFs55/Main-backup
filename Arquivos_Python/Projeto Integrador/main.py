import packages as pk
from os import system
#Definindo qual o tipo de entrada

def calculadora():
    print(f"""{20*'-'}
# Calculado de BINARIO, OCTAL E HEXADECIMAL PARA DECIMAL
# {20*'-'}
# BINARIO P/ DECIMAL      (PRESS '1')
# OCTAL P/ DECIMAL        (PRESS '2')
# HEXADECIMAL P/ DECIMAL  (PRESS '3')
# DECIMAL P/ BINARIO      (PRESS '4')
# DECIMAL P/ OCTAL        (PRESS '5')
# DECIMAL P/ HEXADECIMAL  (PRESS '6') """)
    opcao = input('R:')
    try:   
        num_opcao = int(opcao)
        bi_para_decimal =  num_opcao == 1
        oct_para_decimal = num_opcao == 2
        hex_para_decimal = num_opcao == 3
        dec_para_binario = num_opcao == 4
        dec_para_octal = num_opcao == 5
        dec_para_hexa = num_opcao == 6
        if num_opcao > 6:
            return 'Você não digitou um número correspondente aos fornecidos.'
    except ValueError:
        print('Você não digitou um número')     
    if bi_para_decimal:
        num = input('Digite o numero BINARIO: ')
        return pk.binario(num, 2)
    elif oct_para_decimal:
        num = input('Digite o numero OCTAL: ')
        return pk.octadecimal(num, 8)
    elif hex_para_decimal:
        num = input('Digite o numero HEXAL: ')
        return pk.hexadecimal(num, 16)
    elif dec_para_binario:
        num = input('Digite o numero DECIMAL: ')
        return pk.binario(num, 10)
    elif dec_para_octal:
        num = input('Digite o numero DECIMAL: ')
        return pk.octadecimal(num, 10)
    elif dec_para_hexa:
        num = input('Digite o numero DECIMAL: ')
        return pk.hexadecimal(num, 10)

resultado = calculadora()
print(f'O resultado é {resultado}')