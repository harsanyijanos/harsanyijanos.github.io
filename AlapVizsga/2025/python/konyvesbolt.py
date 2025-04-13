'''

'''
import os
cwd = os.getcwd()
fileFolder = cwd + '\\AlapVizsga\\2025\\python\\'


# a könyv osztály definiálása
class Konyv:
    def __init__(self, cim, mufaj, ar, darab):
        self.cim = cim
        self.mufaj = mufaj
        self.ar = ar
        self.darab = darab

# lista létrehozása a könyv objektumok tárolására
konyvek = []
# fájl megnyitása olvasásra
with open(fileFolder+'konyvek.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        sor = fr.readline()
        item = sor.replace('\n', '').split(';')
        k = Konyv(item[0], item[1], int(item[2]), int(item[3]))
        konyvek.append(k)

        
# hány fajta könyv volt a könyvesboltban
print(f'\n{len(konyvek)} fajta könyv van a könyvesboltban.')   

# számláláshoz és legdrágább könyv kereséséhez
# a változok előkészítése
sumOssz = 0     # összes könyv számlálása
sumKrimi = 0    # krimik számlálása
maxAruKonyv = konyvek[0] # a legdrágább könyv
for k in konyvek:
    sumOssz += k.darab
    if k.mufaj == 'krimi':
        sumKrimi += k.darab
    if k.ar > maxAruKonyv.ar:
        maxAruKonyv = k


# eredmények kiíratása
print(f'A könyvesboltban {sumOssz} darab könyv van.')
print(f'A könyvesboltban {sumKrimi} darab krimi van.')
print(f'A könyvesbolt legdrágább könyve: "{maxAruKonyv.cim}" {maxAruKonyv.ar} Ft\n')

with open(fileFolder+'rendeles.txt', 'w', encoding='utf-8') as fw:
    for k in konyvek:
        if k.darab < 3:
            fw.write(k.cim+'\n')
