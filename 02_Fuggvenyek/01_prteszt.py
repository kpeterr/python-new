# -*- coding:utf-8 -*-

"""
Az alábbi programfájlban megismételtük az interaktív módban készült előbbi
tesztet. A fájlt készítsük el a kiválasztott szerkesztő programmal és mentsük
el valamilyen néven. A print() által kiírt eredményeket a program futtatása
során tudjuk megtekinteni (lásd az „Egy Python program futtatása” című
fejezetet). Vegyük észre, hogy minden sort a legelső pozíción kezdtünk,
az összes utasítás egyetlen blokknak felel meg, nem lenne logikus, ha bármelyik
sort beljebb kezdenénk és erre a hibára az értelmező figyelmeztetne is:
"""

x, y, z = 5, 3, 9
print(x, y, z)
print(min(x, y, z), max(x, y, z), x + y + z + 100)
print(type(x))
print(2015)

input("A befejezéshez nyomja meg az Enter-t!")
