#Carts
 #• Kuva ühe ostukorvi toodete nimed ja kogused (products) 
 #• Arvuta ostukorvide keskmine summa
#• Leia ostukorvide kogusumma (total) 
 #• Leia ostukorv, kus on kõige rohkem tooteid (totalProducts)

import requests

URL = "https://dummyjson.com/carts"
r = requests.get(URL)
data = r.json()
carts = data["carts"]
total_sum = 0
max_products = 0



for cart in carts:
    print("\nOstukorv:", cart["id"])
    product_count = 0
    for product in cart["products"]:
        print(product["title"], "-", product["quantity"])
        product_count += product["quantity"]
    total_sum += cart["total"]
    if product_count > max_products:
        max_products = product_count
        
average = total_sum / len(carts)   
print("keskmine summa", average)
print("kogusumma", total_sum)
print("Kõige rohkem tooteid ühes korvis", max_products)
    