luvut = []

while True:
    syote = input("Anna luku (tai tyhjä lopettaaksesi): ")
    if syote == "":
        break

    luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua suuruusjärjestyksessä:")
for luku in luvut[:5]:
    print(luku)
