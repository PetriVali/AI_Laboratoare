import random

inventory = []
print("Bine ai venit in padurea magica!")

while True:
    direction = input(
        "Alegeti directia (stanga/dreapta) sau 'iesire' pentru a parasi padurea: "
    ).lower()

    if direction == "iesire":
        print("Ai parasit padurea magica.")
        break
    elif direction == "stanga":
        event = random.choice(
            [
                "intalnirea unui lup",
                "descoperirea unei comori",
                "gasirea unui arbore cu fructe magice",
            ]
        )
        print(f"Ai ales sa mergi spre stanga. {event}.")

        if event == "descoperirea unei comori":
            inventory.append("comoara")
            print("Ai gasit o comoara! Ea a fost adaugata in inventar.")
        elif event == "gasirea unui arbore cu fructe magice":
            inventory.append("fructe magice")
            print("Ai gasit un arbore cu fructe magice! Ele au fost adaugate in inventar.")
        elif event == "intalnirea unui lup":
            print("Ai intalnit un lup! Din fericire, ai reusit sa scapi nevatamat.")
    elif direction == "dreapta":
        event = random.choice(
            [
                "intalnirea unui drac",
                "descoperirea unui rau magic",
                "gasirea unui pod de lemn",
            ]
        )
        print(f"Ai ales sa mergi spre dreapta. {event}.")

        if event == "descoperirea unui rau magic":
            inventory.append("rau magic")
            print("Ai gasit un rau magic! A fost adaugat in inventar.")
        elif event == "intalnirea unui drac":
            print("Ai intalnit un drac! Din fericire, ai reusit sa scapi nevatamat.")
        elif event == "gasirea unui pod de lemn":
            print("Ai gasit un pod de lemn! Ai trecut cu succes peste el.")
    else:
        print("Optiune invalida. Va rugam sa alegeti 'stanga', 'dreapta' sau 'iesire'.")

print("Inventarul tau:")
for item in inventory:
    print(f"- {item}")
