import random

num = random.randint(1, 50)
ct = 0

while True:
    guess = int(input("Introduceti un numar intre 1 si 50: "))
    if guess < num:
        print("Numarul este mai mare")
        ct += 1
    elif guess > num:
        print("Numarul este mai mic")
        ct += 1
    else:
        print("Felicitari! Ai ghicit din", ct, "incercari.")
        break
