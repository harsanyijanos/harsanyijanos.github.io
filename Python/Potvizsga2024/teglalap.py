'''
Téglalap kerületét, területét kiszámító program
Készítette: Harsányi János
'''
print('\nTéglalap kerületét és területét kiszámító program')
a = float(input("Kérem az egyik oldal nagyságát cm-ben: "))
b = float(input("Kérem a másik oldal nagyságát cm-ben: "))
k = 2*(a+b)
t = a*b
print(f"A megadott téglalap kerülete: {k} cm")
print(f"A megadott téglalap területe: {t} cm2\n")