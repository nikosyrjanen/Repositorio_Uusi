vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if kuukausi == 12:
    indeksi = 0

else:
    indeksi = (kuukausi - 1) // 3

print(vuodenajat[indeksi])