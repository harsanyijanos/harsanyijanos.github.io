"""
Feladat feltételes utasításra
nagykorúság vizsgálata
Feladat: Vali
"""

nev = input('Add meg a keresztnevedet! ')
kor = int(input('Add meg, hogy hány éves vagy! '))

if kor<18:
    print(nev, "te még kiskorú vagy.")
else:
    print(nev, "te már nagy korú vagy!")