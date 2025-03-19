'''
4. Dolgozat 10B a. csoport

Megadott elemű listát készít szavakból.
A szavak a konzulról kérjük be.
Ezután bekérünk egy karaktert, 
a listán szereplő szavak közül 
kiíratjuk azokat a szavakat, amelyekben 
az első karakter megegyezik az adott 
karakterrel
'''

n = int(input("Adja meg a szavak számát! "))

szavak = []
for _ in range(n):
    szo = input("Adj meg egy szót! ")
    szavak.append(szo)

ch = input("\nAdj meg egy karaktert! ")

vanszo = False

print(f'Szavak, amelyek első karaktere {ch}:')
for szo in szavak:
    if ch.upper() == szo[0].upper():
        print(szo)
        vanszo = True

if not vanszo:
    print(f"Nincs {ch} karakterrel kezdődő szó!")