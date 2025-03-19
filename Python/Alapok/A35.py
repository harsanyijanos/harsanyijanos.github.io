'''
math modul használata
a háromszög területének kiszámítása
az oldalak ismeretében
Feladat: saját
'''
import math

print('*'*40 + '\nHáromszög területének meghatározása\n a Hérón képlet segítségével\n\nAd meg a háromszög oldalainak hosszát:')

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

s = (a+b+c)/2
t2 = s*(s-a)*(s-b)*(s-c)

if t2<0: 
    print('\nA megadott oldalak nem alkotnak háromszöget!\n\n'+'*'*40)
else:
    t = math.sqrt(t2)
    print(f'\nA háromszög területe:{t:.3f}\n\n' + '*'*40)
