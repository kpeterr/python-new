----------------------------------------------------------------
-------------------- V�LTOZ�K �S OBJEKTUMOK --------------------
----------------------------------------------------------------


Az eddig haszn�lt v�ltoz�inkban gyakorlatilag csak sz�mokat t�roltunk, de a Python m�s
t�pus� v�ltoz�kkal is rendelkezik, s�t egyedieket is k�sz�thet�nk. A v�ltoz�kra a kor�bbiakban
mint mem�riarekeszekre (m�s elnevez�ssel mem�riacell�kra) gondoltunk, ami az alacsony szint�
programoz�si nyelvekn�l teljesen helyt�ll�. A Python azonban egy magas szint� nyelv, amelyben
egy v�ltoz�nak nem csak �rt�ke van, hanem m�g egy�b m�s tulajdons�gokkal is rendelkezik,
ennek ok�n a bels� szerkezete sokkal �sszetettebb. Egy Python v�ltoz� t�rol�s�hoz fizikailag m�r
nem el�g egyetlen mem�riacell�nyi hely. Id�nk�nt, amikor ezt a bels� �sszetetts�get ki akarjuk
hangs�lyozni a v�ltoz�t ink�bb objektumnak nevezz�k. A k�s�bbiekben megismerked�nk majd
az objektumok bels� szerkezet�vel, amelyet egy er�sen leegyszer�s�tett modellel fogunk
�br�zolni.
Tekints�k �t a m�r megismert v�ltoz�k t�pusait:
� eg�sz sz�m, angolul integer, r�vid�tve int;
	a type(5) kimenete: <class 'int'>
� tizedes pontot is tartalmaz� sz�m, pontosabban �n. lebeg�pontos sz�m, angolul float;
	a type(3.14) kimenete:<class 'float'>
� booleans-v�ltoz�k, amelyek csak True vagy False �rt�ket vehetnek fel, r�vid�tve bool;
	a type(True) kimenete: <class 'bool'>
	A kifejez�sek eredm�nyeinek �sszehasonl�t�s�ban n�lk�l�zhetetlenek.
� a None objektum;
	a type(None) kimenete: <class 'NoneType'>
A f�ggv�nyek t�rgyal�s�n�l l�ttuk, hogy p�ld�ul ezt az �rt�ket kapja egy v�ltoz�, ha
visszat�r�si �rt�ket nem ad� f�ggv�nnyel pr�b�lunk hozz� �rt�ket rendelni.
Alkalmazhatjuk majd mi is, ha pl. egy adott v�ltoz�t kor�n kell defini�lni, de m�g nem
tudunk neki megfelel� �rt�ket adni: a program tesztelheti a sz�ban forg� v�ltoz�t, s csak
akkor haszn�lja az �rt�k�t, ha az nem None (de ehhez a tud�shoz m�g t�bb fejezetet el kell
olvasnunk).

A type() �ltal ki�rtak k�z�tt szerepl� class kifejez�s angolul oszt�lyt ill. kateg�ri�t jelent. Az
objektumokkal dolgoz� programnyelvek rendszerint ezt haszn�lj�k kulcssz�k�nt �j t�pus�
(kateg�ri�j�) objektumok defini�l�s�ra. Val�j�ban volt m�g egy tov�bbi t�pus, amivel m�r
tal�lkoztunk, de nem vett�k k�zelebbr�l szem�gyre. A programf�jlok v�g�n ez az utas�t�s �llt:
input("A befejez�shez nyomja meg az Enter-t!"). Az id�z�jelek k�z�tt megadott bet�k egy �n.
karakterl�ncot alkotnak:
� karakterl�nc, angolul string, r�vid�tve str;
a type("A befejez�shez nyomja meg az Enter-t!") kimenete: <class 'str'>
A karakterl�nc bet�ket, sz�mokat �s egy�b jeleket tartalmazhat, amelyeket id�z�jelek k�z�
kell tenni. Az id�z�jel lehet dupla � vagy szimpla ', de a l�nc k�t v�g�n azonosnak kell
lenni�k. A karakterl�ncok met�dusaival egy k�l�n fejezetben r�szletesen meg fogunk
ismerkedni.

