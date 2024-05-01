import os
try:
    a = 10
    b = 1#0 ->ZeroDivisionError
    c = a/b#[0]#-> Exception(Capturou qualquer erro possivel) mas tambem pode ser o TypeError
    # c = int('') ->ValueError
    print(f'O resultado é {c}')#[100])#-> IndexError e entra do 3° pq ele tambem está lá
except ValueError:
    try:
        print('Você digitou uma letra.')
    except:
        ...
except ZeroDivisionError:
    print('Você dividiu por 0.')
except (TypeError,IndexError) as error:
    print('TypeError ou IndexError')
    print('Msg:',error)
    print('Name:',error.__class__.__name__)
except Exception as error:
    print(f'ERRO :{error}')
except TypeError:#Nenhum erro será expecificado dps do Exception
    print('ERRO Desconhecido')
else:
    print('Não deu erro')
finally:
    print('ACABOU')
