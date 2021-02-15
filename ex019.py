#Escolhendo o aluno
from random import choice
aluno1 = str(input('Digite o nome do aluno1:'))
aluno2 = str(input('Digite o nome do aluno2:'))
aluno3 = str(input('Digite o nome do aluno3:'))
aluno4 = str(input('Digite o nome do aluno4:'))
lista = [aluno1,aluno2,aluno3,aluno4]
sorteio = choice(lista)
print('O aluno escolhido é o(a) {}'.format(sorteio))
