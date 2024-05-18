import json
import os
caminho = 'Arquivos_Python\\pasta arquivo\\Lista_de_afazeres.json'
listas = {
    'lista_afazer': [],
    'lista_desfazer': [],
}

def entrada(tarefa):
    with open(caminho, 'r', encoding='utf8') as arq:
        try:
            lista = json.load(arq)
        except json.JSONDecodeError:
            lista = listas

    lista['lista_afazer'].append(tarefa)

    with open(caminho, 'w', encoding='utf8') as arq:
        json.dump(lista, arq, indent=3)
def leitura():
    with open(caminho, 'r', encoding='utf8') as arq:
        read = json.load(arq)

        lista = read['lista_afazer']
        if len(lista)>0:    
            print('Lista de Afazeres')
            for i in lista:
                print(f'-{i}')
        else:
            print('Lista de Afazeres vazia')
    print('='*30)

def desfazer():
    with open(caminho, 'r', encoding='utf8') as arq:
        lista = json.load(arq)

    if len(lista['lista_afazer'])>0:
        lista['lista_desfazer'].append(lista['lista_afazer'].pop())

    with open(caminho, 'w', encoding='utf8') as arq:
        json.dump(lista, arq, indent=3)
    

    
    return 'Nada pode mais ser desfeito'

def refazer():
    with open(caminho, 'r', encoding='utf8') as arq:
        lista = json.load(arq)

    if len(lista['lista_desfazer'])>0:
        lista['lista_afazer'].append(lista['lista_desfazer'].pop())
        
    with open(caminho, 'w', encoding='utf8') as arq:
        json.dump(lista, arq, indent=3)

    return 'Nada pode mais ser refeito'



leitura()

print('Comandos: listar, desfazer, refazer.')
print('Digite uma tarefa ou um comando', end='')
inp = input(':')
comandos = {
    'listar':lambda: leitura(),
    'desfazer':lambda: desfazer(),
    'refazer':lambda: refazer(),
    'adiconar':lambda: entrada(inp)
}
comando = comandos.get(inp) if comandos.get(inp) is not None else comandos['adiconar']
comando()

# if inp not in comandos:
#     tarefa = inp
#     entrada(tarefa)
#     os.system('cls')
#     leitura()
# elif inp in 'desfazer':
#         res = desfazer()
#         if res == None:
#             os.system('cls')
#             leitura()
#         print(f"""
# {'='*40}
# {res}
# {'='*40}""")
# elif inp == 'refazer':
#         res = refazer()
#         if res == None:
#             os.system('cls')
#             leitura()
#         else:
#             print(f"""
# {'='*40}
# {res}
# {'='*40}""")
# elif inp == 'listar':
#     os.system('cls')
#     leitura()
