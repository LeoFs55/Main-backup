"""
Flag(Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)operador logico
id = identidade
"""

v1 = 62#a identificação do local da memoria q está alocado o v1
#print(id(v1))

condicao = True
x = None # Para verificar se o if foi executado 
if condicao:
    print('Faca algo')
    x=True
else:
    print('Não faça algo')

if x is None:
    print('Não passou no if')
elif x is not None:
    print('Passou no if')
