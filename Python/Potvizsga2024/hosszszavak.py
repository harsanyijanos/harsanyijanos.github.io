'''
Hosszú szavakat leválogató program
Készítette: Harsányi János
'''
def hosszuszo(sz, n):
    return len(sz)>n


szavak = []
while True:
    szo = input("Kérek egy szót! ")
    if szo == "":
        break
    szavak.append(szo)

hossz = int(input("Hány betűnél hosszabb szó számít hosszú szónak? "))

hosszuak = []
db =  0

for szo in szavak:
    if hosszuszo(szo, hossz):
        db += 1
        hosszuak.append(szo)

print(f"A megadott szavak között {db} db hosszú szó volt.")
print("Ezek a szavak: ", hosszuak)