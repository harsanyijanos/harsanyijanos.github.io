'''
Hosszú szavakat leválogató program
Készítette: Harsányi János
'''
def hosszuszo(sz, n):
    return len(sz)>n


lst = []
while True:
    szo = input("Kérek egy szót! ")
    if szo == "":
        break
    lst.append(szo)

hossz = int(input("Hány betűnél hosszabb szó számít hosszú szónak? "))

hlst = []
db =  0

for szo in lst:
    if hosszuszo(szo, hossz):
        db += 1
        hlst.append(szo)

print(f"A megadott szavak között {db} db hosszú szó volt.")
print("Ezek a szavak: ", hlst)