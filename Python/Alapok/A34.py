"""
Feladat string és print témakör
karakterek megszámlálása 
egy megadott szövegben
Feladat: saját
"""

st = input('Adj meg egy szöveget: ')
str = st.lower()
print(f'{st} szöveg az alábbi karakterekből áll:')
while len(str)>0:
    ch = str[0]
    cnum = str.count(ch)
    print(f'\t\'{ch}\' karakternek {cnum} előfordulása')
    str = str[1:]
    str = str.replace(ch, '')
