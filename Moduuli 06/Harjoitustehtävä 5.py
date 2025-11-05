def karsi_parittomat(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

def main():
    luvut = [3, 7, 10, 2, 5, 8, 11, 14]

    parilliset = karsi_parittomat(luvut)

    print("Alkuperäinen lista:", luvut)
    print("Karsittu lista (vain parilliset):", parilliset)

main()