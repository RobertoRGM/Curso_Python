#Conversor de moeda
carteira = float(input('Quanto você tem na carteira em R$:'))
cotacao = float(input('Digite a cotação do dólar'))
conversao = carteira / cotacao
print('Com R$ {:.2f} você pode comprar $ {:.2f}!'.format(carteira,conversao))

