"""
Egyszerű számítási feladat
Három bekért egész szám közül a legkisebb és
a legnagyobb meghatározása
Feladat: saját
"""

# Adatok bekérése
print("---------------------------")
a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))
c = int(input("Add meg a harmadik számot: "))

# Eredmény kiíratása
print("---------------------------")
print("A három szám közül a legkisebb szám a(z)", min(a,b,c), \
      "a legnagyobb szám a(z)", max(a,b,c))
print("---------------------------")