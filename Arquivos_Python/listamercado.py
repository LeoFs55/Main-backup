lista = []
quant = []
while True:

    try:

        operador = input('O que voce deseja fazer: Adicionar(A), Sair(S), Checar(C) ou Deletar(D): ').upper().strip()
        if operador == 'A': 
            item = input('Digite o nome do produto que deve ser comprado: ')
            lista.append(item)
            qnt = input(f'Digite a quantidade de {lista[-1]}: ')
            quant.append(qnt)

        elif operador == 'S':
            print('O que você deve comprar é: ')
            for indice, produto in enumerate(lista):
                print(f'{indice+1} - {produto} X {quant[indice]}')
            break

        elif operador == 'C':
            for indice, produto in enumerate(lista):
                print(f'{indice+1} - {produto} X {quant[indice]}')
                
        elif operador == 'D':
            try:
                for indice, produto in enumerate(lista):
                    print(f'{indice+1} - {produto} X {quant[indice]}')
                deletar = int(input('Digite o numero do item que deseja remover: '))
                listaremovido = lista.pop(deletar-1)
                quantremovido = quant.pop(deletar-1)
                print(f'Foi removido {listaremovido} X {quantremovido}')
            except:
                print('Não foi possivel apagar este indice')

        else:
            print('Você não digitou nenhuma respostar correspondente. Tente novamente!')
            continue

    except:

        print('Tente novamente!')
        continue