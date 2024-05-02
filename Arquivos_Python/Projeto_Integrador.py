#Validacao do numero

def num_validation(entrada):
    try:
        num = int(entrada)
        return True, num
    except ValueError:
        return False,'O valor inserido não é um número.'        

#Binario

def bi_validation(numero):

    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>1:
            return False, 'O número inserido não era bínario.'
        else:
            continue
    return True, tupla_numero

def calculo_bi_p_dec(entrada,quant):
    resultado = 0
    tupla_entrada = bi_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(2**(i))
    return resultado

def calculo_dec_p_bi(num):
    if num == '0':
        return num
    binario = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
    return num

def binario(num, base):
    if base == 10:

        while True:

            entrada = num

            if num_validation(entrada):
                print(calculo_dec_p_bi(entrada))
                break

            else:
                print(num_validation(entrada)[1])
                continue

    elif base == 2:
        
        while True:
            entrada = num
            if num_validation(entrada):
                quant = len(entrada)

                if bi_validation(entrada)[0]:
                    print(calculo_bi_p_dec(entrada,quant))

                else:
                    print(bi_validation(entrada)[1])
                    continue

                break
            else:
                print(num_validation(entrada)[1])

                continue

#Octal

def oct_validation(numero):
    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>7:
            return False, 'O número inserido não é Octal.'
        else:
            continue
    return True, tupla_numero

def calculo_dec_p_octal(num):
    if num == '0':
        return f'O número {num} é igual a 0 em OCTADECIMAL'
    octal = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal //= 8

    return num

def calculo_oct_p_dec(entrada,quant):#Calculo de OCTAL PARA DECIMAL
    resultado = 0
    tupla_entrada = oct_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(8**(i))
    return resultado

def octadecimal(num, base):
    if base == 10:    
        while True:
            entrada = num
            if num_validation(entrada):
                print(calculo_dec_p_octal(entrada))
                break
            else:
                print(num_validation(entrada)[1])
                continue
    elif base == 8:
        while True:
            entrada = num
            if num_validation(entrada):
                quant = len(entrada)

                if oct_validation(entrada)[0]:
                    print(calculo_oct_p_dec(entrada,quant))

                else:
                    print(oct_validation(entrada)[1])
                    continue

                break
            else:
                print(num_validation(entrada)[1])

                continue

#Hexadecimal

def hex_validation(numero):
    lista_numero = list(numero)
    for ind ,i in enumerate(lista_numero):
        if i == 'a' or i == 'A':
            lista_numero[ind] = 10
        elif i == 'b' or i == 'B':
            lista_numero[ind] = 11
        elif i == 'c' or i == 'C':
            lista_numero[ind] = 12
        elif i == 'd' or i == 'D':
            lista_numero[ind] = 13
        elif i == 'e' or i == 'e':
            lista_numero[ind] = 14
        elif i == 'f' or i == 'F':
            lista_numero[ind] = 15
            
    for i in lista_numero:
        if int(i)>15:
            return False, 'O número inserido não era hexadecimal.'
        else:
            continue
    return True, lista_numero

def calculo_hex_p_dec(entrada,quant):#Calculo de HEXA PARA DECIMAL
    resultado = 0
    tupla_entrada = hex_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(16**(i))
    return resultado

def calculo_dec_p_hexa(num):
    if num == '0':
        return f'O número {num} é igual a 0 em HEXADECIMAL'
    hexa = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 16
        decimal //= 16
        if resto == 10:
            hexa = 'A'+ hexa
        elif resto == 11:
            hexa = 'B'+ hexa
        elif resto == 12:
            hexa = 'C'+ hexa
        elif resto == 13:
            hexa = 'D'+ hexa
        elif resto == 14:
            hexa = 'E'+ hexa
        elif resto == 15:
            hexa = 'F'+ hexa
        else:
            hexa = str(resto) + hexa

    return num

def hexadecimal(num, base):
    if base == 10:    
        while True:
            entrada = num
            if num_validation(entrada):
                print(calculo_dec_p_hexa(entrada))
                break
            else:
                print(num_validation(entrada)[1])
                continue
    if base == 16:
        while True:
            entrada = num
            if True:
                quant = len(entrada)

                if hex_validation(entrada)[0]:
                    print(calculo_hex_p_dec(entrada,quant))

                else:
                    print(hex_validation(entrada)[1])
                    continue

                break

#Definindo qual o tipo de entrada

def entrada():
    try:
        while True:    
            opcao = input('R:')
            num_opcao = int(opcao)
            bi_para_decimal =  num_opcao == 1
            oct_para_decimal = num_opcao == 2
            hex_para_decimal = num_opcao == 3
            dec_para_binario = num_opcao == 4
            dec_para_octal = num_opcao == 5
            dec_para_hexa = num_opcao == 6
            if bi_para_decimal:
                return True
            elif oct_para_decimal:
                return True
            elif hex_para_decimal:
                return True
            elif dec_para_binario:
                return True
            elif dec_para_octal:
                return True
            elif dec_para_hexa:
                return True
            else:
                print('Você não digitou um número correspondente aos fornecidos.')
                continue
    except ValueError:
        print('Você não digitou um número')

# print(f"""{20*'-'}
# Calculado de BINARIO, OCTAL E HEXADECIMAL PARA DECIMAL
# {20*'-'}
# BINARIO P/ DECIMAL      (PRESS '1')
# OCTAL P/ DECIMAL        (PRESS '2')
# HEXADECIMAL P/ DECIMAL  (PRESS '3')
# DECIMAL P/ BINARIO      (PRESS '4')
# DECIMAL P/ OCTAL        (PRESS '5')
# DECIMAL P/ HEXADECIMAL  (PRESS '6') """)
        
# if entrada():
#     binario_dec()
# elif entrada():
#     octal_dec()
# elif entrada():
#     hexa_dec()
# elif entrada():
#     dec_binario()
# elif entrada():
#     dec_octal()
# elif entrada():
#     dec_hexa()