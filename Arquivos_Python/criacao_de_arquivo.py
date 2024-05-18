import os
caminho = 'Arquivos_Python\\pasta arquivo\\'
caminho += 'aquivo_criado.txt'

# arquivo = open(caminho,'w')
# #
# arquivo.close()
# oi = ( f'{i}\n' for i in range(2))
with open(caminho,'w+',encoding='utf-8') as arquivo:
    arquivo.write('Olá mundo\n')
#     arquivo.write('IDIOTA\n')
#     arquivo.writelines(oi)
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     arquivo.seek(0,0)
#     print(arquivo.readline(),end='')
#     print(arquivo.readline().strip())
with open(caminho,'r',encoding='utf-8') as arquivo:
    print(arquivo.read())

with open(caminho,'a+',encoding='utf-8') as arquivo:
    arquivo.write('Olá mundo2\n')

with open(caminho,'r',encoding='utf-8') as arquivo:
    print(arquivo.read())
#os.remove(caminho)
os.rename(caminho,'Arquivos_Python\\pasta arquivo\\Vaisefoder.txt')
