alamitta = 37

pituus = int(input("Anna kuhan pituus (cm): "))

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen! Se on {puuttuu} cm liian lyhyt.")

else:
    print("Kuha on sallittua pyyntikokoa. Hyvää kalansaalista!")
