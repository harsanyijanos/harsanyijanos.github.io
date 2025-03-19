'''
math modul használata
másodfokú egyenlet megoldása
Feladat: saját
'''

from math import sqrt

print('*'*35 + '\nMásodfokú egyenlet megoldása:\n')
a =float(input('Add meg az \'a\' együtthatót: '))
b =float(input('Add meg az \'b\' együtthatót: '))
c =float(input('Add meg az \'c\' együtthatót: '))

if a==0:
    print('\n Ez nem másodfokú egyenlet!\n\n'+'*'*35)
else:
    d = b*b - 4*a*c
    if d>0:
        x1 = (-b + sqrt(d))/2/a
        x2 = (-b - sqrt(d))/2/a
        print(f'\nA másodfokú egyenlet gyökei:\nx1={x1:.2f} és x2={x2:.2f}\n\n'+'*'*35)
    elif d<0:
        print('\n Az egyenletnek nincs valós megoldása!\n\n'+'*'*35)
    else:
        x1 = -b/2/a
        print(f'\nA másodfokú egyenletnek két megegyező gyöke van:\nx1=x2={x1:2f}\n\n' /
              +'*'*35)
