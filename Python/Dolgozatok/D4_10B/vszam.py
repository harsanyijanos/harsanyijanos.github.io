'''
4. Dolgozat 10B A. csoport

Adott számú egész véletlenszámot
generál két adott érték között, 
majd írassuk ki a számok összegét 
és átlagát 
'''


import random

n = int(input("Hány véletlenszámot szeretnél? "))
a = int(input("Mi legyen a véletlen számok legkisebb értéke? "))
f = int(input("Mi legyen a véletlen számok lenagyobb értéke? "))

ah = min(a,f)
fh = max(a,f)

sum = 0
vszamok = []

for _ in range(n):
    rsz = random.randint(ah,fh)
    vszamok.append(rsz)
    print(f'A generált véletlenszám: {rsz}')

    sum += rsz

print(f'Véletlen számok: {vszamok}')
print(f'A véletlenszámok összege: {sum}')
print(f'A véletlenszámok átlaga: {sum/n:.2f}')