Az eml�tett input() egy standard f�ggv�ny, ami ki�rja a k�perny�re az argumentumk�nt
megadott karakterl�ncot, �s beolvassa a billenty�zeten bevitt adatokat am�g az Enter-t le nem
nyomjuk. A beolvasott adatokat egy v�ltoz�ban elt�rolhatjuk, de a fenti f�jljainkban mi ezt nem
tett�k meg, mert csak arra volt sz�ks�g�nk, hogy a termin�lablak (Linuxon) vagy a
parancssorablak (Windowson) ne z�r�djon be miel�tt a ki�rt eredm�nyeket el tudn�nk olvasni, �s
az input() f�ggv�ny v�rakoz�sa az Enter le�t�s�re ezt j�l szolg�lta. Az input() visszat�r�si �rt�ke
mindig karakterl�nc, m�g akkor is, ha sz�mot billenty�z�nk be:
	>>> kl= input("K�rek valamit: ")
	K�rek valamit: hell�
	>>> kl
	'hell�'
	>>> type(kl)
	<class 'str'>

	>>> kl= input("K�rek valamit: ")
	K�rek valamit: 3.14
	>>> kl
	'3.14'
	>>> type(kl)
	<class 'str'>

Egy karakterl�nc m�r bonyolultabb objektumnak t�nik mint egy eg�sz sz�m �s v�rhat�an
��rdekes� tulajdons�gokkal b�r. Nyilv�nval�an az egyik ilyen a hossza. Az objektum hossz�t a
standard len() f�ggv�nnyel k�rdezhetj�k meg, melynek bemeneti adata maga az objektum (a len
az angol length sz� r�vid�t�se, ami hossz�s�got jelent). Figyelj�k meg az al�bbi p�ld�n,
hogy a sz�k�z is belesz�m�t a hosszba:
	>>> s= "Szia Python"
	>>> len(s)
	11
	>>> len("T�k�r")
	5

	>>> s= "T�kr�m t�kr�m"
	>>> s1= "�KR�M �KR�M"
	>>> s.upper()
	'T�KR�M T�KR�M'
	>>> s1.lower()
	'�kr�m �kr�m'


----------------------------------------------------------------


Az objektumok tulajdons�gai k�z� soroljuk az �n. met�dusokat is, azaz a �bels��
f�ggv�nyeiket. Az eddig megismert standard f�ggv�nyek, mint p�ld�ul a min(), type(),
len(), mindig megh�vhat�k a program b�rmely r�sz�ben, de a met�dusokhoz el�bb l�tre
kell hozni egy objektumot, hiszen abban vannak ezek a f�ggv�nyek �be�gyazva�. A fenti jobb
oldali keretben k�t met�dus haszn�lata l�that�, az egyik a l�ncban minden karaktert nagybet�ss�
alak�t, a m�sik pedig kisbet�ss�. A h�v�s m�dja egyszer�: a kiv�lasztott objektum neve ut�n egy ' .'
�ll, majd a met�dus neve k�vetkezik a z�r�jelekkel �s azok k�z�tt az argumentumok, ha ez
ut�bbiak egy�ltal�n kellenek (itt a fenti p�ld�ban most nem). Teh�t a met�dusok �s a standard
f�ggv�nyek megh�v�sa k�z�tt nincs k�l�nbs�g, de az el�bbi neve kieg�sz�l az �t tartalmaz�
objektum nev�vel.
Meglepet�sk�nt hathat, hogy maguk a f�ggv�nyek �s a met�dusok is objektumok:
	>>> type(min)
	<class 'builtin_function_or_method'>
	>>> s= "l�nc"
	>>> type( s.upper)
	<class 'builtin_function_or_method'>

