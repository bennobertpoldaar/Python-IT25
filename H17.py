mehed_kokku = 0
mehed_tootunnid_kokku = 0
mehed_palk = 0

with open("tekst.txt", "a") as fail:
    rida = fail.read().split(",")
    tykeldus = rida.read()
    for r in tykeldus:
        print(r[3])