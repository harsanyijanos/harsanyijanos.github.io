'''
4. Dolgozat 10B B. csoport

Derékszögűháromszög befogói
alapján kiszámítja az átfogót
Ezt addig ismétli amíg valamelyik 
befogó nem nulla vagy negatív szám.

'''

import math

b1 = 1
b2 = 2
while b1>0 and b2>0:
    b1 = float(input("Add meg a derékszögű háromszög befogóját! "))
    b2 = float(input("Add meg a másik befogót! "))
    if b1>0 and b2>0:
        a = math.sqrt(b1*b1 + b2*b2)
        print(f'A {b1} és {b2} befogójú derékszögű háromszög átfogója: {a:.2f}')


