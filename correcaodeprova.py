import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': 'c',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': 'a',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': 'b',
    },
]
alternativas = ['a','b','c','d']
def perguntar(quest,option,tl_options,aswer):
    print(quest)
    resp = aswer
    for i, op in enumerate(option):
        print(f'{tl_options[i]}){op}')

    if resp == input('Digite a alternativa CORRETA: '):
        os.system('cls')
        return 'CERTA'
    else:
        os.system('cls')
        return 'ERRADA'
    
pergunta_1 = perguntar(quest=perguntas[0]['Pergunta'],option=perguntas[0]['Opções'],tl_options=alternativas,aswer=perguntas[0]['Resposta'])
pergunta_2 = perguntar(quest=perguntas[1]['Pergunta'],option=perguntas[1]['Opções'],tl_options=alternativas,aswer=perguntas[1]['Resposta'])
pergunta_3 = perguntar(quest=perguntas[2]['Pergunta'],option=perguntas[2]['Opções'],tl_options=alternativas,aswer=perguntas[2]['Resposta'])

print(f'''GABARITO:
A Resposta 1 está {pergunta_1}!
A Resposta 2 está {pergunta_2}!
A Resposta 3 está {pergunta_3}!
''',sep='')