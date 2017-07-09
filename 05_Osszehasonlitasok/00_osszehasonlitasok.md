==, < , > , <= , >= , !=

A különbözõ objektumtípusok kialakításánál meg kellett határozni, hogy a fenti operátorok
esetén mely jellemzõjük legyen figyelembe véve. Az összehasonlítás eredmény vagy a False vagy
a True bool érték lesz.

A felsorolt operátorok a matematikában megszokott (aritmetikai) módon mûködnek a
számok között: az összehasonlítás alapja a nagyságuk lesz. Ha a két szám nem azonos
típusú, akkor az értelmezõ valamilyen közös alakra hozva végzi el a hasonlítást. Példák
float és int esetében:
	>>> 3.0 == 3
	True
	>>> 10 >= 10.009
	False
	>>> 2 != 2.0
	False

A karakterláncok és a késõbb megismerendõ lista, sokaság, készlet, szótár objektumok több
elemet tartalmazhatnak, amiért konténernek is nevezik õket. Ezek akkor tekintendõk
egyenlõnek, ha ugyanolyan elemeket tartalmaznak, sõt a szótár és a készlet kivételével, az
elemeknek még azonos pozícióban is kell lenniük. Két karakterlánc egyenlõsége, tehát
akkor áll fenn, ha az azonos helyeken azonos karaktereket tartalmaznak:
	>>> s= "összehasonlítás"
	>>> s1= input("lánc=")
	lánc=összehasonlítás
	>>> s == s1
	True

A konténerek összehasonlítása bonyolultabb lesz, ha a kisebb vagy nagyobb jelet is
alkalmazzuk, mert ez feltételezi, hogy az objektumok sorba rendezhetõek valamilyen
tulajdonságuk alapján. Két karakterlánc összevetése a bennfoglalt karakterek ún.
lexikografikus sorrendje szerint kerül meghatározásra. Ha a láncok csak az angol ábécé
betûit tartalmazzák, akkor az eredmény megfelel az angol ábécé betûsorrendjének. Ahhoz
azonban, hogy a magyar vagy például a német ábécé szerint történjen a rendezés, további
erõfeszítéseket kell tennünk. Az alábbi elsõ két példában magyar szavak szerepelnek, de
mivel ezek karakterei benne vannak az angol ábécében is, és még az ottani sorrendiségük is
azonos a magyar ábécében lévõvel, így az eredmények „magyarul” is helyesek; a
harmadikban példában az ékezetes betûk miatt azonban már nem megfelelõ az eredmény. E
problémát majd a késõbbiekben orvosoljuk.
	>>> s1= "ablak"
	>>> s2= "kocsi"
	>>> s1 < s2
	True

	>>> s1= "ablakmosó"
	>>> s2= "ablak"
	>>> s1 > s2
	True

	>>> s1="öröm"
	>>> s2="tükör"
	>>> s1 < s2
	False

A listának listával, sokaságnak sokasággal való összehasonlítása esetén az azonos
pozíciókon lévõ elemek összevetése történik meg, és az elsõ különbözõ pár eredménye
adja a végeredményt. Ha az elemenkénti összehasonlítás során az egyik konténer
rövidebbnek bizonyul, akkor az lesz a „kisebb”.
A szótárak egymás közt nem rendezhetõk, ezért közöttük a kisebb-nagyobb jelek
használata hibát eredményez. A szótárakkal a késõbbiekben majd részletesen
megismerkedünk.
Két készletnél még az is elõfordulhat, hogy az egyik kisebb is meg nem is, mint a másik, de
ezt is majd egy másik fejezetben tárgyaljuk meg részletesen.
A bool változóknál a False mindig kisebb, mint a True.

	>>> "112" < 3
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unorderable types: str() < int()
	>>> "112" == 3
	False
	>>> "112" < "3"
	True