A fenti p�ld�kban a type() f�ggv�ny argumentumak�nt a min() f�ggv�nyre �s a karakterl�nc
upper() met�dus�ra t�rt�n� hivatkoz�st adtuk �t, azaz nem h�vtuk meg ezeket a f�ggv�nyeket,
amit az is mutat, hogy elhagytuk m�g�l�k a z�r�jeleket. Ha megh�v�ssal adjuk �t �ket, pl.
type(min(10,2,3)) akkor a visszat�r�si �rt�k t�pus�t fogjuk megkapni.

Az objektumok azon met�dusai, amelyeknek van visszat�r�si �rt�ke, egy-egy �jabb
objektumot eredm�nyeznek. Az �j objektum t�pusa b�rmi lehet: azt csak a met�dus programk�dja
hat�rozza meg, azaz nem kell hogy megegyezzen a kiindul�si objektum t�pus�val. A visszat�r�si
�rt�kk�nt kapott objektumnak is vannak met�dusai, �gy ezeket is megh�vhatjuk:
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

A fenti k�t p�ld�ban szeml�ltett�k a k�tf�le elj�r�st a visszat�r�si �rt�kek met�dusainak
megh�v�s�ra. Az els� esetben az upper() visszat�r�si �rt�ke az s1-be ker�lt, ami karakterl�nct�pus�.
Ezut�n az s1 count() met�dus�t h�vtuk, ami megsz�molja az argumentumk�nt megadott
karakterl�nc el�fordul�s�t az s1-ben, �s ennek megfelel�en visszaadott egy sz�mot. A m�sodik
esetben ezt egyetlen programsorban megtessz�k, a pontokat �halmozva�. Itt nem hozunk l�tre
k�l�n s1 v�ltoz�t, hanem ekkor a Python-�rtelmez�, a �szem�nk el�l rejtve� k�sz�t egy �n.
ideiglenes v�ltoz�t, amelynek a nev�t nem tudatja vel�nk. Az ideiglenes (vagy �tmeneti) v�ltoz�t
az �rtelmez� megsz�nteti, amint m�r nincs r� sz�ks�ge.

A sz�mok, mint az int- �s a float t�pus�ak is, objektumok, de nekik term�szetesen nincs
upper() met�dusuk: ha m�gis megpr�b�ljuk ezt haszn�lni, akkor az �rtelmez� hibajelz�ssel le�ll.

Id�nk�nt sz�ks�g van arra, hogy egy adott t�pus� v�ltoz�t egy m�sikba alak�tsunk �t: ezt
nevezz�k konverzi�nak. Eml�tett�k, hogy az input() visszat�r�si �rt�ke mindig karakterl�nc �s
ez�rt a sz�mok bebillenty�z�se ut�n �talak�t�st kell v�gezn�nk.
	>>> d= input("K�rek egy sz�mot: ")
	K�rek egy sz�mot: 32
	>>> 1+d
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	>>>

A fenti programban nem tudtuk az 1-hez a 32-�t hozz�adni, mert az �rtelmez� nem tudja hogyan
kell egy eg�sz sz�mot �s egy karakterl�ncot �sszeadni, ami nem meglep�. A k�vetkez�kben a
m�velet m�r sikeres lesz:
	>>> d= input("K�rek egy sz�mot: ")
	K�rek egy sz�mot: 32
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

	>>> d= input("K�rek egy sz�mot: ")
	K�rek egy sz�mot: 5.89
	>>> d
	'5.89'
	>>> type(d)
	<class 'str'>
	>>> d= float(d)
	>>> d+1.11
	7.0

A fenti programokban a d v�ltoz�t az int() �s a float() standard f�ggv�nyek megh�v�s�val
�talak�tjuk, �s az �j �rt�keket ugyancsak a d nev� v�ltoz�ba tessz�k, b�r tehett�k volna egy
m�sikba is. A konverzi�t azonban nem lehets�ges mindig elv�gezni, ilyen eseteket l�tunk a
k�vetkez�kben:
	>>> int( "34 Ft")
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '34 Ft'

