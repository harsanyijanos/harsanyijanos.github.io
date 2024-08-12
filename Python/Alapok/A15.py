"""
Egyszerű számítási feladat
Meghatározza a négyzet oldala alapján
a négyzet kerületét
Feladat: Vali
"""

oldal = float(input('\nAdd mega négyzet oldalhosszát cm-ben! '))
kerulet = 4*oldal
terulet = oldal**2

print(oldal, 'cm-es négyzet kerület:', kerulet, \
      'cm  területe:', terulet, 'cm2\n')