import random

def heita_noppa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

def main():
    tahkot = int(input("Anna nopan tahkojen määrä: "))

    silmaluku = 0
    while silmaluku != tahkot:
        silmaluku = heita_noppa(tahkot)
        print(silmaluku)

main()