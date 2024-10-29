"""
Feladat feltételes utasításra
Két időpont között eltelt idő meghatározása
Feladat: Internet
"""

# Adatok bekérése
print('-----------------------------------')
print('Add meg!')
ora1 = int(input('Első időpont - óra: '))
perc1 = int(input('Első időpont - perc: '))
ora2 = int(input('második időpont - óra: '))
perc2 = int(input('második időpont - perc: '))

# Számítás
ora = ora2-ora1
perc = perc2-perc1
if perc<0:
    ora -= 1
    perc += 60

# Eredmény megjelenítése
print('-----------------------------------')
if ora<0:
    print('Hibás adatot adtál meg!')
elif ora==0:
    print(f"{ora2}:{perc2}-{ora1}:{perc1} között {perc} perc telt el.")
else:
    print(f"{ora2}:{perc2}-{ora1}:{perc1} között {ora} óra {perc} telt el.") 

print('-----------------------------------')
