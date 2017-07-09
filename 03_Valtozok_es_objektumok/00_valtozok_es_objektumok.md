----------------------------------------------------------------
-------------------- VÁLTOZÓK ÉS OBJEKTUMOK --------------------
----------------------------------------------------------------


Az eddig használt változóinkban gyakorlatilag csak számokat tároltunk, de a Python más
típusú változókkal is rendelkezik, sõt egyedieket is készíthetünk. A változókra a korábbiakban
mint memóriarekeszekre (más elnevezéssel memóriacellákra) gondoltunk, ami az alacsony szintû
programozási nyelveknél teljesen helytálló. A Python azonban egy magas szintû nyelv, amelyben
egy változónak nem csak értéke van, hanem még egyéb más tulajdonságokkal is rendelkezik,
ennek okán a belsõ szerkezete sokkal összetettebb. Egy Python változó tárolásához fizikailag már
nem elég egyetlen memóriacellányi hely. Idõnként, amikor ezt a belsõ összetettséget ki akarjuk
hangsúlyozni a változót inkább objektumnak nevezzük. A késõbbiekben megismerkedünk majd
az objektumok belsõ szerkezetével, amelyet egy erõsen leegyszerûsített modellel fogunk
ábrázolni.
Tekintsük át a már megismert változók típusait:
• egész szám, angolul integer, rövidítve int;
	a type(5) kimenete: <class 'int'>
• tizedes pontot is tartalmazó szám, pontosabban ún. lebegõpontos szám, angolul float;
	a type(3.14) kimenete:<class 'float'>
• booleans-változók, amelyek csak True vagy False értéket vehetnek fel, rövidítve bool;
	a type(True) kimenete: <class 'bool'>
	A kifejezések eredményeinek összehasonlításában nélkülözhetetlenek.
• a None objektum;
	a type(None) kimenete: <class 'NoneType'>
A függvények tárgyalásánál láttuk, hogy például ezt az értéket kapja egy változó, ha
visszatérési értéket nem adó függvénnyel próbálunk hozzá értéket rendelni.
Alkalmazhatjuk majd mi is, ha pl. egy adott változót korán kell definiálni, de még nem
tudunk neki megfelelõ értéket adni: a program tesztelheti a szóban forgó változót, s csak
akkor használja az értékét, ha az nem None (de ehhez a tudáshoz még több fejezetet el kell
olvasnunk).

A type() által kiírtak között szereplõ class kifejezés angolul osztályt ill. kategóriát jelent. Az
objektumokkal dolgozó programnyelvek rendszerint ezt használják kulcsszóként új típusú
(kategóriájú) objektumok definiálására. Valójában volt még egy további típus, amivel már
találkoztunk, de nem vettük közelebbrõl szemügyre. A programfájlok végén ez az utasítás állt:
input("A befejezéshez nyomja meg az Enter-t!"). Az idézõjelek között megadott betûk egy ún.
karakterláncot alkotnak:
• karakterlánc, angolul string, rövidítve str;
a type("A befejezéshez nyomja meg az Enter-t!") kimenete: <class 'str'>
A karakterlánc betûket, számokat és egyéb jeleket tartalmazhat, amelyeket idézõjelek közé
kell tenni. Az idézõjel lehet dupla ” vagy szimpla ', de a lánc két végén azonosnak kell
lenniük. A karakterláncok metódusaival egy külön fejezetben részletesen meg fogunk
ismerkedni.

Az említett input() egy standard függvény, ami kiírja a képernyõre az argumentumként
megadott karakterláncot, és beolvassa a billentyûzeten bevitt adatokat amíg az Enter-t le nem
nyomjuk. A beolvasott adatokat egy változóban eltárolhatjuk, de a fenti fájljainkban mi ezt nem
tettük meg, mert csak arra volt szükségünk, hogy a terminálablak (Linuxon) vagy a
parancssorablak (Windowson) ne záródjon be mielõtt a kiírt eredményeket el tudnánk olvasni, és
az input() függvény várakozása az Enter leütésére ezt jól szolgálta. Az input() visszatérési értéke
mindig karakterlánc, még akkor is, ha számot billentyûzünk be:
	>>> kl= input("Kérek valamit: ")
	Kérek valamit: helló
	>>> kl
	'helló'
	>>> type(kl)
	<class 'str'>

	>>> kl= input("Kérek valamit: ")
	Kérek valamit: 3.14
	>>> kl
	'3.14'
	>>> type(kl)
	<class 'str'>

