'''
2. Dolgozat 10B B. csoport

páros- és páratlan négyzetösszege

'''

# Harsányi János

szum1 = 0
szum2 = 0
sz = 1
while sz!=0:
    sz = int(input("Adj meg egy egész számot! "))
    if sz%2==0:
        szum2 += sz*sz
    else:
        szum1 += sz**2
print("A páros számok négyzetösszege:", szum2)
print("A páratlan számok négyzetösszege:", szum1)