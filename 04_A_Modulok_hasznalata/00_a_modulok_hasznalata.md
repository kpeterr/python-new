A programozásban a korábban megszerzett ismereteket, például a gyakran elvégzendõ
feladatok unalmas utasítássorozatait vagy az éppenséggel nagy matematikai jártasságot
megkövetelõ eljárások (algoritmusok) programkódjait az ún. függvénykönyvtárak tárolják,
melyeket a Pythonban moduloknak nevezünk. A kedves olvasó is képes lesz majd modulok
készítésére, de itt most csak áttekintjük a használatuk módját. A moduloknak mindenekelõtt van
egy nevük, amelyre hivatkozva úgymond be kell „importálnunk” õket a programunkba. A
modulok önmagukban is objektumnak tekintendõk, amelyekbe további objektumok (változók,
függvények) vannak „beágyazva”. Az importálás többféleképpen is történhet. Az egyik módszert
alkalmazva a programunk és a modul változói elkülönítve maradnak, ekkor a belsõ elemekre a '.'
-tal kell hivatkozni, hasonlóan ahhoz, amint azt az „egyszerû” objektumoknál (pl. a karakterlánc
esetében az upper() metódusnál) láttuk. A másik módszer szerint a programunk és a modul
változói „összefésülõdnek”, s így a modul elemei ugyanúgy használhatók, mintha a saját
programunkban lettek volna definiálva. Az utóbbi eljárást nem ajánlott követni, ha a modulban és
a programunkban azonos nevû objektumok léteznek.

Az alábbi keretekben a math matematikai modul importálására látunk példákat. A math
típusa „module” objektum. A középsõ keretben a belsõ objektumokra a math. elõtaggal
hivatkozunk, a math.pi értékét egy saját változóba is beírjuk. A jobb oldali keretben az „import *”
utasítással minden belsõ objektumot „beleolvasztunk” a programkódunkba, így nincs szükség az
elõtagra, de ez keveredést okozhat, mint azt a pi változónál látjuk, amint új értéket kap.
	>>> import math
	>>> type(math)
	<class 'module'>
	>>>

	>>> import math
	>>> math.sqrt(4)
	2.0
	>>> v= math.sqrt(19.82)
	>>> v
	4.451965857910413
	>>> pi= math.pi
	>>> pi*pi
	9.869604401089358

	>>> from math import *
	>>> pi
	3.141592653589793
	>>> sqrt(pi*pi)
	3.141592653589793
	>>> pi= 3
	>>> pi
	3
	>>>

	>>> from math import pi
	>>> pi
	3.141592653589793
	>>> sqrt(4)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'sqrt' is not defined

	>>> import math as mm
	>>> mm.pi
	3.141592653589793
	>>> mm.sqrt(9)
	3.0
	>>>

A modulból elegendõ csak azokat az objektumokat importálni, amelyekre szükségünk lesz. A fenti
bal oldali keretben a pi-t importáltuk, de az sqrt()-t nem. A jobb oldali keretben az import hatása
megegyezik a legelsõ két példában adottal, de itt a math modult a továbbiakban a rövidebb mm
néven fogjuk tudni használni.
Az alábbiakban csak egyes objektumokat importálunk és mindegyiknek új nevet adunk,
amelyek ezután a modulbeli belsõ nevükön nem lesznek elérhetõk (lásd a pi -re adott hibát):
	>>> from math import pi as Pi, e as Ex, sqrt as sq
	>>> Pi, Ex, sq(4)
	(3.141592653589793, 2.718281828459045, 2.0)
	>>> pi
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'pi' is not defined
	>>>

