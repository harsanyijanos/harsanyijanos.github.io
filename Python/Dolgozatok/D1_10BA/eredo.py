'''
1 Dolgozat 10B A. csoport

Ellenállások eredőjének meghatározása
'''

# Harsányi János

R1 = float(input('Add meg a R1 eredő értékét [Ohm]! '))
R2 = float(input('Add meg a R2 eredő értékét [Ohm]! '))
Rs = R1 + R2
Rp = R1 * R2 / Rs
print()
print('Eredő soros kapcsolás esetén:',round(Rs,3), 'Ohm')
print('Eredő párhuzamos kapcsolás esetén:',round(Rp,3), 'Ohm')
print()