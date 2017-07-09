# -*- coding:utf-8 -*-

"""
A következő függvények3.py program két függvényt mutat be, az egyiknek egy
paramétere van és nincs visszatérési értéke, a másiknak nincs sem paramétere,
sem visszatérési értéke. Ekkor a return utasítás önmagában szerepel.
Amennyiben a visszatérési érték nélküli rutin olyan, hogy nincs benne
elágazás, akkor a return utasítás el is hagyható. Valójában a visszatérési
érték nélküli függvény egy speciális értéket, a None-t adja vissza, s ezért
nem kapunk hibajelzést az a=c10() értékadó utasításnál, az a értéke None lesz
(a None-ról még sok szó lesz a későbbiekben).
"""


# Kiírja az argumentum értékét
def mutat(v):     # egy paraméter
    print(v)
    return 		# nincs visszatérési érték


# Mindig 10-et ír ki
def c10():  # nincs paraméter
    print(10)
    # return
    # nincs visszatérési érték és a return sem fontos


mutat(3.14) 	# "belül" van a print()
c10() 			# "belül" van a print()
a = c10()
print(a)
input("A befejezéshez nyomja meg az Enter-t!")
