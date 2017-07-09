# -*- coding:utf-8 -*-

# Az alábbi programkódban a time- és a sys modul néhány objektumát alkalmazzuk:

import time
import sys

print(" Az operációs rendszer:", sys.platform)

tstart = time.time()
print(" Aludni megyek ...")
time.sleep(5)
print(" Felébredtem!")
tstop = time.time()

print(" Az alvási idő másodpercben:", tstop-tstart)

input("A befejezéshez nyomja meg az Enter-t!")

"""
A sys modul platform nevű változójából megtudhatja a programunk, hogy milyen
rendszeren fut, s ennek megfelelően eltérő feladatokat is végrehajthat, de ezt
itt most nem használjuk ki. A timemodulnak van egy ugyancsak time nevű
függvénye, amely az ún. epocha óta eltelt időt adja meg másodpercben.
Az epocha valamilyen időszámítás kezdetére utal, a mostani számítógépes
rendszerekben ez általában 1970. január 1-je 0 óra 0 perc 0 másodperc.
A tárgyalt programunkban nem volt érdekes az epocha pontos időpontja,
mert csak két időpont közötti különbségre voltunk kíváncsiak.
A time modul két érdekes metódusa még a gmtime() és a localtime(),
az első az aktuális greenwichi középidőt (Greenwich Mean Time) adja meg,
a második pedig a helyi időt. (A Python ezen függvényei a számítógép operációs
rendszerének időbeállítását használják fel.) Amennyiben argumentumként egy
számot adunk meg nekik, akkor azt az epocha óta eltelt másodpercként
értelmezik és az ahhoz tartozó értékeket jelenítik meg. Így a 0 másodpercet
megadva megtudhatjuk az epocha dátumát is:
    >>> import time as tt
    >>> tt.time()
    1423922312.078496
    >>> tt.gmtime()
    time.struct_time(tm_year=2015, tm_mon=2, tm_mday=14, tm_hour=13, tm_min=58,
    tm_sec=39, tm_wday=5, tm_yday=45, tm_isdst=0)
    >>>
    >>> tt.localtime()
    time.struct_time(tm_year=2015, tm_mon=2, tm_mday=14, tm_hour=14, tm_min=58,
    tm_sec=47, tm_wday=5, tm_yday=45, tm_isdst=0)
    >>>
    >>> tt.gmtime(0)
    time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0,
    tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
    >>>
    >>> type( tt.gmtime())
    <class 'time.struct_time'>
    >>>

Mindkét függvény egy a time modulban meghatározott objektumot ad meg
visszatérési értékként, melynek sajátos szerkezetében (struktúrájában,
angolul structure) több adat is található. Előre is szaladhatunk az időben,
ha akarunk: lekérdezve az aktuális időponthoz tartozó másodperceket, hozzájuk
adva egy számot, majd az összeget átadva a localtime() függvények,
megtudhatjuk, hogy a hozzáadott másodpercek elteltével mi lesz a dátum:
    >>> import time as tt
    >>> tt.gmtime( tt.time() + 86400 )
    time.struct_time(tm_year=2015, tm_mon=2, tm_mday=15, tm_hour=14, tm_min=11,
    tm_sec=57, tm_wday=6, tm_yday=46, tm_isdst=0)
    >>>
"""
