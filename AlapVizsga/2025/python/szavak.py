'''

'''

szo = ''    # a bekért szó, induláskor üres

# ciklus a szavak beolvasására,
# amíg nem hosszabb mint 5 karakter
while len(szo)<5:
    # egy szó beolvasása
    szo = input('Adj meg egy szót: ')
print(f'\tA megadott szó "{szo}" {len(szo)} karakterből áll.')
print(f'\tA megadott szó visszafelé: "{szo[::-1]}"')