A fenti példában az elsõ állítás egy karakterlánc és egy egész szám sorrendjére kérdezett rá,
ami értelmetlen ezen különbözõ típusú objektumok között, s ezért hibaüzenetet kaptunk. A
második állítás a két különbözõ típusú objektum egyenlõségét állítja, ami nem igaz. A
harmadikban két olyan karakterlánc közötti sorrendre vagyunk kíváncsiak, amelyek csak
számjegyeket tartalmaznak, de az eredmény természetesen nem egyezik meg a számokra
vonatkozó (aritmetikai) összehasonlítás eredményével, hiszen most az ábécé szerinti
(lexikografikus) sorba rendezést kell alkalmazni. A karakterláncban a számjegyek ugyanolyan
jeleknek tekintendõk, mint például a betûk, a pont vagy a felkiáltójel; és ezekre a lexikografikus
rendezési szabály vonatkozik.
Amely objektumok között a rendezés értelmezett, ott használhatjuk az erre támaszkodó
függvényeket:
	>>> min("kocsi","ablak")
	'ablak'


-----------------------------------------------------------


in, not in

A két operátorral megkérdezhetjük, hogy egy objektumot egy másik tartalmaz-e. Ezek a
konténertípusú objektumok esetén rendkívül hasznosak. Az eredmény bool típusú lesz.
	>>> s= "ûrhajózás"
	>>> "ó" in s
	True
	>>> "hajó" in s
	True
	>>> s= "ûrhajózás"
	>>> "haj" not in s
	False
	>>> "q" in s
	False


-----------------------------------------------------------


is, is not

Ezen operátorokkal az objektumok azonosságát tesztelhetjük, hasonlóan ahogy azt az
id() függvénnyel a „Változók és objektumok” címû fejezetben már láttuk. Az eredmény bool típusú
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
Érdekes dolgokat figyelhetünk meg a takarékos memóriakezelést illetõen. Ha a
lebegõpontos számoknak egyetlen utasítással adjuk ugyanazt az értéket, akkor csak
egyetlen float objektum jön létre, de az érték megváltoztatásával kettéválnak.


-----------------------------------------------------------

not, or, and

A Boole-algebra operátorai is jól használhatók állítások megfogalmazására.
A programozásban a kétértékû Boole-algebra használatos, amelyben csak két érték van,
a hamis és az igaz, és ezek egymás ellentettjei. Szokásos még a 0 és az 1 számokkal
is jelölni az értékeket, a Pythonban a False és a True objektumok töltik be ezt a szerepet.
Az ilyen operátorokat tartalmazó kifejezést logikai kifejezésnek nevezzük.

Nagyon fontos jellemzõje a logikai kifejezések feldolgozásának, hogy az értelmezõ az
utoljára kiszámított részkifejezés értékét adja eredményként, ami nem feltétlen bool
típusú. Ez tehát jelentõs eltérés a korábban tárgyalt összehasonlító operátorok
alkalmazásához képest, amelyek bool típust szolgáltattak. Lejjebb látunk majd példákat.

A not a tagadás operátoraként az utána álló kifejezés bool értékének az ellentettjét adja
meg.
Az or az ún. „vagy kapcsolatot” jelenti, az ezzel összekapcsolt részállítások bármelyikének
igaz volta az egész kifejezés igaz voltát eredményezi. Csak ha minden részkifejezés hamis,
akkor lesz az egész is az. (Igaz, ha ez VAGY az igaz.)
Az and az „és kapcsolatot” testesíti meg, amely csak akkor ad eredményül igazat, ha a
kifejezés minden egyes részállítása is igaz, azaz már az egyik hamissága révén az egész
kifejezés hamis lesz. (Csak akkor igaz, ha ez is ÉS az is igaz.)

A „Változók és objektumok” címû fejezetben már volt róla szó, hogy minden objektumnak
van bool értéke:
• A 0 bármilyen formában (pl. 0.0 is) False, minden más szám bool értéke True.
• Egy elemeket tartalmazó konténerobjektum (pl. karakterlánc, lista) értéke True, az
üres konténeré azonban False.
• Egy „közönséges”, azaz nem konténertulajdonságú objektum értéke True.
(Megjegyezzük, hogy ha majd tudunk saját objektumokat készíteni, akkor azt is
meghatározhatjuk, hogy annak mi legyen a bool értéke.)
• A None üres objektum bool értéke False.

