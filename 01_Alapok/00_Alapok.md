Alap operátorok:
+ összeadás
- kivonás
* szorzás
/ osztás
** hatványozás

**          a legerõsebben köt
+ és -      ha elõjelként állnak (egyformán erõsek),
            pl.: -2**4=-16 lesz, de (-2)**4 =16
* és /      (egyformán erõsek)
+ és -      ha két operandust kötnek össze (egyformán erõsek)

----------------------------------------------------
Feladat:
Budapestrõl Amszterdamba szeretnénk autóval utazni,
és kíváncsiak vagyunk az útiköltségre:
a távolság 1395 km, az autónk fogyasztása
7 liter 100 km-en, és 1 liter benzin ára 327.9 Ft

Megoldás:
1395/100*7*327.9    # 32019 Ft

Vác-Ózd távolságban az utiköltség:
168/100*6.5*383.6   # 4200 Ft
----------------------------------------------------


----------------------------------------------------
Feladat:
A következõ kalkulációban meghatározzuk 100 000 forint kamatát, amelyet megtakarításként
félre szeretnénk tenni. Az összeget (az ö nevû változóban tároljuk) 5 hónapra (hó) szeretnénk
lekötni a bankban, az éves kamatláb 3.5% (ékl_sz), és a nyert kamat után 22% (adó_sz) adót kell
fizetnünk. A k változóba tettük az 5 hónap után járó kamatot. Elõször kiszámítottuk az összegnek
az éves kamatláb szerinti százalékát (ö/100*ékl_sz), de ez az egész évre járó kamatot jelenti, azaz
ezt az értéket el kell osztani 12-vel, így megkapva az 1 hónapra jutó kamatot, majd ezt
megszorozva 5-tel, a kívánt megtakarítási idõvel. Tehát 5 hónapra a kamat kerekítve 1458.3 Ft. A
kamat adóját az a változóban tároljuk, ami kerekítve 320.8 Ft-ot tesz ki, azaz a „hazavihetõ”
nyereség 1137.5 Ft-nak adódik (természetesen az eredeti összeget, a tõkét is visszakapjuk).

Megoldás:
>>> ö= 100000
>>> hó= 5
>>> ékl_sz= 3.5
>>> adó_sz= 22
>>> k= ö/100*ékl_sz/12*hó
>>> k
1458.3333333333335
>>> a= k/100*adó_sz
>>> a
320.83333333333337
>>> k-a
1137.5
>>>

A következõ példában ugyanezt a feladatot oldjuk meg bemutatva, hogy az elõbbi program nem
az egyetlen, amivel a helyes értékeket elõállíthatjuk. Minden fejlesztõnél kialakul majd egy rá
jellemzõ programozási stílus, ami az idõk folyamán általában változik is (remélhetõleg
tökéletesedik).

>>> ö= 10**5
>>> hó= 5
>>> ész= 3.5/100
>>> asz= 22/100
>>> k= ö*ész/12*hó
>>> k - k*asz
1137.5
>>>

