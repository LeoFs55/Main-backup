import os
import re
import random
import sys
lista = [[],[],[10,9,8,7,6,5,4,3,2],[11,10,9,8,7,6,5,4,3,2]]
resultado_digito1= 0
resultado_digito2= 0
cpf_valido = ''
cabecalho = 'Validador de CPF'
# print(random.randint(111111112, 999999998))
# print(f"""
# {len(cabecalho)*'='}
# {cabecalho}
# {len(cabecalho)*'='}
def entrada_cpf(a):
    cpf_str = a
    primeiro_cpf_str = cpf_str[0]
    quantidade =len(cpf_str)
    str_repetida = primeiro_cpf_str*quantidade
    str_comp_igual = str_repetida == cpf_str
    global tupla_cpf
    tupla_cpf = ''
    if quantidade<9:
        print('Você não digotu um CPF completo, tente novamente.')
        return 1
    elif str_comp_igual:
        print('Você digitou um numero de CPF invalido!')
        return 2
    else:
        tupla_cpf = tuple(cpf)
        if len(tupla_cpf)>10:
            del tupla_cpf[-1]
            del tupla_cpf[-1]
        elif len(tupla_cpf)>9:
            del tupla_cpf[-1]
        return tupla_cpf
def primeiro_digito(a):
    for indice, i in enumerate(a):
        resultado = i*lista[2][indice]
        lista[1].append(resultado)
    for i in lista[1]:
        resultado_digito1+= i
    digito1 = resultado_digito1*10%11
    digito1 = digito1 if digito1 <= 9 else 0
    lista[1].clear()
    return digito1

def segundo_digito():
    resultado_digito2 = 0
    cpf_valido = ''
    for indice, i in enumerate(lista[0]):
        resultado = i*lista[3][indice]
        lista[1].append(resultado)
    for i in lista[1]:
        resultado_digito2+= i
    digito2 = resultado_digito2*10%11
    digito2 = digito2 if digito2 <= 9 else 0
    lista[0].append(digito2)
    for i in lista[0]:
        cpf_valido += f'{i}'
        return cpf_valido
# # Este programa tem o objetivo de identificar o primeiro dígito
# # do seu CPF.
# # """)
# entrada = input('Deseja entrar? Sim(S) ou Não(N): ').upper()
# if entrada == 'S':
#     os.system('cls')
while True:
    cpf = input('Digite seu CPF: ').replace('.','').replace('-','')
    if entrada_cpf(cpf) == 1:
        continue
    elif entrada_cpf(cpf) == 2:
        continue
    else:
        print(entrada_cpf(cpf))
        break
# primeiro_digito(tupla_cpf)
# print(primeiro_digito(tupla_cpf))
# segundo_digito()
# formato_cpf = f'{segundo_digito()[:3]}.{segundo_digito()[3:6]}.{segundo_digito()[6:9]}-{segundo_digito()[9:11]}'
# print(formato_cpf)
#     # print(formato_cpf)
    # lista[0].clear()
    # lista[1].clear()
    # cpf_valido = ''
# elif entrada == 'N':
#     print('Ok, tchau!')
# else:
#     print('Não entendi o que você disse, tente novamente!')

