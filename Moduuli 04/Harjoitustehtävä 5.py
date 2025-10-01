oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
maksimi_yritykset = 5

while yritykset < maksimi_yritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {maksimi_yritykset - yritykset}")

    if yritykset == maksimi_yritykset:
        print("Pääsy evätty.")
