from itertools import groupby
from pprint import pprint
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(dict):
    return dict['nota']

alunos_agrupados = sorted(alunos, key=ordena) #a lambda aq serve para retonar para a funcao do 
#sorted que o valor recebido será o da nota, pq sem ele estaria pegando os dois valores do dict
grupos = groupby(alunos_agrupados, key=ordena)
for chave,grupo in grupos:
    print(chave)
    pprint(list(grupo))