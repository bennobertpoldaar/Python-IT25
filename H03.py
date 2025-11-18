import turtle

#Benno BErt Põldäär
#Ülesanne 03
# Ülesanne 3.3: Reisiplaan
# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”
name = "Imre"
age = 18
keskmine_hinne = 4.7
print(name,",",age,"aastat vana ja keskmine hinne on",keskmine_hinne)
#Ülesanne 3.4: Lemmikraamat
#Loo muutuja raamatu_pealkiri, mis sisaldab raamatu pealkirja (string)
#Loo muutuja raamatu_autor, mis sisaldab kirjaniku nime (string)
#Loo muutuja raamat,  mis ühendab kokku raamatu_pealkiri ja raamatu_autor ning nende vahele jääb tühik
#Loo muutuja lehekylgede_arv, mis näitab raamatu lehekülgede arvu (integer)
#Loo muutuja hindamisskoor, mis näitab raamatu hinnet skaalal 1-10 (float)
#Trüki välja lause, nt: “Minu lemmikraamat on Sipsik Eno Raud , mis on 16 lehekülge pikk ja mille ma hindan 9.7 punktiga.”
#Kasuta väljatrükkimisel ainult plussi (+)

raamatu_pealkiri = "Sipsik"
raamatu_autor = "Eno Raud"
raamat = raamatu_pealkiri+" "+raamatu_autor
lehekylgede_arv = 16
hindamisskoor = 7.0
print("Minu lemmikraamat on "+raamat+",mis on "+str(lehekylgede_arv)+" pikk ja mille ma hindan "+str(hindamisskoor)+" punktiga ")
# Ülesanne 3.7: Python Turtle kolmnurk
# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
# Kasutades Turtle’i, joonista kõrvuti 3 värvilist kolmnurka, mis kasutab loodud muutujaid
# Iga kolmnurk on järgmisest 1,5 korda eemal
# Testi: muuda külje pikkust ning kolmnurgad on kenasti teineteisest eemal
kylje_pikkus = 20
nurk = 120
kujundi_varv = "pink"
kordaja = 3
nihe = 1.5
turtle.color(kujundi_varv)
for i in range(kordaja): 
    for i in range(kordaja):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.fd(kylje_pikkus*nihe)
    turtle.pendown()


turtle.done()