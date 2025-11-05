import math

def yksikkohinta(halkaisija_cm, hinta_euro):
    r_metreina = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * (r_metreina ** 2)
    return hinta_euro / pinta_ala

def main():
    print("Pizza 1")
    d1 = float(input("Halkaisija (cm): "))
    h1 = float(input("Hinta (euro): "))
    uh1 = yksikkohinta(d1, h1)

    print("Pizza 2")
    d2 = float(input("Halkaisija (cm): "))
    h2 = float(input("Hinta (euro): "))
    uh2 = yksikkohinta(d2, h2)

    print(f"Pizza 1 yksikköhinta: {uh1:.2f} €/m²")
    print(f"Pizza 2 yksikköhinta: {uh2:.2f} €/m²")

    if uh1 < uh2:
        print("Pizza 1 antaa paremman vastineen rahalle.")
    elif uh2 < uh1:
        print("Pizza 2 antaa paremman vastineen rahalle.")
    else:
        print("Pizzat ovat yhtä hyviä hinnaltaan.")

main()