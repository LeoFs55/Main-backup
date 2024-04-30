name = 'Leonardo'
height = 1.78
weight = 103.2
imc = (weight/(height**2))
print(f'{name}, você com {weight}kg e {height:.2f}m o seu IMC(Indice de massa corporal) é {imc:.2f}') #Colocando :,.2f vc consegue fazer o bglh de dinheiro tipo: 1,000.40
print('{val1}, você com {val2}kg e {val3:.2f}m o seu IMC(Indice de massa corporal) é {val4:.2f}'.format (val1=name, val2=weight, val3=height, val4=imc)) #Mesma coisa só pra mim mais complicado só que é um método 
# Agora com paramentros que identifica a variavel alem do resultante do valor