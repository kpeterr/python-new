#-*- coding:utf-8 -*-

"""
Az alábbi kifejezésekben a '¤' jel helyébe tegyük be az or és az and kulcsszavakat úgy, hogy
az egyenlőségek teljesüljenek:
	10 == ( 5 ¤ 10 ¤ 20 )
	20 == ( 5 ¤ 10 ¤ 20 )
	5 == ( 5 ¤ 10 ¤ 20 )
	None == ( 5 ¤ print("Szia!") )
	True == ( None ¤ not None )
	False == ( bool("") ¤ bool(" ") )
Mi történik, ha elhagyjuk a zárójeleket? Tipp: a '==' kötési erősségét is figyelembe kell
venni.
"""

# Megoldás:
print(10 == (5 and 10 or 20))
print(20 == (5 and 10 and 20))
print(5 == (5 or 10 or 20))
print()
print(None == ( 5 and print("Szia!") ))
print(True == ( None or not None ))
print(False == ( bool("") and bool(" ") ))