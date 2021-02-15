#Custo de locação
k = float(input('Informe a quantidade de kilometros percorridos KM:'))
d = int(input('Informe a quantidade de dias alugado'))
p = (k * 0.15) + (d * 60)
print('O valor a pagar por {} dias de aluguel e por {:.2f}km percorridos é R${:.2f}'.format(d,k,p))
