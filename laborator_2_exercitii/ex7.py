cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urat", "prost", "groaznic", "dezamagitor"]

comentariu = input("Introduceti un comentariu: ")

for cuvant in comentariu.split():
    if cuvant.lower() in cuvinte_pozitive:
        print("Comentariu pozitiv")
    elif cuvant.lower() in cuvinte_negative:
        print("Comentariu negativ")
    else:
        print("Comentariu neutru")
