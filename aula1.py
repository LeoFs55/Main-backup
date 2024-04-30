"""
A eu gostaria de te mandar tomar no  cu fazendo o querido favor
*comentario multilinha*DOC STRING - o pyhton lê essa porra
"""
'''
mesma coisa q a de cima
'''
# Comentário bla bla
# print('Olá, mundo!') # Comentário
# Comentário
# os trei tipos são comentarios os com ' ou " o python lê  mas o # não
# print('=P')

def numero(a,b):
    def somar(a,b):
        def multiplicar_soma(a,b):
            mult = a*b
            return mult
        soma = a + b
        multiplicador = int(input('Insira o multiplicador: '))
        return multiplicar_soma(soma, multiplicador)
    a_int = int(a)
    b_int = int(b)
    return somar(a_int, b_int)

print(numero(2,3))