A fenti utas�t�s v�grehajt�sakor az �rtelmez� arra panaszkodik hogy egy t�zes sz�mrendszerben
megadott karakterl�ncot alak�tott volna �t, de �rv�nytelen karaktert tal�lt, nyilv�n az 'F' �s 't'
okozta a probl�m�t. A k�vetkez� keret els� utas�t�s�ban a '0xFF' karakterl�ncn�l ugyanez a
helyzet �llt el�, mivel az 'x' �s 'F' karakterek �rtelmezhetetlenek a t�zes sz�mrendszerben. Megadva
azonban m�sodik argumentumk�nt a 16-ot, mint alapsz�mot, a konverzi� sikeresen megt�rt�nik
(egy k�s�bbi fejezetben m�g lesz sz� a tizenhatos sz�mrendszerr�l). A '2.7' l�nc �talak�t�sa sem
siker�lhet az int() f�ggv�nnyel, mert egy eg�sz sz�m nem tartalmazhat pontot:
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

Az el�bbi p�ld�kban karakterl�ncokb�l k�sz�tett�nk sz�mokat, de az egyik t�pus� sz�mb�l is
lehets�ges egy m�sikat k�sz�teni, s�t sz�mb�l karakterl�ncot, �s ak�rmib�l bool v�ltoz�t:
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

Egy float sz�mb�l az int() f�ggv�ny �gy k�sz�t eg�sz sz�mot, hogy egyszer�en elhagyja a
tizedespont ut�ni sz�mjegyeket. A kor�bban megismert round() f�ggv�ny ezt m�sk�ppen teszi.
Vegy�k �szre, hogy az int() nem ugyan�gy viselkedik, ha egy tizedespontot tartalmaz� sz�mot
float-k�nt illetve karakterl�nck�nt adunk �t neki.
A 0 sz�m bool �rt�ke False �s minden m�s sz�m� True. Egy nem �res karakterl�nc bool �rt�ke
is True. Figyelj�k meg, hogy az egyetlen sz�k�zt tartalmaz� karakterl�nc nem egy �res l�nc! Az
�res karakterl�ncot szorosan egym�s mell� �rt id�z�jelekkel �br�zoljuk �s ennek �rt�ke m�r False.
A None objektum bool �rt�ke False. Fontos megjegyezni, hogy a 'None' egy karakterl�nc �s
nem a None objektum.

Az eddigiekben m�r l�ttuk hogyan lehet a v�ltoz�kat l�trehozni, �s felmer�l a k�rd�s, hogy
meg lehet �ket sz�ntetni, ha m�r nincs r�juk sz�ks�g. Igen, egy v�ltoz�t a del utas�t�ssal
t�r�lhet�nk, ami ut�n a nev�nek haszn�lata m�r hib�hoz vezet:
	>>> mi = �t�k�r�
	>>> mi
	't�k�r'
	>>> del mi
	>>> mi
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'mi' is not defined


A �v�ltoz� �s az �objektum� kifejez�seket gyakorlatilag egym�s helyett haszn�ltuk, �s
haszn�lhatjuk a j�v�ben is, de nem minden esetben, mert val�j�ban nem ugyanazt
jelentik. Ezt �gy vil�g�thatjuk meg, ha sz�mba vessz�k a tulajdons�gaikat. Egy
objektumnak van �rt�ke, esetleg hossza, lehetnek met�dusai �s m�g m�s tulajdons�gai, de
mindenekel�tt van neki t�pusa ; neve azonban �nmag�ban nincs . Ezzel szemben a v�lt�z�
rendelkezik egy n�vvel, �s a szemeink el�l rejtetten t�rol egy mem�riac�met, amely valamely
objektumnak a sz�m�t�g�p mem�ri�j�ban elfoglalt kezd�c�m�vel egyezik meg. A v�ltoz�
val�j�ban csak egy hivatkoz�s, �n. referencia egy adott objektumra, neves�ti azt, de nem maga az
objektum. Amikor egy v�ltoz� �rt�k�r�l vagy pl. a hossz�r�l, esetleg a met�dusair�l besz�l�nk,
akkor val�j�ban az �ltala neves�tett objektum tulajdons�gaival ruh�zzuk fel azt, de csak sz�ban.
L�tni fogjuk, hogy egy objektumot t�bb n�vvel is illethet�nk, azaz t�bb v�ltoz� is mutathat
ugyanarra az objektumra. S�t ezt a Python-�rtelmez� a tudtunk n�lk�l is sokszor alkalmazza,
hogy takar�koskodjon a rendelkez�sre �ll� mem�ri�val. A k�t fogalom k�zti k�l�nbs�get jobban
fogjuk �rteni, ha foglalkozunk egy kicsit a mem�riac�mekkel.

