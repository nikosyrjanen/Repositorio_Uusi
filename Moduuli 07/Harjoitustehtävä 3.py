lentoasemat = {}

while True:
    print("\n(1) Syötä uusi lentoasema")
    print("(2) Hae lentoaseman tiedot")
    print("(3) Lopeta")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Koodia ei löydy.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta, yritä uudestaan.")