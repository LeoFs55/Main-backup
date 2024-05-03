from copy import deepcopy

def alteracao_de_preco(lista):
    lista_alterada = [{'nome':i['nome'],'preco':(i['preco']*1.1)} for i in lista]
    novos_produtos = [deepcopy(i) for i in lista_alterada]
    return novos_produtos
