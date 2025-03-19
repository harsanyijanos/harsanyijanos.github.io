'''
3. Dolgozat 10B B. csoport

Megadott hosszú rudak darabolása
30 cm-es darabokra
Meghatározni a kapott darabszámát

'''

db = 0

while True:
    hossz = int(input("Add meg a rúd hosszát! "))
    if hossz <= 0:
        break
    db += hossz//30

print(f'{db} db 30 cm-es darabot kaptunk')