A Python-értelmezõ úgy dolgozza fel a logikai kifejezéseket, hogy elkerüli a felesleges
számításokat. Az értelmezõ balról jobbra halad és ha egy or kapcsolatban az elsõ kifejezés
kiértékelése igaz lesz, akkor tudván, hogy a teljes kifejezés is az lesz, már nem szükséges
kiértékelnie a második kifejezést. Az and kapcsolatnál viszont akkor nem érdemes tovább
haladnia, ha az elsõ kifejezés hamis lesz, hiszen akkor a teljes kifejezés is az lesz.
Nézzünk példákat a vagy kapcsolatra:
	>>> "ló" or "teve"
	'ló'
	>>> "" or "teve"
	'teve'
	>>> "" or ""
	''
	>>> not "ló" or 5-2*1.0
	3.0
	>>> bool( not "ló" or 5-2*1.0 )
	True
	>>> 0.0 or not 10
	False
	>>> 0 or None or "" or 2**3-8 or False or not True or "Szia"
	'Szia'

Az elsõ példában az elsõ operandus egy nem üres karakterlánc, aminek a bool értéke True, az
operátor egy vagy kapcsolat, és mivel ezekbõl már következik a teljes állítás igaz volta, az
értelmezõ nem számol tovább. Az eredmény az utoljára kiértékelt kifejezés eredménye lesz, de
nem a bool értéke (amit csak az állítás kiértékeléséhez használtunk). A 'ló' kifejezés pedig
kiértékelve is 'ló'.
A második példában az elsõ operandus egy üres karakterlánc, amelynek értéke hamis, ezért ki
kell értékelni a másik oldalt is, amelynek eredménye a 'teve'.
A harmadik példában mindkét operandus bool értéke hamis és így az egész kifejezés bool
értéke is hamis, de nem ez az eredmény, hanem az utolsónak kiértékelt kifejezés értéke,
ami maga a jobb oldalon szereplõ karakterlánc, és ez most üres.
A negyedik kifejezésben a nem üres karakterlánc bool értéke igaz, a tagadás folytán ez hamis
lesz, ezért a másik oldalon lévõ kifejezést is ki kell értékelni és így 3.0 lesz az eredmény,
egyébként a teljes kifejezés bool értéke True, hiszen egy 0-tól különbözõ szám az eredmény.
Az ötödik állításban a második kifejezés not-tal kezdõdik, ez pedig a mögötte álló kifejezés
bool értékének ellentettjét képezi, tehát a teljes kifejezés kiértékelése most bool értéket
eredményez, nem úgy mint a megelõzõ példákban.

Következzenek a példák az és kapcsolatra:
	>>> "ló" and "teve"
	'teve'
	>>> "" and "teve"
	''
	>>> "" and ""
	''
	>>> not "ló" and 5-2*1.0
	False
	>>> bool( not "ló" and 5-2*1.0 )
	False
	>>> 0.0 and not 10
	0.0
	>>> 0 and None and "" and 2**3-8 and False and not True and "Szia"
	0
	>>> 1 and not None and "lánc" and 8 and True and not False and "Szia"
	'Szia'

Az elsõ példában az elsõ operandus értéke igaz, ezért még „van remény”,
hogy az egész kifejezés igaz lesz, de ehhez meg kell nézni a második operandust is,
így az adja az eredményt.
A második példában az elsõ operandus egy üres karakterlánc, aminek a bool értéke hamis,
és ez szolgál eredményként is, mert már a másik operandus megvizsgálása nélkül is tudható,
hogy az egész kifejezés hamis lesz. A többi kifejezés értelmezését a olvasóra bízzuk.