Egy karakterlánc már bonyolultabb objektumnak tûnik mint egy egész szám és várhatóan
„érdekes” tulajdonságokkal bír. Nyilvánvalóan az egyik ilyen a hossza. Az objektum hosszát a
standard len() függvénnyel kérdezhetjük meg, melynek bemeneti adata maga az objektum (a len
az angol length szó rövidítése, ami hosszúságot jelent). Figyeljük meg az alábbi példán,
hogy a szóköz is beleszámít a hosszba:
	>>> s= "Szia Python"
	>>> len(s)
	11
	>>> len("Tükör")
	5

	>>> s= "Tükröm tükröm"
	>>> s1= "ÖKRÖM ÖKRÖM"
	>>> s.upper()
	'TÜKRÖM TÜKRÖM'
	>>> s1.lower()
	'ökröm ökröm'


----------------------------------------------------------------


Az objektumok tulajdonságai közé soroljuk az ún. metódusokat is, azaz a „belsõ”
függvényeiket. Az eddig megismert standard függvények, mint például a min(), type(),
len(), mindig meghívhatók a program bármely részében, de a metódusokhoz elõbb létre
kell hozni egy objektumot, hiszen abban vannak ezek a függvények „beágyazva”. A fenti jobb
oldali keretben két metódus használata látható, az egyik a láncban minden karaktert nagybetûssé
alakít, a másik pedig kisbetûssé. A hívás módja egyszerû: a kiválasztott objektum neve után egy ' .'
áll, majd a metódus neve következik a zárójelekkel és azok között az argumentumok, ha ez
utóbbiak egyáltalán kellenek (itt a fenti példában most nem). Tehát a metódusok és a standard
függvények meghívása között nincs különbség, de az elõbbi neve kiegészül az õt tartalmazó
objektum nevével.
Meglepetésként hathat, hogy maguk a függvények és a metódusok is objektumok:
	>>> type(min)
	<class 'builtin_function_or_method'>
	>>> s= "lánc"
	>>> type( s.upper)
	<class 'builtin_function_or_method'>

A fenti példákban a type() függvény argumentumaként a min() függvényre és a karakterlánc
upper() metódusára történõ hivatkozást adtuk át, azaz nem hívtuk meg ezeket a függvényeket,
amit az is mutat, hogy elhagytuk mögülük a zárójeleket. Ha meghívással adjuk át õket, pl.
type(min(10,2,3)) akkor a visszatérési érték típusát fogjuk megkapni.

Az objektumok azon metódusai, amelyeknek van visszatérési értéke, egy-egy újabb
objektumot eredményeznek. Az új objektum típusa bármi lehet: azt csak a metódus programkódja
határozza meg, azaz nem kell hogy megegyezzen a kiindulási objektum típusával. A visszatérési
értékként kapott objektumnak is vannak metódusai, így ezeket is meghívhatjuk:
	>>> s= "csermely"
	>>> s1= s.upper()
	>>> db= s1.count("E")
	>>> db
	2

	>>> s= "csermely"
	>>> db= s.upper().count("E")
	>>> db
	2
	>>>

A fenti két példában szemléltettük a kétféle eljárást a visszatérési értékek metódusainak
meghívására. Az elsõ esetben az upper() visszatérési értéke az s1-be került, ami karakterlánctípusú.
Ezután az s1 count() metódusát hívtuk, ami megszámolja az argumentumként megadott
karakterlánc elõfordulását az s1-ben, és ennek megfelelõen visszaadott egy számot. A második
esetben ezt egyetlen programsorban megtesszük, a pontokat „halmozva”. Itt nem hozunk létre
külön s1 változót, hanem ekkor a Python-értelmezõ, a „szemünk elõl rejtve” készít egy ún.
ideiglenes változót, amelynek a nevét nem tudatja velünk. Az ideiglenes (vagy átmeneti) változót
az értelmezõ megszünteti, amint már nincs rá szüksége.

A számok, mint az int- és a float típusúak is, objektumok, de nekik természetesen nincs
upper() metódusuk: ha mégis megpróbáljuk ezt használni, akkor az értelmezõ hibajelzéssel leáll.

