'''
4. Dolgozat 10B A. csoport

Egyenlő szárú háromszög magasságát
számítjuk ki a háromszög alapja, 
és oldalhossza alapján.
A számítást addig ismételjük,
amig valamelyik adat nem nulla 
vagy negatív szám.
'''

import math

a = 1
b = 2
while a>0 and b>0:
    a = float(input("Add meg a háromszög alapjának hosszát! "))
    b = float(input("Add meg a háromszög oldalának hosszát! "))
    if a>0 and b>0:
        m = math.sqrt(b*b-(a/2)**2)
        print(f'A {a} alapú és {b} oldalhosszú háromszög magassága: {m:.2f}')


