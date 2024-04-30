nomes = []
idades = []
def maioridade(a): 
    if a>=18:
        idades.append(a)
        return 'você é maior de idade!'
    else:
        return 'você é menor de idade!'

def nome(a):
    nomes.append(a)
    return a

for i in range(5):   
    name = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    print(f'Olá {nome(name)} segundo meus calculos {maioridade(idade)}')
print(*nomes, sep='\n')
print(*idades, sep='\n')