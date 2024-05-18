import json
# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# caminho = 'Arquivos_Python\\pasta arquivo\\'
caminho = 'Arquivos_Python\\pasta arquivo\\aula117.json'
# with open(caminho,'w',encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo,indent=3)
with open(caminho,'r',encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
