#Calculo de desconto
p = float(input('Digite o preço do produto R$:'))
d = float(input('Digite a % de desconto:'))
d1 = d/100
np = p - (p * d1)
print('O novo preço com {}% de desconto é R${:.2f}'.format(d,np))
#Opção 2
np = p - (p * (d/100))
print('O novo preço com {}% de desconto é R${:.2f}'.format(d,np))
