#import calculo
from calculo import *
from notas import *

c = 10
d = 5

print(f'a soma de {c} e {d} é : {soma(c,d)}')

print(f'A subtração de {c} e {d} é : {sub(c,d)}')

show()

calculoMedia = calculaMedia(leG1(), leG2())
print('Calculo da sua nota',calculoMedia)
if calculoMedia >= 6: 
    print('passou')
else: 
    print('nao deu')

