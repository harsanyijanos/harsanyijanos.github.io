"""
Egyszerű kiíratás gyakorlása
Kiíratandó:
    /
   /
  /
 /
/
Feladat: 9. Digitális kultúra
101. oldal 2. feladat
"""
# Megoldás: ciklus használata nélkül
print("    /")
print("   /")
print("  /")
print(" /")
print("/")

# Megoldás ciklussal
print()
for i in range(5):
    str = ""
    for j in range(5-i):
        str += " "
    str += "/"
    print(str)