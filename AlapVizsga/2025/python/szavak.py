'''

'''

szo = ''    # a bekért szó, induláskor üres

# ciklus a szavak beolvasására,
# amíg nem hosszabb mint 5 karakter
while len(szo)<5:
    # egy szó beolvasása
    szo = input('Adj meg egy szót: ')
print("Az ellenőrzött bekérés sikeres!\n")
print(f'A megadott szó "{szo}" {len(szo)} karakterből áll.')
print(f'A megadott szó visszafelé: "{szo[::-1]}"\n')