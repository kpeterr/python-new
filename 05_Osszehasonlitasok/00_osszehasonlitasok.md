==, < , > , <= , >= , !=

A k�l�nb�z� objektumt�pusok kialak�t�s�n�l meg kellett hat�rozni, hogy a fenti oper�torok
eset�n mely jellemz�j�k legyen figyelembe v�ve. Az �sszehasonl�t�s eredm�ny vagy a False vagy
a True bool �rt�k lesz.

A felsorolt oper�torok a matematik�ban megszokott (aritmetikai) m�don m�k�dnek a
sz�mok k�z�tt: az �sszehasonl�t�s alapja a nagys�guk lesz. Ha a k�t sz�m nem azonos
t�pus�, akkor az �rtelmez� valamilyen k�z�s alakra hozva v�gzi el a hasonl�t�st. P�ld�k
float �s int eset�ben:
	>>> 3.0 == 3
	True
	>>> 10 >= 10.009
	False
	>>> 2 != 2.0
	False

A karakterl�ncok �s a k�s�bb megismerend� lista, sokas�g, k�szlet, sz�t�r objektumok t�bb
elemet tartalmazhatnak, ami�rt kont�nernek is nevezik �ket. Ezek akkor tekintend�k
egyenl�nek, ha ugyanolyan elemeket tartalmaznak, s�t a sz�t�r �s a k�szlet kiv�tel�vel, az
elemeknek m�g azonos poz�ci�ban is kell lenni�k. K�t karakterl�nc egyenl�s�ge, teh�t
akkor �ll fenn, ha az azonos helyeken azonos karaktereket tartalmaznak:
	>>> s= "�sszehasonl�t�s"
	>>> s1= input("l�nc=")
	l�nc=�sszehasonl�t�s
	>>> s == s1
	True

A kont�nerek �sszehasonl�t�sa bonyolultabb lesz, ha a kisebb vagy nagyobb jelet is
alkalmazzuk, mert ez felt�telezi, hogy az objektumok sorba rendezhet�ek valamilyen
tulajdons�guk alapj�n. K�t karakterl�nc �sszevet�se a bennfoglalt karakterek �n.
lexikografikus sorrendje szerint ker�l meghat�roz�sra. Ha a l�ncok csak az angol �b�c�
bet�it tartalmazz�k, akkor az eredm�ny megfelel az angol �b�c� bet�sorrendj�nek. Ahhoz
azonban, hogy a magyar vagy p�ld�ul a n�met �b�c� szerint t�rt�njen a rendez�s, tov�bbi
er�fesz�t�seket kell tenn�nk. Az al�bbi els� k�t p�ld�ban magyar szavak szerepelnek, de
mivel ezek karakterei benne vannak az angol �b�c�ben is, �s m�g az ottani sorrendis�g�k is
azonos a magyar �b�c�ben l�v�vel, �gy az eredm�nyek �magyarul� is helyesek; a
harmadikban p�ld�ban az �kezetes bet�k miatt azonban m�r nem megfelel� az eredm�ny. E
probl�m�t majd a k�s�bbiekben orvosoljuk.
	>>> s1= "ablak"
	>>> s2= "kocsi"
	>>> s1 < s2
	True

	>>> s1= "ablakmos�"
	>>> s2= "ablak"
	>>> s1 > s2
	True

	>>> s1="�r�m"
	>>> s2="t�k�r"
	>>> s1 < s2
	False

A list�nak list�val, sokas�gnak sokas�ggal val� �sszehasonl�t�sa eset�n az azonos
poz�ci�kon l�v� elemek �sszevet�se t�rt�nik meg, �s az els� k�l�nb�z� p�r eredm�nye
adja a v�geredm�nyt. Ha az elemenk�nti �sszehasonl�t�s sor�n az egyik kont�ner
r�videbbnek bizonyul, akkor az lesz a �kisebb�.
A sz�t�rak egym�s k�zt nem rendezhet�k, ez�rt k�z�tt�k a kisebb-nagyobb jelek
haszn�lata hib�t eredm�nyez. A sz�t�rakkal a k�s�bbiekben majd r�szletesen
megismerked�nk.
K�t k�szletn�l m�g az is el�fordulhat, hogy az egyik kisebb is meg nem is, mint a m�sik, de
ezt is majd egy m�sik fejezetben t�rgyaljuk meg r�szletesen.
A bool v�ltoz�kn�l a False mindig kisebb, mint a True.

	>>> "112" < 3
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unorderable types: str() < int()
	>>> "112" == 3
	False
	>>> "112" < "3"
	True
