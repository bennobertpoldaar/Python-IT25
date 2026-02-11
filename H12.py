# pank depo ja väljavõte

def depo(s, r):
    uus = s + r
    return uus

def vv(s, r):
    uus = s - r
    return uus

saldo = 100

print(saldo)
saldo = depo(saldo, 10)
saldo = depo(saldo, 100)
saldo = depo(saldo, 1)
print(saldo)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 911)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
print(saldo)


# lambda näide
# 5l / 100km
# 200km
# L * KM / 100

kytus = lambda l, km: l * km / 100
print(kytus(5, 150))



# C > F
# F > C

def tempTeisendamine(t, k):
    """
    Teisendamine C -> F või F -> C.

    Parameetrid:
    t (str): "c" või "f"
    k (float): temperatuur

    Tagastab:
    float või string

    Näide:
    >>> tempTeisendamine("c", 19.45)
    """
    
    if t == "c":
        # F leidmine
        vastus = k * 9/5 + 32
    elif t == "f":
        # C leidmine
        vastus = (k - 32) / (9/5)
    else:
        vastus = "Ma ei mõista sind"
    
    return vastus


print(tempTeisendamine("c", 19.45))
print(tempTeisendamine("f", 19.45))
print(tempTeisendamine("blablablablablabla", 19.45))

print(tempTeisendamine.__doc__)