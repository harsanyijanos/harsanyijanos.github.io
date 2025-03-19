'''
2. Dolgozat 10B A. csoport

nagyobb szám keresése

'''

# Harsányi János

a = 1 
b = 2
while a!=b:
    a = int(input("Adj egy egész számot! "))
    b = int(input("Adj egy másik egész számot! "))
    if a!=b:
        mx = max(a, b)
        print(a, "és", b, "közül a", mx, "nagyobb szám.")


