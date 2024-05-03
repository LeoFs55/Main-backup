
val = 'Boi'

from .modulo_b import subtrair


def somar(n1,n2):
    resultado = int(n1+n2)
    return resultado

# print(subtrair(1,2))

#Validacao do numero

def num_validation(entrada):
    try:
        num = int(entrada)
        return True, num
    except ValueError:
        return False, ValueError        

#Binario

def bi_validation(numero):

    tupla_numero = tuple(str(numero))

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
    return binario

def binario(num, base):
    if base == 10:
            
        entrada = num
        if num_validation(entrada):
            return int(calculo_dec_p_bi(entrada))
        else:
            return num_validation(entrada)[1]

    elif base == 2:

        entrada = num
        if num_validation(entrada):
            quant = len(str(entrada))

            if bi_validation(entrada)[0]:
                return (calculo_bi_p_dec(entrada,quant))
            
            else:
                return bi_validation(entrada)[1]
            
        else:
                
            print(num_validation(entrada)[1])
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
        return 0
    octal = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal //= 8
    return octal

def calculo_oct_p_dec(entrada,quant):#Calculo de OCTAL PARA DECIMAL
    resultado = 0
    tupla_entrada = oct_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(8**(i))
    return resultado

def octadecimal(num, base):
    if base == 10:    
        entrada = num
        if num_validation(entrada):
            return int(calculo_dec_p_octal(entrada))
                
        else:
            return num_validation(entrada)[1]

    elif base == 8:
        entrada = num
        if num_validation(entrada):
            quant = len(entrada)

            if oct_validation(entrada)[0]:
                return int(calculo_oct_p_dec(entrada,quant))
            else:
                return oct_validation(entrada)[1]
        else:
            print(num_validation(entrada)[1])

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
        return 0
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

    return hexa

def hexadecimal(num, base):
    if base == 10:    
        entrada = num
        if num_validation(entrada):
            return calculo_dec_p_hexa(entrada)
        else:
            return num_validation(entrada)[1]

    if base == 16:
        entrada = num

        quant = len(entrada)
        if hex_validation(entrada)[0]:
            return int(calculo_hex_p_dec(entrada,quant))

        else:
            return hex_validation(entrada)[1]