A fenti p�ld�ban az els� �ll�t�s egy karakterl�nc �s egy eg�sz sz�m sorrendj�re k�rdezett r�,
ami �rtelmetlen ezen k�l�nb�z� t�pus� objektumok k�z�tt, s ez�rt hiba�zenetet kaptunk. A
m�sodik �ll�t�s a k�t k�l�nb�z� t�pus� objektum egyenl�s�g�t �ll�tja, ami nem igaz. A
harmadikban k�t olyan karakterl�nc k�z�tti sorrendre vagyunk k�v�ncsiak, amelyek csak
sz�mjegyeket tartalmaznak, de az eredm�ny term�szetesen nem egyezik meg a sz�mokra
vonatkoz� (aritmetikai) �sszehasonl�t�s eredm�ny�vel, hiszen most az �b�c� szerinti
(lexikografikus) sorba rendez�st kell alkalmazni. A karakterl�ncban a sz�mjegyek ugyanolyan
jeleknek tekintend�k, mint p�ld�ul a bet�k, a pont vagy a felki�lt�jel; �s ezekre a lexikografikus
rendez�si szab�ly vonatkozik.
Amely objektumok k�z�tt a rendez�s �rtelmezett, ott haszn�lhatjuk az erre t�maszkod�
f�ggv�nyeket:
	>>> min("kocsi","ablak")
	'ablak'


-----------------------------------------------------------


in, not in

A k�t oper�torral megk�rdezhetj�k, hogy egy objektumot egy m�sik tartalmaz-e. Ezek a
kont�nert�pus� objektumok eset�n rendk�v�l hasznosak. Az eredm�ny bool t�pus� lesz.
	>>> s= "�rhaj�z�s"
	>>> "�" in s
	True
	>>> "haj�" in s
	True
	>>> s= "�rhaj�z�s"
	>>> "haj" not in s
	False
	>>> "q" in s
	False


-----------------------------------------------------------


is, is not

Ezen oper�torokkal az objektumok azonoss�g�t tesztelhetj�k, hasonl�an ahogy azt az
id() f�ggv�nnyel a �V�ltoz�k �s objektumok� c�m� fejezetben m�r l�ttuk. Az eredm�ny bool t�pus�
lesz.
	>>> f1, f2 = 3.14, 3.14
	>>> id(f1), id(f2)
	(152859508, 152859508)
	>>> f1 is f2
	True
	>>> f3= 3.14
	>>> f4= 3.14
	>>> id(f3), id(f4)
	(152859476, 152859556)
	>>> f3 is not f4
	True
	>>> f1 is not f3
	True

	>>> f1 = f2 = 1.5
	>>> id(f1), id(f2)
	(152859460, 152859460)
	>>> f1 is f2
	True
	>>> f1= 2*f1
	>>> id(f1)
	152859444
	>>> f1 is f2
	False
	>>>
�rdekes dolgokat figyelhet�nk meg a takar�kos mem�riakezel�st illet�en. Ha a
lebeg�pontos sz�moknak egyetlen utas�t�ssal adjuk ugyanazt az �rt�ket, akkor csak
egyetlen float objektum j�n l�tre, de az �rt�k megv�ltoztat�s�val kett�v�lnak.


-----------------------------------------------------------

not, or, and

