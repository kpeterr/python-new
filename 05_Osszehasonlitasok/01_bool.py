#-*- coding:utf-8 -*-

"""
Az alábbi bool.py nevű programmal szemléltethetjük a kiértékelés menetét.
Készítettünk benne egy ff() nevű függvényt, amelyet a kifejezésekben a True
és False értékek helyére írhatunk be; az első argumentuma egyben a
visszatérési értéke is lesz, a második pedig kiírásra kerül a végrehajtás során.
Amennyiben az első argumentumnak a True vagy False értéket adjuk meg, a
másodiknak pedig a függvény sorszámát az adott logikai kifejezésben, akkor
láthatóvá tehető, hogy az értelmező milyen sorszámú kifejezéseket (amik most
maguk a függvényeink) értékel ki, és melyekre nem vesztegeti az időt. Egy
szerkesztéstechnikai megjegyzést is kell tennünk: a programban látható
fordított perjel (\) segítségével egy hosszú sor kétfelé törhető. Mellékeltük a
futtatás eredményét is, amelyben az utolsó szakaszban kijelzett eredmény a
fenti példának felel meg.
"""

def ff( ertek, info):
    print( info)
    return ertek

print()     # ugrik egy üres sort

#(1) nincsennek műveleti zárójelek:
# True or True and False
v= ff(True,1) or ff(True,2) and ff(False,3)
print("v=",v)
print("-----------")

#(2) az első két tag és az operátor egy zárójelben:
# (True or True) and False
v= ( ff(True,1) or ff(True,2) ) and ff(False,3)
print("v=",v)
print("-----------")

#(3) egy hosszabb kifejezés:
# False and False and True or False or True
v= ff(False,1) and ff(False,2) and ff(True,3) or ff(False,4) \
or ff(True,5)
print("v=",v)
print("-----------")

print()     # ugrik egy üres sort
input("A befejezéshez nyomja meg az Enter-t!")