note_valide = list(range(1, 11))
nota = int(input("Introduceti o nota intre 1 si 10: "))

while nota not in note_valide:
    nota = int(input("Nota invalida. Va rugam sa introduceti o nota intre 1 si 10: "))

if nota < 5:
    print("Reexaminare")
elif nota <= 6:
    print("Suficient")
elif nota <= 8:
    print("Bine")
elif nota <= 10:
    print("Excelent")
