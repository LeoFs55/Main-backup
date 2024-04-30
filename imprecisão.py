# Nessa aula ele aborta sobre a imprecisão de python em relação a numeros de ponto flutuante
import decimal
num_1 = 0.1
num_2 = 0.2
num_3 = num_1 + num_2
print(num_3)
num_1 = 0.1
num_2 = 0.7
num_3 = num_1 + num_2
print(F'{num_3:.2f}')
num_1 = 0.1
num_2 = 0.7
num_3 = num_1 + num_2
print(round(num_3,2))#(variavel, casas decimais)
num_1 = decimal.Decimal('0.1')#usado para numeros de ponto flutuante muito grandes e na situação correta
num_2 = decimal.Decimal('0.2')#é usado uma str para passar o numero e a função fazer todo o resto 
num_3 = num_1 + num_2
print(num_3)