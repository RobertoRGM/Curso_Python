#Calculo seno, cosseno e tangente
import math
num = float(input('Digite o angulo°:'))
seno = math.sin(math.radians(num))
coss = math.cos(math.radians(num))
tang = math.tan(math.radians(num))
print('O seno, cosseno e a tangete do angulo {} são: {:.2f}, {:.2F} e {:.2f} '.format(num,seno,coss,tang))
## Os graus estão em centigrados para transforma-los foi necessário utilizar a função math.radians para converte-lo para radioanos