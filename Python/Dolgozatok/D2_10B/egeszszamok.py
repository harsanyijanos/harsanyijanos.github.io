'''
2. Dolgozat 10B B. csoport

pozitív- és negatív számok 
négyzetösszege

'''

# Harsányi János

pszum = 0
nszum = 0
sz = 1
while sz!=0:
    sz = int(input("Adj meg egy egész számot! "))
    if sz>0:
        pszum += sz*sz
    elif sz<0:
        nszum += sz**2
print("A pozitív számok négyzetösszege:", pszum)
print("A negatív számok négyzetösszege:", nszum)



