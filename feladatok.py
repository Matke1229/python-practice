print('Az 1-es szám megadásával számokat írhat be, amiket a program összead és kiadja az eredményt, majd egy másik sorban leírja az átlagukat.')
print('A 2-es szám megadásával megadhat egy számot, amiről a program eldönti, hogy páros vagy páratlan-e.')
print('A 3-as szám megadásával megadhat egy számot és a program kiszámítja annak a számnak a faktoriálisát.')
print('A 4-es szám megadásával megadhat egy szót, amit kiír a program megfordítva.')
print('Az 5-ös szám megadásával a program bekér számokat, majd csökkenő sorrendbe rendezi') #fgv használata nélkül

megadott_szam = int(input('\nKérem adja meg a kívánt mód számát!  '))

def szamlalo():
    szamok = []
    while(szam := (input('Adjon meg számokat, ha nem szeretne többet megadni, üssön entert!  '))) != '':
        szamok.append(int(szam))
    osszeg = 0
    db = 0
    for szam in szamok:
        osszeg += szam
        db += 1
    atlag = round(osszeg/db, 2)
    print(f'A megadott számok összege: {osszeg}')
    print(f'A megadott számok átlaga: {atlag}')

def paritas():
    szam = int(input('Kérek egy számot!  '))
    if szam % 2 == 0:
        print('A szám páros')
    else:
        print('A szám páratlan')

def faktorialis():
    szam = int(input('Kérek egy számot!  '))
    faktorialis = 1
    while szam > 0:
        faktorialis *= szam
        szam -= 1
    print(f'A megadott szám faktoriálisa: {faktorialis}')

def megfordito():
    szo = input('Kérek egy szót!  ')
    betuk = []
    db = -1
    for betu in szo:
        betuk.append(betu)
        db += 1
    fordit = []
    while db > -1:
        fordit.append(betuk[db])
        db -= 1
    print(''.join(fordit))
    
def rendezo():
    szamok = []
    while(szam := (input('Adjon meg számokat, ha nem szeretne többet megadni, üssön entert!  '))) != '':
        szamok.append(int(szam))
    sorrend = []
    for i in range(len(szamok)):
        leg = 0
        for szam in szamok:
            if szam > leg:
                leg = szam
        sorrend.append(str(leg))
        szamok.remove(leg)
    print(' > '.join(sorrend))

if megadott_szam == 1:
    szamlalo()
elif megadott_szam == 2:
    paritas()
elif megadott_szam == 3:
    faktorialis()
elif megadott_szam == 4:
    megfordito()
elif megadott_szam == 5:
    rendezo()