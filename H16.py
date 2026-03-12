import os
from datetime import date
print(f"Hello {os.getlogin()}")

print(f"Sinu kataloogitee{os.getcwd()}")
today = date.today()
print(today)
os.mkdir("str(today)")
try:
    os.mkdir(str(today))
except:
    print("ära jama, juba´olemas")

mitu = int(input("Mitu kataloogi tahad teha"))
for i in range(5):
    os.mkdir(str(today)+"/"+str(i+1))