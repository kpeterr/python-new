#-*- coding:utf-8 -*-

"""
Az értékadás.py nevű program illusztrálja az elmondottakat. Egy programtechnikai
megjegyzés: az első if-else utasítás kimenetét az üzenet nevű változóba töltjük,
majd a print() függvény azt onnan veszi át, a második ilyen szerkezetnél az eredmény
közvetlenül a print() argumentumaként jön létre, megtakarítva egy külön értékadást:
"""

print()
# 'valami'-ben kar.lánc lesz, bár lehet, hogy egy üres lánc:
valami= input(" Kérek valamit: ")
uzenet= " Van valamim:" if valami else " Nincs semmim."
print( uzenet, valami)
print(" -------")

fiok= valami or "pótlék" 	# a 'fiók'-ban kar.lánc lesz
print( " A fiókban ez van:", fiok)
print(" -------")

p= "g" in fiok 		# 'p'-ben bool érték lesz
print( " Van 'g' a fiókban?", "Nincs" if not p else "Van" )
print(" -------")

valami= valami.lower()
van= "python" in valami or "piton" in valami
hir= " Van egy kígyónk" if van else " Semmi új hír."
print( hir)
van and print( " a hossza:", len(valami) )
# a= van and print( " a hossza:", len(valami) )
print(" -------")

input("A befejezéshez nyomja meg az Enter-t!")

"""
A fiók=valami or 'pótlék' értékadás jó példa arra, hogy ha egy adott változónak (fiók)
szánt érték (valami) nem megfelelő (pl. üres), akkor azt hogyan helyettesíthetjük mással
('pótlék'). Figyeljük meg a lower() metódus használatát is: így nem fog számítani, hogy a
megadott karakterláncban keverednek-e a kis- és nagybetűk. A „van and print()” kifejezés
szerint ha a van igaz, azaz a 'piton' vagy a 'python' szó benne van a beadott karakterláncban,
akkor kiíratjuk a lánc hosszát. Ez a kifejezés egy értékadó utasítás, de nem tároljuk el az
értékét. Ha a van hamis, akkor a False lenne a tárolható eredmény, ha igaz, akkor a print()
utasítás által visszaadott None.
"""