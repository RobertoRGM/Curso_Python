#Cálculos aritimeticos
n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz de {} quadrada de é {:.2f}!'.format(n,d,n,t,n,r))
#Opção 2
n = int(input('Digite um numero:'))
print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz de {} quadrada de é {:.2f}!'.format(n,(n*2),n,(n*3),n,(n**(1/2))))
