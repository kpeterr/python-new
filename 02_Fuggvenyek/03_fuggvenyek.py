# -*- coding:utf-8 -*-

"""
A következő programban arra találhatunk példákat, hogy a függvények a
paramétereik illetve a visszatérési értékeik számát tekintve hogyan
különbözhetnek. A máli() rutin két értéket ad vissza, amelyeket a return
utasítás után vesszővel elválasztva sorolunk fel. A máli() hívásakor
egyidejűleg két változónak, az y1-nek és az y2-nek adunk értéket.
"""


# Lineáris függvény
def lini(x):     	# egy paraméter
    y = 3 * x + 1
    return y 		# egy v.térési érték


# Másodfokú függvény
def masodf(x): 		# egy paraméter
    return x*x-4 	# egy v.térési érték


# Egyidejűleg számol két függvényt
def mali(x): 		# egy paraméter
    return lini(x), masodf(x) 	# két v.térési érték


# Párhuzamos egyenesek
def ugras(x, c):     	# két paraméter
    return 3 * x + c 	# egy v.térési érték


# A fenti függvények tesztelése
print(masodf(0), masodf(2))

y1, y2 = mali(3)
print(y1, y2)

print(ugras(1, 1), ugras(1, 2), ugras(2, 2))

input("A befejezéshez nyomja meg az Enter-t!")


"""
Az itteni függvények belsejében használt x,y,c változók a függvényeken kívüli
utasítások számára láthatatlanok, ún. lokális változók. Ezen változók a
függvény végrehajtása során jönnek létre és annak visszatérése után megszűnnek
létezni, ez minden újabb híváskor újra és újra lejátszódik. A függvényeket még
azok első meghívása előtt definiálni kell, ezért a programban rendszerint
előre csoportosítjuk őket.
A későbbi fejezetekben lesz csak szó az ún. elágazásokról, ahol bizonyos
feltételek teljesülése vagy nem teljesülése esetén más-más utasítás-
csoportokkal folytatódik a függvényblokk végrehajtása: ekkor igény szerint
több return utasítást is elhelyezhetünk a függvényen belül.
"""
