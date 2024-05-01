try:
    a = input('Digite um numero: ')
    b = input('Digite outro numero: ')
    a_int, b_int = float(a), float(b)
    c = a_int/b_int
    print(f'O resultado é {c}')
except ValueError:
    print('Você digitou uma letra.')