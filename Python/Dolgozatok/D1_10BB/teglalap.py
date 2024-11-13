'''
1 Dolgozat 10B B. csoport

Téglalap kerületének, területének meghatározása
'''

# Harsányi János

a = float(input('Add meg a téglalap egyik oldal hosszát [cm]! '))
b = float(input('Add meg a téglalap másik oldal hosszát [cm]! '))
K = 2*(a+b)
T = a*b
print()
print('Téglalap kerülete:',round(K,3), 'cm2')
print('Téglalap területe:',round(T,3), 'cm2')
print()