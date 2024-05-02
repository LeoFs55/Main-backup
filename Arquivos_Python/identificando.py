
nome = input('Digite seu nome: ')
nome_semespaço = nome.strip().replace(' ', '')
qnt_nome = len(nome_semespaço)
x = 0
y = ""
while x<qnt_nome:
    print(f'A {x+1}º letra do seu nome é {nome_semespaço[x]}')
    y+= '*'+nome_semespaço[x]
    x+=1
print(y)