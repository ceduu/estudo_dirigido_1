import math


metros_a_pintar = int(input('Qual o tamanho a pintar '))

litros_necessarios = (metros_a_pintar / 6)


print('ESSAS SÃO AS SUAS OPÇÕES DE COMPRA :')



#questão a)
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_lata = (latas_necessarias * 80)
print('Você precisará de',latas_necessarias,'lata(s) e pagará ',preco_lata)



#questão b)
galoes_necessarios = math.ceil(litros_necessarios / 3.6)
preco_galoes = (galoes_necessarios * 25)
print('Você precisará de',galoes_necessarios,   'galõe(s) e pagará ', preco_galoes)

#questão c)
latas_necessarias = int(litros_necessarios / 18)
faltou = litros_necessarios % 18
galoes_necessarios = math.ceil(faltou / 3.6)
preco_lata = (latas_necessarias * 80)
preco_galoes = (galoes_necessarios * 25)
preco_galoes_e_latas = (preco_lata + preco_galoes)
print('Voce precisará de',latas_necessarias, 'lata(s)','e de', galoes_necessarios ,'galõe(s) e pagará ', preco_galoes_e_latas)

