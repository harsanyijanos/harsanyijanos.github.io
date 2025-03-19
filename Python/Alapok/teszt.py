'''
4. Dolgozat 10B A. csoport

Adott számú egész véletlenszámot
generál két adott érték között, 
majd írassuk ki a számok összegét 
és átlagát 
'''


global lst 
lst = [5, 11, 8, 2, 5]

def novel():
    global lst
    for i in range(len(lst)):
        lst[i] +=1

novel()
print(lst)
