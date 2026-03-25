import json

with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)

klass12 = 0
klass11 = 0
klass10 = 0
tegevused = []

for tulem in tulemused:
    #print(tulem['klass'])
    if tulem['klass'] == "12":
        print(tulem['nimi'])
        for aine,hinne in tulem['hinded'].items():
            print("\t",aine, hinne)
        klass12 += 1
        for tegevus in tulem['tegevused']:
            if tegevus not in tegevused:
                tegevused.append(tegevus)
    elif tulem['klass'] == "11":
        klass11 += 1
    else: 
        klass10 += 1


print(f"12. Klassis {klass12} õpilast")
print(f"11. Klassis {klass11} õpilast")
print(f"10. Klassis {klass10} õpilast")
for t in tegevused:
    print(t, end=", ")