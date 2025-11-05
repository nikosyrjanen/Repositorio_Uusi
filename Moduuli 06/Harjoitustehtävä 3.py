def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def main():
    while True:
        gallonat = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))

        if gallonat < 0:
            break

        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.3f} litraa")

main()