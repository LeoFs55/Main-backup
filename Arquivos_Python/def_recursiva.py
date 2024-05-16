# def recursiva(inicio=0, fim=10):
#     print(inicio,fim)
#     inicio += 1
#     return recursiva(inicio,fim) if inicio <= fim else fim

# recursiva(0,1000)

def fatorial(num):
    if num <= 1:
        return 1
    
    return num * fatorial(num-1)
print(fatorial(2))
print(fatorial(3))
print(fatorial(4))
print(fatorial(5))
print(fatorial(6))
print(fatorial(7))
print(fatorial(8))
print(fatorial(9))
print(fatorial(998))