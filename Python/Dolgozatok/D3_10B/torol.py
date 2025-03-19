'''
3. Dolgozat 10B B. csoport

Bekért szövegből kitöröl 
egy adott karaktert

'''

st = input("Adj meg egy szöveget! ")
ch = input("Add meg a törlendő karaktert! ")

print(st.replace(ch,''))

i = 0
nst = ""
while i<len(st):
    if st[i] != ch:
        nst += st[i]
    i += 1

print(nst)
