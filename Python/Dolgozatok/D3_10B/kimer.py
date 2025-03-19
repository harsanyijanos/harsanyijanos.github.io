'''
3. Dolgozat 10B A. csoport

Termel mennyiségek kimérése
40 dkg-os adagokba
Feladat meghatározni 
a kapott adagszámot

'''

db = 0

while True:
    dkg = int(input("Add meg a gyártott mennyiséget [dkg]! "))
    if dkg <= 0:
        break
    db += dkg//40

print(f'{db} adag 40 dkg-os adagot kaptunk')