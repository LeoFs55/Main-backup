while True:
    valor_str = input('Digite um numero de 0 à 9: ')
    try:
        valor_int = int(valor_str)
        v_valor = valor_int >= 0 and valor_int <= 9
        validation = 'Valor correto!' if v_valor else 'Valor incorreto!'
        print(validation)
        break
    except:
        print('Você não digitou um número.')
        continue