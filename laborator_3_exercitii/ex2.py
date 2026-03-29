def genereaza_factura(nume_client, **kwargs):
    print(f"Factura pentru {nume_client}:")
    total = 0
    for produs, pret in kwargs.items():
        print(f"{produs}: {pret} lei")
        total += pret
    print(f"Total de plata: {total} lei")


genereaza_factura("Vali", cacao=10, lapte=8, cereale=3)