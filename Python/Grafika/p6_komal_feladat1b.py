def ohason(ac,bc):
    if ac==bc:
        return ac
    else:
        return '_'

def feladat(a,b):
    if a=='' or b=='':
        return ''
    return ohason(a[0],b[0]) + feladat(a[1:],b[1:])      
    

print(feladat('almar','elmeri'))
print(feladat('','elmeri'))