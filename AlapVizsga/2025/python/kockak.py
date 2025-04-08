'''

'''
import math

# függvény a kocka térfogatának kiszámítására
def terfogat(a):
    return a*a*a

# kockák számát bekérjük a konzolról
n = int(input(' Add meg a kockák számát: '))

# kockák élhosszának tárolása listába
# az üres lista előkészítése
kockak = []

# élhosszak beolvasása
for _ in range(n):
    a = float(input("Add meg a kocka élhosszát: "))
    kockak.append(a)

# megadott adatok listába kiíratása
print("\tA megadott élhosszak listája:", kockak)

print("Az egyes kockák adatai:")
for a in kockak:
    print(f'\télhossz: {a}; térfogat: {terfogat(a):.2f}; testátló: {math.sqrt(3)*a:.2f}')



