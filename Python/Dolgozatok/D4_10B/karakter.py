'''
4. Dolgozat 10B b. csoport

Megadott elemű listát készít szavakból.
A szavak a konzulról kérjük be.
Ezután bekérünk egy karaktert, 
a listán szereplő szavak közül 
kiíratjuk azokat, amelyekben szerepel a 
megadott karakter
'''

n = int(input("Adja meg a szavak számát! "))

szavak = []
for _ in range(n):
    szo = input("Adj meg egy szót! ")
    szavak.append(szo)

ch = input("\nAdj meg egy karaktert! ")

vanszo = False

print(f'Szavak, amelyek tartalmazzák az {ch} karaktert:')
for szo in szavak:
    if ch.upper() in szo.upper():
        print(szo)
        vanszo = True

if not vanszo:
    print(f"Nincs a {ch} karaktert tartalmazó szó!")