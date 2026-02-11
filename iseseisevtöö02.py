# tere
import datetime
failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

nr = 1
for rida in fail:
    if nr == datetime.now().day:
        print(nr,rida, end="")
    nr = nr + 1

