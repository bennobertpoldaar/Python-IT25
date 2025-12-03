# 03.12.25 Põldäär
#6.1
import math
import turtle

turtle.speed(0)
kordaja = 10

nurk = math.radians(53)
korgus = 4.4
kaugus = korgus/math.tan(nurk)
pikkus = round(math.sqrt(math.pow(korgus,2) + math.pow(kaugus,2)),2)




print(pikkus)

turtle.fd(kaugus * kordaja)
turtle.lt(90)
turtle.fd(korgus * kordaja)
turtle.lt(143)
turtle.fd(pikkus * kordaja)



turtle.done()
