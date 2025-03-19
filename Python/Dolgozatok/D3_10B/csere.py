'''
3. Dolgozat 10B A. csoport

Bekért szövegben kicserélni
egy adott karaktert

'''

st = input("Adj meg egy szöveget! ")
ch = input("Add meg a kicserélendő karaktert! ")

print(st.replace(ch,'*'))

i = 0
nst = ""
while i<=len(st):
    if st[i]==ch:
        nst += st[i]
    else:
        nst += '*'

print(nst)
