"""
Egyszerű számítási feladat
Megadott másodperceket átszámolja
óra, perc, másodpercbe
Feladat: Vali
"""

timeSec =int(input('Add meg az időt másodpercben! '))

sec = timeSec%60
timeSec //=60
min = timeSec%60
ora = timeSec//60

print("Ez", ora, "óra,", min, "perc,", sec, "másodperc")
