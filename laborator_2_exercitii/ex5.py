import random

set_generator = set()
while len(set_generator) < 6:
    num = random.randint(1, 49)
    set_generator.add(num)

set_user = set()

print(set_generator)
    
while len(set_user) < 6:
    num = int(input("Introduceți un număr între 1 și 49: "))
    if 1 <= num <= 49:
        set_user.add(num)

ghicite = set_generator.intersection(set_user)

print("Numere ghicite:", ghicite)