#Teste Tipo
n = input('Digite')
print((type(n),(n.isalnum()),(n.isalpha()),(n.isnumeric()),(n.isupper())))
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços {}'.format(n.isspace()))
print('É um numero {}'.format(n.isnumeric()))
print('É alfabetico {}'.format(n.isalpha()))
print('É um alfanumerico {}'.format(n.isalnum()))
print('Esta em maiusculas {}'.format(n.isupper()))
print('Esta em minusculas {}'.format(n.islower()))
print('Esta capitalizada {}'.format(n.istitle()))

