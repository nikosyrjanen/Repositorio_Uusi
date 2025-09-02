leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
luodit_total = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luodit_total * 13.3
kilogrammat = int(grammat // 1000)
jaljella_grammat = grammat % 1000
print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {jaljella_grammat:.2f} grammaa.")

#muutos