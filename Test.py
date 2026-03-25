#ā€¢	Leia, mitu Ć¼ritust toimub Tallinnas.
#ā€¢	Leia kĆµik Ć¼ritused, mis toimuvad pĆ¤rast kellaaega 18:00.
#ā€¢	Leia kuu, kus toimub kĆµige rohkem Ć¼ritusi.
#ā€¢	Leia kĆµige varasem ja kĆµige hilisem Ć¼ritus kalendris.
#ā€¢	Loetle kĆµik Ć¼ritused, mis toimuvad nĆ¤dalapĆ¤eval "laupĆ¤ev" vĆµi "pĆ¼hapĆ¤ev".

import json
import requests
url = f"https://metshein.com/kordamine/json/uritused.json"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
events = data["uritused"]
tallinn_events = [e for e in events if e["koht"] == "Tallinn"]
print("Tallinnas üritusi:", len(tallinn_events))




