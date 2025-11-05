def summa(lista):
    alku = 0
    for luku in lista:
        alku = alku + luku
    return alku

def main():
    luvut = [3, 7, 10, 2, 5]
    tulos = summa(luvut)
    print("Listan summa on:", tulos)

main()