Természetesen az and, az or és a not operátorok együtt is használhatóak. Azonban, ha túl
sokat teszünk belõlük vegyesen egy kifejezésbe, akkor az igen áttekinthetetlenné válhat,
könnyen elõfordulhat, hogy nem az lesz az eredménye, mint amit várnánk.
A kiértékelés sorrendjénél figyelembe kell venni az operátorok kötési erõsségét is,
a not köt a legerõsebben, gyengébben az and, és a leggyengébben az or (lásd a help('+')-et
interaktív módban). Javasolt inkább több rövidebb kifejezést használni, illetve zárójelekkel
csoportosítani a részkifejezéseket, amivel a kiértékelés sorrendje is megváltoztatható.
Az alábbi elsõ példa elsõ kifejezésében a második True-t és az utolsó False-t az and erõsebben
köti, mint az or az elsõ két True-t, s ezért a kiértékelés úgy történik, ahogy azt a második
kifejezésben a zárójelekkel jeleztük; a harmadik kifejezésben egy másféle zárójelezéssel
módosítottuk a kötéseket és így az eredményt is.
Hasonlóan értelmezhetõk a második példa kifejezései is:
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

Az alábbiakban bemutatjuk az értelmezõ mûködését egy öttagú kifejezésen. Lépésenként jelöltük,
amin az értelmezõ éppen dolgozik: az operandust aláhúzással, az operátort pedig kiemelt
színnel. Az áthúzott operandussal az értelmezõnek nem kell törõdnie, a dõlten szedett értékek
a részeredmények:
False and False and True or False or True
	 False      and True or False or True
			   False     or False or True
					   False      or True
								   True


A fejezet eddigi példáiban a könnyebb érthetõség kedvéért fõleg olyan kifejezéseket
használtunk, ahol az operátor mindkét oldalán csak egy-egy operandus állt, sokszor ezek is
csak a True és False értékek voltak; ezek azonban tetszõlegesen komplikált kifejezések is
lehetnek:
	>>> a,b,c = 1,10,100
	>>> s= "Python"
	>>> a+b+c == 100 or "P" in s and ( b >= len(s) or not b )
	True

A továbbiakban meg szeretnénk említeni néhány érdekesebb kifejezés értelmezését. Az alábbi
példában az elsõ sor négy változónak ugyanazt az értéket adja. A harmadik sorban egy az
összehasonlító operátorok láncolatával megadott kifejezés látható, amelyet a Python úgy
értelmez, amint azt az ötödik sorban megadtuk, s ez teljesen megegyezik a matematikában
megszokottal, de sok más programnyelv ezt másképpen kezeli:
	>>> a = b = c = d = 100
	>>> e = 99
	>>> a == b >= 50 <= e + 1 == c != d+1
	True
	>>> a == b and b >= 50 and 50 <= e + 1 and e + 1 == c and c != d + 1
	True

Az alábbi programocska második sorát szóban felmondva nem a számított False értéket várjuk:
„A b egyenlõ vagy a-val vagy b-vel.”
	>>> a,b = 10,0
	>>> b == (a or b)
	False
Mint tudjuk az or operátor miatt a zárójelen belül a kiértékelés leáll az elsõ operandusnál,
ha annak bool értéke igaz. Itt ez igaz, az eredmény az a lesz, azaz 10, ami nyilván nem
egyenlõ 0 -val.

A fejezetben tárgyalt operátorokkal összefûzött kifejezések mindegyikének volt számított
értéke, vagy az utolsó részkifejezés eredménye vagy egy bool érték, s így nem meglepõ tehát,
hogy ezek értékadó utasításokban is nagyon hasznosak. Mielõtt az ezt bemutató programot
megadnánk, még meg kell említeni egy jól használható értékadó utasítást, az if-else feltételes
szerkezetet:
	obj = kif1 if tesztkif else kif2
Az értelmezõ elõször a tesztkif kifejezést értékeli ki, és ha az igaz, akkor a kif1
kiértékelésének az eredményét írja be az obj nevû változóba, ha hamis akkor a kif2 eredményét.

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