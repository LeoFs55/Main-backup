produto = {'nome': 'Caneta Azul','preco': 2.5,'categoria': 'Escritorio'}

dc = {
    chave:valor.upper() 
    if isinstance(valor, str) else valor 
    for chave, valor in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
    ('d', 'valor d'),
    ('e', 'valor e'),
]

dc = {
    chave: valor
    for chave,valor in lista
}

s1 = {2 ** i for i in range(10) if i%2 == 1}
print(s1)