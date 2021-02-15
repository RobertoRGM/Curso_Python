#Operações
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma vale {}, a subtração vale {}, a multiplicação vale {} e a divisão vale {:.2f}! '.format(s,sub,m,d), end='')
print('A divisão inteira vale {} e a potencia vale {}!'.format(di,p))
#{}:. e um numero seguido da letra f dentro dos colchetes define quantas casas decimais serão impressas
# End '' utlizado para que não pule linha de um print para o outro