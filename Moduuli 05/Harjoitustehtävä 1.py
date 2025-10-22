import random

maara = int(input("Kuinka monta aprakuutiota haluat heittää? "))

summa = 0

for i in range(maara):
    silmaluku = random.randint(1, 6)
    print(f"Heitto {i + 1}: {silmaluku}")
    summa += silmaluku

print(f"Silmälukujen summa on {summa}.")