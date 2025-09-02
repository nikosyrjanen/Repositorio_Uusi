import random

code3 = ""
for _ in range(3):
    code3 += str(random.randint(0, 9))

code4 = ""
for _ in range(4):
    code4 += str(random.randint(1, 6))

print(f"Kolminumeroinen koodi: {code3}")
print(f"Nelinumeroinen koodi: {code4}")

#muutos