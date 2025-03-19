'''
random modul használata
egy véletlen egész szám kitalálása
Feladat: saját
'''

import random

vszam = random.randint(1,10)

print('*'*45 + '\nGondoltam egy számra 1 és 10 között.\n Találd ki a számot!\n')

while True:
    sz = int(input('\nTippelj egy egész számot 1 és 10 között! '))

    if sz<1 or sz>10:
        print('A szám nem esik 1 és 10 közé!')
        continue

    if sz<vszam:
        print('Túl kis számot adtál meg!')
    elif sz>vszam:
        print('Túl nagy számot adtál meg!')
    else:
        print('Eltaláltad a számot amire gondoltam!\n\n'+'*'*45)
        break