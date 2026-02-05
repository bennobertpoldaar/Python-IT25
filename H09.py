for i in range(11):
    print(f"{i} * {i} = {i*i}")
import random
    
    
tehe = ["+","-","*","/"]

for _ in range(10)("kysimuste_arv"):
    arv1 = random.randint(1,10)
    arv2 = random.randint(1,10)
    t = random.choice(tehe)
    
    

    if t=="+":
        print(f"{arv1}{t}{arv2}={arv1 + arv2}")
        v = int(input("VASTUS: "))
        if arv1*arv2 == v:
            punktid+=1
    elif t=="-":
        print(f"{arv1}{t}{arv2}={arv1 - arv2}")
        v = int(input("VASTUS: "))
        if arv1*arv2 == v:
            punktid+=1
    elif t== "*":
        print(f"{arv1}{t}{arv2}={arv1 * arv2}")
        v = int(input("VASTUS: "))
        if arv1*arv2 == v:
            punktid+=1
    else:
        print(f"{arv1}{t}{arv2}={arv1 / arv2}")
        v = float(input("VASTUS:  "))
        if arv1*arv2 == v:
            punktid+=1
            
print(punktid/kysimuste_arv)
if punktid/kysimuste_arv >= 0.5:
    print("A")
else:
    print("MA")
    