A Boole-algebra oper�torai is j�l haszn�lhat�k �ll�t�sok megfogalmaz�s�ra.
A programoz�sban a k�t�rt�k� Boole-algebra haszn�latos, amelyben csak k�t �rt�k van,
a hamis �s az igaz, �s ezek egym�s ellentettjei. Szok�sos m�g a 0 �s az 1 sz�mokkal
is jel�lni az �rt�keket, a Pythonban a False �s a True objektumok t�ltik be ezt a szerepet.
Az ilyen oper�torokat tartalmaz� kifejez�st logikai kifejez�snek nevezz�k.

Nagyon fontos jellemz�je a logikai kifejez�sek feldolgoz�s�nak, hogy az �rtelmez� az
utolj�ra kisz�m�tott r�szkifejez�s �rt�k�t adja eredm�nyk�nt, ami nem felt�tlen bool
t�pus�. Ez teh�t jelent�s elt�r�s a kor�bban t�rgyalt �sszehasonl�t� oper�torok
alkalmaz�s�hoz k�pest, amelyek bool t�pust szolg�ltattak. Lejjebb l�tunk majd p�ld�kat.

A not a tagad�s oper�torak�nt az ut�na �ll� kifejez�s bool �rt�k�nek az ellentettj�t adja
meg.
Az or az �n. �vagy kapcsolatot� jelenti, az ezzel �sszekapcsolt r�sz�ll�t�sok b�rmelyik�nek
igaz volta az eg�sz kifejez�s igaz volt�t eredm�nyezi. Csak ha minden r�szkifejez�s hamis,
akkor lesz az eg�sz is az. (Igaz, ha ez VAGY az igaz.)
Az and az ��s kapcsolatot� testes�ti meg, amely csak akkor ad eredm�ny�l igazat, ha a
kifejez�s minden egyes r�sz�ll�t�sa is igaz, azaz m�r az egyik hamiss�ga r�v�n az eg�sz
kifejez�s hamis lesz. (Csak akkor igaz, ha ez is �S az is igaz.)

A �V�ltoz�k �s objektumok� c�m� fejezetben m�r volt r�la sz�, hogy minden objektumnak
van bool �rt�ke:
� A 0 b�rmilyen form�ban (pl. 0.0 is) False, minden m�s sz�m bool �rt�ke True.
� Egy elemeket tartalmaz� kont�nerobjektum (pl. karakterl�nc, lista) �rt�ke True, az
�res kont�ner� azonban False.
� Egy �k�z�ns�ges�, azaz nem kont�nertulajdons�g� objektum �rt�ke True.
(Megjegyezz�k, hogy ha majd tudunk saj�t objektumokat k�sz�teni, akkor azt is
meghat�rozhatjuk, hogy annak mi legyen a bool �rt�ke.)
� A None �res objektum bool �rt�ke False.

A Python-�rtelmez� �gy dolgozza fel a logikai kifejez�seket, hogy elker�li a felesleges
sz�m�t�sokat. Az �rtelmez� balr�l jobbra halad �s ha egy or kapcsolatban az els� kifejez�s
ki�rt�kel�se igaz lesz, akkor tudv�n, hogy a teljes kifejez�s is az lesz, m�r nem sz�ks�ges
ki�rt�kelnie a m�sodik kifejez�st. Az and kapcsolatn�l viszont akkor nem �rdemes tov�bb
haladnia, ha az els� kifejez�s hamis lesz, hiszen akkor a teljes kifejez�s is az lesz.
N�zz�nk p�ld�kat a vagy kapcsolatra:
	>>> "l�" or "teve"
	'l�'
	>>> "" or "teve"
	'teve'
	>>> "" or ""
	''
	>>> not "l�" or 5-2*1.0
	3.0
	>>> bool( not "l�" or 5-2*1.0 )
	True
	>>> 0.0 or not 10
	False
	>>> 0 or None or "" or 2**3-8 or False or not True or "Szia"
	'Szia'