Idõnként szükség van arra, hogy egy adott típusú változót egy másikba alakítsunk át: ezt
nevezzük konverziónak. Említettük, hogy az input() visszatérési értéke mindig karakterlánc és
ezért a számok bebillentyûzése után átalakítást kell végeznünk.
	>>> d= input("Kérek egy számot: ")
	Kérek egy számot: 32
	>>> 1+d
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	>>>

A fenti programban nem tudtuk az 1-hez a 32-öt hozzáadni, mert az értelmezõ nem tudja hogyan
kell egy egész számot és egy karakterláncot összeadni, ami nem meglepõ. A következõkben a
mûvelet már sikeres lesz:
	>>> d= input("Kérek egy számot: ")
	Kérek egy számot: 32
	>>> d
	'32'
	>>> type(d)
	<class 'str'>
	>>> d= int(d)
	>>> d
	32
	>>> type(d)
	<class 'int'>
	>>> 1+d
	33

	>>> d= input("Kérek egy számot: ")
	Kérek egy számot: 5.89
	>>> d
	'5.89'
	>>> type(d)
	<class 'str'>
	>>> d= float(d)
	>>> d+1.11
	7.0

A fenti programokban a d változót az int() és a float() standard függvények meghívásával
átalakítjuk, és az új értékeket ugyancsak a d nevû változóba tesszük, bár tehettük volna egy
másikba is. A konverziót azonban nem lehetséges mindig elvégezni, ilyen eseteket látunk a
következõkben:
	>>> int( "34 Ft")
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '34 Ft'

A fenti utasítás végrehajtásakor az értelmezõ arra panaszkodik hogy egy tízes számrendszerben
megadott karakterláncot alakított volna át, de érvénytelen karaktert talált, nyilván az 'F' és 't'
okozta a problémát. A következõ keret elsõ utasításában a '0xFF' karakterláncnál ugyanez a
helyzet állt elõ, mivel az 'x' és 'F' karakterek értelmezhetetlenek a tízes számrendszerben. Megadva
azonban második argumentumként a 16-ot, mint alapszámot, a konverzió sikeresen megtörténik
(egy késõbbi fejezetben még lesz szó a tizenhatos számrendszerrõl). A '2.7' lánc átalakítása sem
sikerülhet az int() függvénnyel, mert egy egész szám nem tartalmazhat pontot:
	>>> int("0xFF")
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '0xFF'
	>>> int( "0xFF", 16)
	255
	>>> int( "2.7")
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '2.7'

Az elõbbi példákban karakterláncokból készítettünk számokat, de az egyik típusú számból is
lehetséges egy másikat készíteni, sõt számból karakterláncot, és akármibõl bool változót:
>>> float(1)
1.0
>>> int(2.7)
2

>>> s= str( 3.14)
>>> type(s)
<class 'str'>
>>> s
'3.14'

>>> bool(0)
False
>>> bool(1)
True
>>> bool(0.001)
True

>>> bool("Szia")
True
>>> bool(" ")
True
>>> bool("")
False

>>> bool(None)
False

>>> bool("None")
True

Egy float számból az int() függvény úgy készít egész számot, hogy egyszerûen elhagyja a
tizedespont utáni számjegyeket. A korábban megismert round() függvény ezt másképpen teszi.
Vegyük észre, hogy az int() nem ugyanúgy viselkedik, ha egy tizedespontot tartalmazó számot
float-ként illetve karakterláncként adunk át neki.
A 0 szám bool értéke False és minden más számé True. Egy nem üres karakterlánc bool értéke
is True. Figyeljük meg, hogy az egyetlen szóközt tartalmazó karakterlánc nem egy üres lánc! Az
üres karakterláncot szorosan egymás mellé írt idézõjelekkel ábrázoljuk és ennek értéke már False.
A None objektum bool értéke False. Fontos megjegyezni, hogy a 'None' egy karakterlánc és
nem a None objektum.

Az eddigiekben már láttuk hogyan lehet a változókat létrehozni, és felmerül a kérdés, hogy
meg lehet õket szüntetni, ha már nincs rájuk szükség. Igen, egy változót a del utasítással
törölhetünk, ami után a nevének használata már hibához vezet:
	>>> mi = ”tükör”
	>>> mi
	'tükör'
	>>> del mi
	>>> mi
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'mi' is not defined


