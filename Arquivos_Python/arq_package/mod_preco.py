from copy import deepcopy

def alteracao_de_preco(lista):
    novos_produtos_alterados = [{'nome':i['nome'],'preco':round(i['preco']*1.1,2)} for i in deepcopy(lista)]
    return novos_produtos_alterados
