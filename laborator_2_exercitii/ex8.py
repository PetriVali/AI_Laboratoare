
import time
tari_suspicioase = ["Coreea de Nord", "Siria", "Iran"]
tranzactii = []
while True:
    suma_tranzactie= float(input("Suma tranzactie:"))
    tara_tranzactie = input("Tara tranzactie:")
    tranzactie = {"suma": suma_tranzactie, "tara": tara_tranzactie, "timp": time.time()}
    tranzactii.append(tranzactie)
    if suma_tranzactie > 10000:
        print("Tranzactie suspicioasa: suma prea mare.")
    elif tara_tranzactie in tari_suspicioase:
        print("Tranzactie posibila frauduloasa: tara cu risc ridicat.")
    else:
        print("Tranzactie sigura.")
    tranzactii_recent = [t for t in tranzactii if time.time() - t["timp"] < 60]
    if len(tranzactii_recent) > 3:
        print("Atentie: posibila activitate de tip bot. Utilizator blocat.")
        break


