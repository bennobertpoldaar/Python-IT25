import csv


faili_nimi = 'EstonianBasketballGames.csv'

meeskonnad = {}

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    # Päise (header) lugemine
    pais = next(csv_lugeja)

    # print(f"Päise veerud: {pais}")
    for rida in csv_lugeja:
        meeskonnad[rida[1]] = 0
        
        # if rida[1] not in meeskonnad:
            # meeskonnad.append(rida[1])
        # if rida[2] not in meeskonnad:
            # meeskonnad.append(rida[2])
        # print(rida[1])

print(meeskonnad)
# print(f"Meeskonnad kokku: {len(meeskonnad)}")