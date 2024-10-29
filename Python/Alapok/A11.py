"""
Egyszerű számítási feladat
Fogyasztás, megtett km alapján meghatározza
a fogyasztást
Feladat: Internetről
"""

# Adatok bekérése
km = float(input("Hány km-et mentél: "))
liter = float(input("Hány litert tankoltál: "))

# Fogyasztás kiszámítása
fogy = liter/km*100

# Eredmény megjelenítése
print("-----------------------------")
print("Ha", km, "-t mentél és", liter, \
      "-t tankoltál, akkor a fogyasztás", \
        round(fogy,2), "liter.")
