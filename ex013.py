#Calculo de aumento de salário
s = float(input('Digite o salário do funcionário R$:'))
a = float(input('Digite a % de aumento'))
pa = a/100
ns = s + (s * pa)
print('Novo salário com {}% de aumento é R$ {:.2f}'.format(a,ns))
#Opção 2
ns = s + (s * a / 100)
print('Novo salário com {}% de aumento é R$ {:.2f}'.format(a,ns))

