
variante = ["piatra", "hartie", "foarfeca"]
def get_user_choice():
    while True:
        user_input = input("Alege piatra, hartie sau foarfeca: ").lower()
        if user_input in variante:
            return user_input
        else:
            print("Alegere invalida. Te rog să incerci din nou.")


while True:
    print("Jucator 1:")
    player1_choice = get_user_choice()
    
    print("Jucator 2:")
    player2_choice = get_user_choice()
    
    if player1_choice == player2_choice:
        print("Egalitate!")
    elif ((player1_choice == "piatra" and player2_choice == "foarfeca") or
            (player1_choice == "hartie" and player2_choice == "piatra") or
            (player1_choice == "foarfeca" and player2_choice == "hartie")):
        print("Jucător 1 castiga")
    else:
        print("Jucător 2 castiga")