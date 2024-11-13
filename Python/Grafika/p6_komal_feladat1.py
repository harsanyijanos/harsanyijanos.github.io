def feladat(a,b):
    na=len(a)
    n=nb=len(b)
    if na<n:
        n=na
    c=''
    for i in range(n):
        if a[i]==b[i]:
            c+=a[i]
        else:
            c+='_'
    return c


print(feladat('almar','elmeri'))