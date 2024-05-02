while True:
    valor_str = input('Digite o valor da compra realizada pelo cliente: ')
    try:
        valor_float = float(valor_str)
        desconto_20 = valor_float>200
        if desconto_20:
            valor_float -= (valor_float*0.2)
            print(f'Por passar de R$200,00 o cliente recebeu 20% de desconto, logo o valor de sua compra é {valor_float}')
        else:
            print(f'O valor da compra do cliente é {valor_float}')
        break
    except:
        print('Você não digitou um número.')
        continue