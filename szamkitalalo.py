import random

print("Gondoltam egy számra 1 és 100 között. Találd ki!")
szam = random.randint(1, 100)
tipp = None
probalkozasok = 0

while tipp != szam:
    tipp = int(input("Add meg a tipped: "))
    probalkozasok += 1
    if tipp < szam:
        print("Túl kicsi!")
    elif tipp > szam:
        print("Túl nagy!")
    else:
        print(f"Gratulálok! {probalkozasok} próbálkozásból eltaláltad.")
            