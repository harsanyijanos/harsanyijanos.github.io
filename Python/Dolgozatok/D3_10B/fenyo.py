'''
3. Dolgozat 10B mindkét csoportnak

n sorú karácsonyfa kirajzolása
csillagokból

'''

n = int(input('Add meg a sorok számát! '))

i = 1
j = n
while i<=n:
    print(" "*j, "*"*i)
    i += 1
    j -= 1