b = []
def soma(*args):#args empacota todos os agumentos colocados nele
    x = 0
    for i in args:
        x += i
    return x
for i in range(5):
    a = input('Digite um valor: ')
    b.append(int(a))
c = tuple(b)
print(soma(*c))