Az els� p�ld�ban az els� operandus egy nem �res karakterl�nc, aminek a bool �rt�ke True, az
oper�tor egy vagy kapcsolat, �s mivel ezekb�l m�r k�vetkezik a teljes �ll�t�s igaz volta, az
�rtelmez� nem sz�mol tov�bb. Az eredm�ny az utolj�ra ki�rt�kelt kifejez�s eredm�nye lesz, de
nem a bool �rt�ke (amit csak az �ll�t�s ki�rt�kel�s�hez haszn�ltunk). A 'l�' kifejez�s pedig
ki�rt�kelve is 'l�'.
A m�sodik p�ld�ban az els� operandus egy �res karakterl�nc, amelynek �rt�ke hamis, ez�rt ki
kell �rt�kelni a m�sik oldalt is, amelynek eredm�nye a 'teve'.
A harmadik p�ld�ban mindk�t operandus bool �rt�ke hamis �s �gy az eg�sz kifejez�s bool
�rt�ke is hamis, de nem ez az eredm�ny, hanem az utols�nak ki�rt�kelt kifejez�s �rt�ke,
ami maga a jobb oldalon szerepl� karakterl�nc, �s ez most �res.
A negyedik kifejez�sben a nem �res karakterl�nc bool �rt�ke igaz, a tagad�s folyt�n ez hamis
lesz, ez�rt a m�sik oldalon l�v� kifejez�st is ki kell �rt�kelni �s �gy 3.0 lesz az eredm�ny,
egy�bk�nt a teljes kifejez�s bool �rt�ke True, hiszen egy 0-t�l k�l�nb�z� sz�m az eredm�ny.
Az �t�dik �ll�t�sban a m�sodik kifejez�s not-tal kezd�dik, ez pedig a m�g�tte �ll� kifejez�s
bool �rt�k�nek ellentettj�t k�pezi, teh�t a teljes kifejez�s ki�rt�kel�se most bool �rt�ket
eredm�nyez, nem �gy mint a megel�z� p�ld�kban.

K�vetkezzenek a p�ld�k az �s kapcsolatra:
	>>> "l�" and "teve"
	'teve'
	>>> "" and "teve"
	''
	>>> "" and ""
	''
	>>> not "l�" and 5-2*1.0
	False
	>>> bool( not "l�" and 5-2*1.0 )
	False
	>>> 0.0 and not 10
	0.0
	>>> 0 and None and "" and 2**3-8 and False and not True and "Szia"
	0
	>>> 1 and not None and "l�nc" and 8 and True and not False and "Szia"
	'Szia'

Az els� p�ld�ban az els� operandus �rt�ke igaz, ez�rt m�g �van rem�ny�,
hogy az eg�sz kifejez�s igaz lesz, de ehhez meg kell n�zni a m�sodik operandust is,
�gy az adja az eredm�nyt.
A m�sodik p�ld�ban az els� operandus egy �res karakterl�nc, aminek a bool �rt�ke hamis,
�s ez szolg�l eredm�nyk�nt is, mert m�r a m�sik operandus megvizsg�l�sa n�lk�l is tudhat�,
hogy az eg�sz kifejez�s hamis lesz. A t�bbi kifejez�s �rtelmez�s�t a olvas�ra b�zzuk.

Term�szetesen az and, az or �s a not oper�torok egy�tt is haszn�lhat�ak. Azonban, ha t�l
sokat tesz�nk bel�l�k vegyesen egy kifejez�sbe, akkor az igen �ttekinthetetlenn� v�lhat,
k�nnyen el�fordulhat, hogy nem az lesz az eredm�nye, mint amit v�rn�nk.
A ki�rt�kel�s sorrendj�n�l figyelembe kell venni az oper�torok k�t�si er�ss�g�t is,
a not k�t a leger�sebben, gyeng�bben az and, �s a leggyeng�bben az or (l�sd a help('+')-et
interakt�v m�dban). Javasolt ink�bb t�bb r�videbb kifejez�st haszn�lni, illetve z�r�jelekkel
csoportos�tani a r�szkifejez�seket, amivel a ki�rt�kel�s sorrendje is megv�ltoztathat�.
Az al�bbi els� p�lda els� kifejez�s�ben a m�sodik True-t �s az utols� False-t az and er�sebben
k�ti, mint az or az els� k�t True-t, s ez�rt a ki�rt�kel�s �gy t�rt�nik, ahogy azt a m�sodik
kifejez�sben a z�r�jelekkel jelezt�k; a harmadik kifejez�sben egy m�sf�le z�r�jelez�ssel
m�dos�tottuk a k�t�seket �s �gy az eredm�nyt is.
Hasonl�an �rtelmezhet�k a m�sodik p�lda kifejez�sei is:
	>>> True or True and False
	True
	>>> True or (True and False)
	True
	>>> (True or True) and False
	False
	
	>>> False and False or True
	True
	>>> (False and False) or True
	True
	>>> False and (False or True)
	False

