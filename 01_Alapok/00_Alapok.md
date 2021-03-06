## Alap operátorok:
* összeadás (+)
* kivonás (-)
* szorzás (*)
* osztás (/)
* hatványozás (**)

## A kiértékelés sorrendje:
* (**)     a legerősebben köt
* (+ és -) ha előjelként állnak (egyformán erősek),
            pl.: -2**4=-16 lesz, de (-2)**4 =16
* (* és /) egyformán erősek
* (+ és -) ha két operandust kötnek össze (egyformán erősek)


---

### Feladat:
Budapestről Amszterdamba szeretnénk autóval utazni,
és kíváncsiak vagyunk az útiköltségre:
* a távolság: 1395 km,
* az autónk fogyasztása: 7 liter 100 km-en,
* és 1 liter benzin ára: 327.9 Ft

> **Megoldás:**
1395 / 100 x 7 x 327.9 = 32019 Ft

> **Vác-Ózd távolságban az utiköltség:**
168 / 100 x 6.5 x 383.6 = 4200 Ft


### Feladat:
A következő kalkulációban meghatározzuk **100 000 forint** kamatát, amelyet megtakarításként félre szeretnénk tenni. Az összeget (az `osszeg` nevű változóban tároljuk) **5 hónapra** (`ho`) szeretnénk lekötni a bankban, az éves kamatláb **3.5%** (`ekl_sz`), és a nyert kamat után **22%** (`ado_sz`) adót kell fizetnünk. A `k` változóba tettük az 5 hónap után járó kamatot. Először kiszámítottuk az összegnek az éves kamatláb szerinti százalékát (`osszeg / 100 * ekl_sz`), de ez az egész évre járó kamatot jelenti, azaz ezt az értéket el kell osztani 12-vel, így megkapva az 1 hónapra jutó kamatot, majd ezt megszorozva 5-tel, a kívánt megtakarítási idővel (`ho`). Tehát 5 hónapra a kamat kerekítve 1458.3 Ft. A kamat adóját a `kamat_ado` változóban tároljuk, ami kerekítve 320.8 Ft-ot tesz ki, azaz a „hazavihető” nyereség 1137.5 Ft-nak adódik (természetesen az eredeti összeget, a tőkét is visszakapjuk).

**Megoldás:**
```python
osszeg = 100000
ho = 5
ekl_sz = 3.5
ado_sz = 22
kamat = osszeg / 100 * ekl_sz / 12 * ho
kamat_ado = kamat / 100 * ado_sz
print(kamat - kamat_ado)
```

A következő példában ugyanezt a feladatot oldjuk meg bemutatva, hogy az előbbi program nem az egyetlen, amivel a helyes értékeket előállíthatjuk. Minden fejlesztőnél kialakul majd egy rá jellemző programozási stílus, ami az idők folyamán általában változik is (remélhetőleg tökéletesedik).

```python
osszeg = 10 ** 5
ho = 5
esz = 3.5 / 100
asz = 22 / 100
kamat = osszeg * esz / 12 * ho
print(kamat - kamat * asz)
```