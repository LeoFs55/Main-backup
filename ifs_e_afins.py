# if / elif / else
# se / se não se / se não
'''entrada = input('Você quer "entrar" ou "sair"? ')
entrada = entrada.lower()
if entrada == 'entrar':
    print('Você entrou!')
    entrada2 = input('Você quer continuar entrando "entrar" ou "sair"? ')
    if entrada2 == 'entrar':
        print('Você entrou!')
    elif entrada2 == 'sair':
        print('Você saiu!')
    else:
        print('Você não digitou nem "entrar" nem  "sair". ')  
elif entrada == 'sair':
    print('Você saiu!')
else:
    print('Você não digitou nem "entrar" nem  "sair". ')
'''
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')
