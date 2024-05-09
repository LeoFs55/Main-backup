# def aleatoria(a=1,b=2):
#     def decorator(func):
#         def iner(a, b):#iner_funcion, iner, nested_funcion ou nested
#             res = func(a, b)
#             return res
#         return iner
#     return decorator
    

# @aleatoria(1,2)
# def soma(x,y):
#     return x+y

# dez_mais_cinco = soma
# print(dez_mais_cinco(a=1,b=3))


def arquivamento_de_tentativas(nome,outra_entrada):
    def decoradora(func):
        funcao = func
        def iner(entrada):
            argumantos = entrada
            with open('Arquivos_Python\\arquivo.txt','a') as pagina:
                pagina.write(f'Funcao executada: {nome}. Argumento:({argumantos}).Resultado 1 {func(entrada)} Resultado2 {func(outra_entrada)}\n')
            return func(entrada)
        return iner
    return decoradora

# @arquivamento_de_tentativas(nome='Calculo para Binario')
# def calculo_dec_p_bi(num):
#     if num == '0':
#         return num
#     binario = ''
#     decimal  = int(num)
#     while decimal > 0:
#         resto = decimal % 2
#         binario = str(resto) + binario
#         decimal //= 2
#     return binario
@arquivamento_de_tentativas(nome='Calculo para decimal2',outra_entrada='101010')
@arquivamento_de_tentativas(nome='Calculo para decimal',outra_entrada='1010')
def calculo(entrada):
    resultado = 0
    lista_de_entrada = [int(i) for i in entrada if int(i)<= 1]
    for ind, i in enumerate(reversed(lista_de_entrada)):
        resultado += (i)*(2**ind)
    return resultado

funcao_binaria_com_arquivamento1 = calculo
funcao_binaria_com_arquivamento1('10')
# funcao_binaria_com_arquivamento2 = calculo_dec_p_bi
# print(funcao_binaria_com_arquivamento2('10'))

