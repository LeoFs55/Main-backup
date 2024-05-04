# def local(x):
#     a = x
#     def dentro():
#         print(dentro.__code__.co_freevars)
#         b = 2
#         return a
#     return dentro
# locals()
# dentro = local(10)
# print(locals())
# print('')
# print(globals())

def contatena(string_a):
    valor_final = string_a
    def interna(valor):
        nonlocal valor_final
        valor_final += valor
        return valor_final
    return interna

frase = contatena('a')
print(frase(''))
print(frase('b'))
print(frase('c'))
print(frase('d'))