#isinstance - verifica o objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item, isinstance(item, set))
    
    elif isinstance(item, str):
        print('Str')
        print(item, isinstance(item, str))

    elif isinstance(item,(int,float)):
        print('Num')
        print(item, isinstance(item,(int,float)))

    else:
        print('Outro')
        print(item)
    

# num = input('Digite um numero') Não verifica profundamente
# numero = int(num) if isinstance(num, int) else num

# print(numero, type(numero))
