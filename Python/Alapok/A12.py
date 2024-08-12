"""
Egyszerű számítási feladat
Két egész szám maradékos osztása
Feladat: Internetről
"""

szam = int(input('\nOsztandó szám:'))
oszto = int(input('Osztó: '))
print()
print(szam, ':', oszto,'=', szam//oszto, ', maradék ', szam%oszto, \
    '\n',  sep='')