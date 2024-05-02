from math import sqrt
print(f'''
{32*'-'}
    Calculadora de perímetro
{32*'-'}
''')
res = 0
while True:
    entrada = input('Digite um numero: ')
    try:
        num = float(entrada)
        print('''
O que você gostaria de fazer com esse numero, digite o numero da operação:
Somar - 1/ Subtrair - 2/ Dividir - 3/ Multiplicar - 4/ Exponenciar - 5/ Raiz Quadrada - 6/ Resultado - 7/  Sair - 0''')
        operacao = input('R:')
        op_int = int(operacao)
        match op_int:
            case 0:
                print('Tchau!')
                break
            case 1:
                num_2 = float(input('Digite o outro numero:'))
                res += num+num_2
                print('Continuar - 1/ Sair - 0')
            case 2:
                num_2 = float(input('Digite o outro numero:'))
                res += num-num_2
                print('Continuar - 1/ Sair - 0')
            case 3:
                num_2 = float(input('Digite o outro numero:'))
                res += num/num_2
                print('Continuar - 1/ Sair - 0')
            case 4:
                num_2 = float(input('Digite o outro numero:'))
                res += num*num_2
                print('Continuar - 1/ Sair - 0')
            case 5:
                num_2 = float(input('Digite o outro numero:'))
                res += num**num_2
                print('Continuar - 1/ Sair - 0')
            case 6:
                res += sqrt(num)
                print('Continuar - 1/ Sair - 0')
            case 7:
                    print(f'O Resultado da(s) operações é {res}')
        saida = int(input('R: '))
        if op_int>7:
            print('Você não digitou um numero compativel com as opções.')
            continue
        elif saida == 0:
            print(f'O Resultado da(s) operações é {res}')
            break
    except:
        print('Você não digitou nenhum número. Volte do Inicio')
        print(20*'-')
        continue