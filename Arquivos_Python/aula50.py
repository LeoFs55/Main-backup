"""
CONSTANTES  = 'Variaveis' que não vão mudar e sõa definidas por variaveis que tem somente letras maiusculas
muitas condiçoes no mesmo if é ruim
e se o seu codigo está muito complexo é ruim(simples é melhor do que complexo)

"""
velocidade = 60
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
range_inicial = LOCAL_1 - RADAR_RANGE
range_final = LOCAL_1 + RADAR_RANGE
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= range_inicial and local_carro <= range_final
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

#Essa aula foi mais expecifica para já recomendar para diminuir o maximo que a parte 
#logica do código e deixar com a maior quantidade de variaveis 
