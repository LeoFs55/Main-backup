p_valor = input('Digite um valor: ')
s_valor = input('Digite outro valor: ')
if p_valor > s_valor:
    print(f'O {p_valor=} é maior do que o {s_valor=}.')
elif p_valor < s_valor:
    print(f'O {p_valor=} é menor que o {s_valor=}.')
else:
    print(f'O {p_valor=} e {s_valor=} são iguais.')
    
""" tem como fazer isso aq
    print(
        f'O {p_valor=} é maior'
        f'do que o {s_valor=}.'
   legal
     )
"""