while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break

    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")

    if luvut:
        pienin = min(luvut)
        suurin = max(luvut)
        print(f"Pienin luku: {pienin}")
        print(f"Suurin luku: {suurin}")
    else:
        print("Yhtään lukua ei syötetty.")