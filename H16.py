import os
from datetime import date
print(f"Hello {os.getlogin}")
print(f"Sinu kataloogitee: {os.getcwd()}")
today = date.today()
print(today)
try:
    os.mkdir(str(today))
except:
    print("ära jama, juba olemas")
    mitu = int(input("mitu kataloogi tahad teha: "))
    for i in range(mitu):
        os.mkdir(str(today)+"/"+str(i+1))
        print("Kataloogid 1-{mitu} tehtud")
    KUSTUTA = int(f"Kustuta valikust 1-{mitu}:")
    path = os.getcwd()+'\\'+str(today)+'\\'+kustuta 
    #print(path)
    if os.path.isdir(path):
        os.rmdir(path)