Az al�bbiakban bemutatjuk az �rtelmez� m�k�d�s�t egy �ttag� kifejez�sen. L�p�senk�nt jel�lt�k,
amin az �rtelmez� �ppen dolgozik: az operandust al�h�z�ssal, az oper�tort pedig kiemelt
sz�nnel. Az �th�zott operandussal az �rtelmez�nek nem kell t�r�dnie, a d�lten szedett �rt�kek
a r�szeredm�nyek:
False and False and True or False or True
	 False      and True or False or True
			   False     or False or True
					   False      or True
								   True


A fejezet eddigi p�ld�iban a k�nnyebb �rthet�s�g kedv��rt f�leg olyan kifejez�seket
haszn�ltunk, ahol az oper�tor mindk�t oldal�n csak egy-egy operandus �llt, sokszor ezek is
csak a True �s False �rt�kek voltak; ezek azonban tetsz�legesen komplik�lt kifejez�sek is
lehetnek:
	>>> a,b,c = 1,10,100
	>>> s= "Python"
	>>> a+b+c == 100 or "P" in s and ( b >= len(s) or not b )
	True

A tov�bbiakban meg szeretn�nk eml�teni n�h�ny �rdekesebb kifejez�s �rtelmez�s�t. Az al�bbi
p�ld�ban az els� sor n�gy v�ltoz�nak ugyanazt az �rt�ket adja. A harmadik sorban egy az
�sszehasonl�t� oper�torok l�ncolat�val megadott kifejez�s l�that�, amelyet a Python �gy
�rtelmez, amint azt az �t�dik sorban megadtuk, s ez teljesen megegyezik a matematik�ban
megszokottal, de sok m�s programnyelv ezt m�sk�ppen kezeli:
	>>> a = b = c = d = 100
	>>> e = 99
	>>> a == b >= 50 <= e + 1 == c != d+1
	True
	>>> a == b and b >= 50 and 50 <= e + 1 and e + 1 == c and c != d + 1
	True

Az al�bbi programocska m�sodik sor�t sz�ban felmondva nem a sz�m�tott False �rt�ket v�rjuk:
�A b egyenl� vagy a-val vagy b-vel.�
	>>> a,b = 10,0
	>>> b == (a or b)
	False
Mint tudjuk az or oper�tor miatt a z�r�jelen bel�l a ki�rt�kel�s le�ll az els� operandusn�l,
ha annak bool �rt�ke igaz. Itt ez igaz, az eredm�ny az a lesz, azaz 10, ami nyilv�n nem
egyenl� 0 -val.

A fejezetben t�rgyalt oper�torokkal �sszef�z�tt kifejez�sek mindegyik�nek volt sz�m�tott
�rt�ke, vagy az utols� r�szkifejez�s eredm�nye vagy egy bool �rt�k, s �gy nem meglep� teh�t,
hogy ezek �rt�kad� utas�t�sokban is nagyon hasznosak. Miel�tt az ezt bemutat� programot
megadn�nk, m�g meg kell eml�teni egy j�l haszn�lhat� �rt�kad� utas�t�st, az if-else felt�teles
szerkezetet:
	obj = kif1 if tesztkif else kif2
Az �rtelmez� el�sz�r a tesztkif kifejez�st �rt�keli ki, �s ha az igaz, akkor a kif1
ki�rt�kel�s�nek az eredm�ny�t �rja be az obj nev� v�ltoz�ba, ha hamis akkor a kif2 eredm�ny�t.

Boolean Operators
------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True