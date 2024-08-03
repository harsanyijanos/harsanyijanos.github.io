'''
Egész szám pozitivitásának vizsgálata
Készítette: Harsányi János
'''
egesz = int(input("Adj meg egy egész számot: "))
if egesz>0:
    print("A megadott szám pozitív!")
elif egesz<0:
    print("A megadott szám negatív!")
else:
    print ("A megadott szám nulla!")