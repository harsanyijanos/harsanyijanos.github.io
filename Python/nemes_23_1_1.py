
def inpNumber(ksz, ah, fh):
    kiiras = f'{ksz} [{ah},{fh}]: '
    while True:
        sz = int(input(kiiras))
        if sz<ah or sz>fh:
            print("A megadott értek nem esik az adott intervallumba! Add meg újra!")
            continue
        return sz
    
def inpList(ksz, ah, fh, n):
    kiiras = f'{ksz} ({n} db) [{ah},{fh}]: '
    while True:
        szoveg = input(kiiras)
        strNumber = szoveg.split(',')
        if len(strNumber)!=n:
            print("Nem a kellő számú adatot adtad meg! Add meg újra!")
            continue
        numbers = []
        isInterv = True
        for sz in strNumber:
            number = int(sz) 
            if number<ah or number>fh:
                isInterv = False
                break
            numbers.append(number)
        if not isInterv:
                print("A megadott értek nem esik az adott intervallumba! Add meg újra!")
                continue
        return numbers


import time

startTime = time.time()
print(inpList("értek", 1, 9, 3))
endTime = time.time()
print("Futási idő:", endTime-startTime)
    

