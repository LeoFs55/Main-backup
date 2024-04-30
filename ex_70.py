frase = 'Assine para desbloquear novos recursos e, se elegível, receba uma parte da receita dos anúncios.'.lower()
i = 0
qnt_letras = len(frase)
ap_mais = ''
qnt_mais = 0
while i < qnt_letras:
    letra_atual = frase[i]
    qnt = frase.count(letra_atual)
    if letra_atual == ' ':
        i+=1
        continue

    if qnt_mais < qnt:
        qnt_mais = qnt
        ap_mais = letra_atual
    i+=1

print(f'A letra q apareceu mais foi {ap_mais} sendo {qnt_mais}')