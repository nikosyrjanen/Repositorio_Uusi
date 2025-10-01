import random

salainen_luku = random.randint(1, 10)

print("Tervetuloa arvauspeliin!")
print("Tietokone on arponut luvun väliltä 1-10.")

while True:
    try:
        arvaus = int(input("Anna arvauksesi: "))
    except ValueError:
        print("Anna kokonaisluku, kiitos.")
        continue

    if arvaus > salainen_luku:
        print("Liian suuri arvaus.")
    elif arvaus < salainen_luku:
        print("Liian pieni arvaus.")
    else:
        print("Oikein! Hyvä arvaus.")
        break