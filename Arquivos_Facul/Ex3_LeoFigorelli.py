while True:
    horas_str = input('Digite um valor em horas: ')
    try:
        hora_int = int(horas_str)
        minuto_int = hora_int*60
        print(f'O valor digitado de {hora_int} horas é igual a {minuto_int} minutos.')
        break
    except:
        print('Você não digitou um número.')
        continue
    