A „változó” és az „objektum” kifejezéseket gyakorlatilag egymás helyett használtuk, és
használhatjuk a jövõben is, de nem minden esetben, mert valójában nem ugyanazt
jelentik. Ezt úgy világíthatjuk meg, ha számba vesszük a tulajdonságaikat. Egy
objektumnak van értéke, esetleg hossza, lehetnek metódusai és még más tulajdonságai, de
mindenekelõtt van neki típusa ; neve azonban önmagában nincs . Ezzel szemben a váltózó
rendelkezik egy névvel, és a szemeink elõl rejtetten tárol egy memóriacímet, amely valamely
objektumnak a számítógép memóriájában elfoglalt kezdõcímével egyezik meg. A változó
valójában csak egy hivatkozás, ún. referencia egy adott objektumra, nevesíti azt, de nem maga az
objektum. Amikor egy változó értékérõl vagy pl. a hosszáról, esetleg a metódusairól beszélünk,
akkor valójában az általa nevesített objektum tulajdonságaival ruházzuk fel azt, de csak szóban.
Látni fogjuk, hogy egy objektumot több névvel is illethetünk, azaz több változó is mutathat
ugyanarra az objektumra. Sõt ezt a Python-értelmezõ a tudtunk nélkül is sokszor alkalmazza,
hogy takarékoskodjon a rendelkezésre álló memóriával. A két fogalom közti különbséget jobban
fogjuk érteni, ha foglalkozunk egy kicsit a memóriacímekkel.

Két objektum egyidejûleg nem foglalhatja el ugyanazt a helyet a memóriában. A standard id()
függvénnyel (az angol identity szó rövidítése, mely identitást, azonosságot, személyazonosságot
jelent) lekérdezhetjük az objektumokat azonosító memóriacímeket:
	>>> a= 5
	>>> b= 5
	>>> id(a),id(b)
	(137396096, 137396096)
	>>> f1= 3.14
	>>> f2= 3.14
	>>> id(f1),id(f2)
	(155423668, 155423604)
	>>>

Mint a példából látható, az egész számhoz a Python csak egyszer hozta létre az objektumot, míg a
tizedes pontot tartalmazókhoz mindkét esetben újat gyártott. A Python dokumentációjában
olvasható, hogy egy adott egész szám objektuma nem módosítható. Ez nem jelent korlátozást,
mert ezt az egész számot tetszõleges alkalommal felhasználhatjuk más objektumok létrehozására.
Például az alábbi keretben az a=a+2 kifejezés esetén nem az 5-öt tartalmazó objektum értékét
módosítjuk 7-re, hanem az a értékének a felhasználásával létrehozzuk a 7-et tartalmazó új
objektumot, s mostantól az a változó már erre fog „mutatni”, ezt fogja nevesíteni. A b továbbra is
az 5-ös objektumra fog hivatkozni. Egy új c változónak a 7-es értéket adva, nem keletkezik új
objektum, hanem a c a már az elõbbiekben létrejött objektumra fog mutatni:
	>>> a=b= 5
	>>> id(a), id(b)
	(137396096, 137396096)
	>>> a= a+2
	>>> a
	7
	>>> id(a), id(b)
	(137396128, 137396096)
	>>> c= 7
	>>> id(c)
	137396128

Ha töröljük az egy adott objektumra mutató összes változót, akkor az az objektum már
elérhetetlen lesz és így felesleges is, s ezért azt a Python-értelmezõ elõbb vagy utóbb kitörli a
memóriából egy „szemétgyûjtésnek” nevezett eljárásban.
Egy objektum törlésekor felszabadul az addig általa lefoglalt memória, és azt egy új objektum
megkaphatja, tehát az id() által jelzett azonosító is meg fog egyezni a korábban létezett
objektuméval. Az egyidejûleg létezõ különbözõ objektumokat azonban az id() soha nem fogja
azonosnak jelezni!

Az alábbi keretben a karakterlánc-típusú objektumoknál is tapasztalható a takarékosság elve. Az
input() függvény által beolvasott lánc azonban már egy új objektum lesz, bár ugyanolyan
karakterláncot tartalmaz mint az s1 és s2 által hivatkozott objektum:
	>>> s1= "Szia"
	>>> s2= "Szia"
	>>> s3= input(" Köszönés: ")
	Köszönés: Szia
	>>> id(s1),id(s2),id(s3)
	(3073928320, 3073928320, 3073928608)
	>>>

