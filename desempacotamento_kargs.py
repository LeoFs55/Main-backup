# nome, sobrenome = pessoa
# print(nome, sobrenome)

# nome, sobrenome = pessoa.values()
# print(nome, sobrenome)

# nome, sobrenome = pessoa.items()
# print(nome, sobrenome)

# (chave,nome), (chave2,sobrenome) = pessoa.items()
# print(chave,':',nome,chave2,':',sobrenome)

# for chave, valor in pessoa.items():
#     print(chave, valor)
nome_pessoa = {'nome':'Leonardo', 'sobrenome':'Figorelli Santana'}
dados_pessoa = {'idade': 18, 'altura': 1.78}

pessoa_completa = {**nome_pessoa, **dados_pessoa}
# print(pessoa_completa)

def mostrar(*args,**kwargs):
    print(f'Não nomeados: {args}')

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar(**pessoa_completa)