K�t objektum egyidej�leg nem foglalhatja el ugyanazt a helyet a mem�ri�ban. A standard id()
f�ggv�nnyel (az angol identity sz� r�vid�t�se, mely identit�st, azonoss�got, szem�lyazonoss�got
jelent) lek�rdezhetj�k az objektumokat azonos�t� mem�riac�meket:
	>>> a= 5
	>>> b= 5
	>>> id(a),id(b)
	(137396096, 137396096)
	>>> f1= 3.14
	>>> f2= 3.14
	>>> id(f1),id(f2)
	(155423668, 155423604)
	>>>

Mint a p�ld�b�l l�that�, az eg�sz sz�mhoz a Python csak egyszer hozta l�tre az objektumot, m�g a
tizedes pontot tartalmaz�khoz mindk�t esetben �jat gy�rtott. A Python dokument�ci�j�ban
olvashat�, hogy egy adott eg�sz sz�m objektuma nem m�dos�that�. Ez nem jelent korl�toz�st,
mert ezt az eg�sz sz�mot tetsz�leges alkalommal felhaszn�lhatjuk m�s objektumok l�trehoz�s�ra.
P�ld�ul az al�bbi keretben az a=a+2 kifejez�s eset�n nem az 5-�t tartalmaz� objektum �rt�k�t
m�dos�tjuk 7-re, hanem az a �rt�k�nek a felhaszn�l�s�val l�trehozzuk a 7-et tartalmaz� �j
objektumot, s mostant�l az a v�ltoz� m�r erre fog �mutatni�, ezt fogja neves�teni. A b tov�bbra is
az 5-�s objektumra fog hivatkozni. Egy �j c v�ltoz�nak a 7-es �rt�ket adva, nem keletkezik �j
objektum, hanem a c a m�r az el�bbiekben l�trej�tt objektumra fog mutatni:
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

Ha t�r�lj�k az egy adott objektumra mutat� �sszes v�ltoz�t, akkor az az objektum m�r
el�rhetetlen lesz �s �gy felesleges is, s ez�rt azt a Python-�rtelmez� el�bb vagy ut�bb kit�rli a
mem�ri�b�l egy �szem�tgy�jt�snek� nevezett elj�r�sban.
Egy objektum t�rl�sekor felszabadul az addig �ltala lefoglalt mem�ria, �s azt egy �j objektum
megkaphatja, teh�t az id() �ltal jelzett azonos�t� is meg fog egyezni a kor�bban l�tezett
objektum�val. Az egyidej�leg l�tez� k�l�nb�z� objektumokat azonban az id() soha nem fogja
azonosnak jelezni!

Az al�bbi keretben a karakterl�nc-t�pus� objektumokn�l is tapasztalhat� a takar�koss�g elve. Az
input() f�ggv�ny �ltal beolvasott l�nc azonban m�r egy �j objektum lesz, b�r ugyanolyan
karakterl�ncot tartalmaz mint az s1 �s s2 �ltal hivatkozott objektum:
	>>> s1= "Szia"
	>>> s2= "Szia"
	>>> s3= input(" K�sz�n�s: ")
	K�sz�n�s: Szia
	>>> id(s1),id(s2),id(s3)
	(3073928320, 3073928320, 3073928608)
	>>>

