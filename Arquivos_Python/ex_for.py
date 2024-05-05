import random
lista = ['prego','falar','ouvir','jogar']
palavra = random.choice(lista)
x = 0
print(30*'=')
print('Adivinhe a palavra de 5 letras')
print(30*'=')
while True:
    a = input(f'({x}x)Digite a palavra: ').lower()
    letra_certa = 0
    local_certo = 0
    string = ''
    if len(a) == 5:   
        for i in a:
            if a[i] == palavra[i]:
                letra_certa+=1
                local_certo+=1
                print(f'A letra {a[i]} está certa e no local correto.')
            elif a[i] in palavra:
                print(f'A letra {a[i]} está certa, mas no local errado.')
                if a[i] == palavra[i]:
                    letra_certa+=1
            
        if local_certo == 5 and letra_certa == 5:
            print(len('Você acertou a palavra, parabéns!')*'=')
            print('Você acertou a palavra, parabéns!')
            print(len('Você acertou a palavra, parabéns!')*'=')
            break
        x+=1
    else:
        print('Digite 5 letras!')
    