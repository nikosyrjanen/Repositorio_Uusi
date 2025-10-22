kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i + 1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("Antamasi kaupungit ovat:")
for kaupungit in kaupungit:
    print(kaupungit)
