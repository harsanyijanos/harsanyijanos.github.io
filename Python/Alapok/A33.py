"""
Feladat string és print témakör
karácsonyfa csillagokból
Feladat: saját
"""
i = 1
n = int(input('Add meg a maximális csillagok számát! '))
while i<=n:
    print('*'*i)
    i += 1

print('\n'*3)

i = 1 
j = n//2+2
while i<=n:
    print(' '*j, '*'*(2*i-1), sep='')
    i += 1; j -= 1