"""
Verseny feladat
Egy adott szövegből törli a magánhangzókat
Megoldás rekurzív függvénnyel


"""

def isMaganhangzo(ch):
    if len(ch) == 0:
        return False
    
    mhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"

    if ch[0] in mhangzok:
        return True
    else:
        return False
    
def deleteMhangzok(st):
    if len(st)==0:
        return ""
    
    if isMaganhangzo(st):
        return deleteMhangzok(st[1:])
    else:
        return st[0]+deleteMhangzok(st[1:])

print(deleteMhangzok("amma"))
