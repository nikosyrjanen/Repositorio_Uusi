while True:
    try:
        syote = input("Anna tuumamäärä (negatiivinen lopettaa): ")
        tuumat = float(syote)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")
        continue

    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit:.2f} cm.")