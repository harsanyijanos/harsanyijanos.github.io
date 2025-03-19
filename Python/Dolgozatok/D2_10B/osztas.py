'''
2. Dolgozat 10B B. csoport

maradékos osztás

'''
# Harsányi János

a = 1 
b = 2
while a!=b:
    a = int(input("Add meg az osztandót (egész szám)! "))
    b = int(input("Add meg az osztót (egész szám)! "))
    if a!=b:
        if a%b!=0:
            print(a, "/", b, "maradék", a%b)
        else:
            print("Nincs maradék!")
