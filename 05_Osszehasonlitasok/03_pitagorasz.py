#-*- coding:utf-8 -*-

"""
A következő programban azt ellenőrizzük, hogy a beadott egész számok lehetnek-e egy
derékszögű háromszög oldalai:
"""

print(" Kérem adja meg a háromszög oldalait! Csak egész számokat adjon meg!")
a,b,c = int( input(" a= ")), int( input(" b= ")), int( input(" c= "))

a2, b2, c2 = a*a, b*b, c*c
pita= a2+b2 == c2 or a2+c2 == b2 or b2+c2 == a2

nem= "" if pita else "NEM"
print(" Ezek",nem,"lehetnek derékszögű háromszög oldalai.")

input("A befejezéshez nyomja meg az Enter-t!")

"""
A pita változónak értéket adó kifejezésben három egyenlőséget kell ellenőrizni, és bármelyik
is bizonyul igaznak, az or operatorok révén az egész kifejezés True értéket kap, illetve
False-t, ha egyik sem igaz (nincs a kifejezésben pl. and, ami erősebben kötne). A program
egész számokat vár bemenetként, de természetesen egy derékszögű háromszög oldalai nem csak
ilyenek lehetnek.
Programozástechnikai megjegyzések: Az a,b,c változóknak egyetlen sorban kérünk értéket a
három input() utasítással. Az input() visszatérési értékét nem mentjük el változóba, hanem
„röptében” átadjuk az int()-nek argumentumként, és az így nyert értéket tároljuk csak el a
megfelelő változóban. Ha valamelyik bemeneti adat nem egész érték, akkor az int()-nél hiba fog
jelentkezni. Az a változó négyzetét előre kiszámolva két négyzetszámítást megtakarítunk ott,
ahol az a2 szerepel, és ugyanígy a másik két oldalnál is. A nem változóba az üres
karakterláncot tesszük, ha lehet szó derékszögű háromszögről, de a 'NEM' szót, ha az oldalak
nem megfelelőek. A nem változót ezután beillesztjük a print() által kiírandó üzenetbe.
"""