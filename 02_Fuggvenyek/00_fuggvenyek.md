--------------------------------------------------------
-------------------- FÜGGVÉNYEK I. ---------------------
--------------------------------------------------------


Programok írása közben a legtöbbször azzal szembesülünk, hogy utasítások egymás
után következõ csoportját több helyre is be kellene írni, s ez egyrészt fárasztó, másrészt
megnöveli a programfájl méretét, harmadrészt a sok ismétlés áttekinthetetlenné teszi a
programot. Erre találták ki a programozásban használt függvény fogalmát, aminek segítségével a
gyakran ismételt utasítások sorozatát egy külön egységbe szervezik, ezt csak egyszer írják le,
nevet adnak neki, és ezzel a névvel a program bármelyik részérõl röviden hivatkozhatnak rá. A
függvény „nevesítését” a definiálásának nevezzük, a függvényre történõ hivatkozást pedig a
függvény meghívásának. Meghívás esetén elõször megtörténik a függvényben leírt utasítások
végrehajtása, majd a program ott folytatódik, ahonnan a függvényt meghívták, és a meghívó
utasítás helyébe a függvény utasításai által eredményezett érték kerül. Talán nem meglepõ, hogy
egy függvény belsejében az utasítások más függvényeket is meghívhatnak. Sõt egy függvény saját
magát is meghívhatja (ún. rekurzív függvény), ami nagyon hatékony módszer bizonyos esetekben,
de ekkor nagyon körültekintõen kell eljárni, mert esetleg a program soha nem jön ki a
függvénybõl, azaz végtelen ciklusba kerül.

A programozásban a függvényeket más nevekkel is szokták illetni, mint például eljárás,
metódus, rutin, szubrutin. Egyes programnyelvekben egyik-másik kifejezést arra használják, hogy
bizonyos tulajdonságú függvényeket megkülönböztessenek a többitõl: például az eljárás jelölheti
azt a függvénytípust, amelyiknek nincs visszatérési értéke (errõl lesz szó a késõbbiekben). A
metódus általában azoknak a függvényeknek a megnevezése, amelyek nem „önállóan”, hanem
valamilyen objektumhoz kapcsoltan lettek definiálva (errõl is lesz még szó).

A sok beszéd után ismerkedjünk meg néhány alapfüggvénnyel:
        >>> abs(9)
        9
        >>> abs(-9.1)
        9.1
        >>> a= -100
        >>> abs( 34+1/2*a)
        16.0
        >>> b= abs(a*5)
        >>> b
        500
        >>>
Az elsõ az abszolútérték-függvény, amelyet a matematika óráról ismerünk, csak ott nem így
jelöltük, itt a függvény neve abs. Amely számnak az abszolút értékére kíváncsiak vagyunk, azt a
név után zárójelben kell megadnunk. Azt mondjuk, hogy az abs() függvény egyetlen
argumentumot vár bemeneti értékként, és egyetlen visszatérési értéke van, most éppenséggel a
bemenet abszolút értéke. Az utóbbit egy változóban eltárolhatjuk, s ezt a b=abs(a*5) utasításban
meg is tettük. A példákon láthatjuk, hogy az argumentum nem csak egy konkrét szám lehet,
hanem változókat is tartalmazó kifejezés is, de ennek kiértékelése egyetlen számot kell hogy
eredményezzen.

        >>> a,b,c= -10, -1, 25
        >>> min( c,a,b, -3.14, 2)
        -10
        >>> mini= min( c,a,b, -3.14, 2)
        >>> mini
        -10
        >>> maxi= max( c,a,b, -3.14, 2)
        >>> maxi
        25
        >>> max( maxi, 100, c*a-b )
        100
        >>>
A következõ megismerendõk a min() és max() függvénypár, amelyeket több
argumentummal is meghívhatunk, és elnevezésüknek megfelelõen ezek közül a legkisebbet ill. a
legnagyobbat adják meg visszatérési értékként. Figyeljük meg, hogy a bemeneti értékeket
vesszõvel kell elválasztani, és ezért is kell a tizedes törtek írásánál pontot használnunk a
tizedesvesszõ helyett:
        >>> min( -3,14, 5 )
        -3
        >>> min( -3.14, 5 )
        -3.14
        >>>
        
        >>> round( 2.7)
        3
        >>> round( -2.7)
        -3
        >>>
        >>> 4/3
        1.3333333333333333
        >>> round( 4/3,3)
        1.333
        >>> round( -4/3,3)
        -1.333
        >>> round( -1.6789, 2)
        -1.68
        >>>
A számok kerekítésére használt round() függvény alkalmazható egy ill. két bemeneti értékkel
is. Az elsõ esetben a beírt számnak az egészre kerekített értéket adja vissza. A két
argumentummal történõ hívásnál a második bemeneti érték azt mondja meg, hogy az elsõnek
megadott szám hány tizedesjegyre legyen kerekítve. Az argumentumok sorrendje fontos!

Most tekintsük a type() és print() függvényeket, amelyeknek már tényleg nincs közük a
matematikához! A type() a bemenetként kapott érték típusát adja vissza, a példában a float a
tizedespontot is tartalmazó adatra vonatkozik, az int pedig az egész számra:
        >>> a= 1.37
        >>> type(a)
        <class 'float'>
        >>> type( 2.7)
        <class 'float'>
        >>> type(1.0)
        <class 'float'>
        >>> b= 137
        >>> type(b)
        <class 'int'>
        >>>
        
        >>> x,y,z = 5, 3, 9
        >>> print( x,y,z)
        5 3 9
        >>> print( min(x,y,z), max(x,y,z), x+y+z+100 )
        3 9 117
        >>> print( type(x) )
        <class 'int'>
        >>> print( 2015)
        2015
        >>>

A print() függvény az argumentumként beadott értékeket jeleníti meg a képernyõn. Ez az
interaktív mód ismeretében feleslegesnek tûnik, de egy programfájlt indítva a változók értéke már
nem fog automatikusan kiíródni, mégpedig azért nem, hogy a programozó teljesen ellenõrzése
alatt tarthassa a megjelenítést: az értelmezõt a print() függvénnyel közvetlenül kell a
megjelenítésre utasítani. A függvény változó számú bemeneti értéket kaphat. Figyeljük meg,
hogy van olyan hívása, amelyben valamely argumentum maga is függvényt hív: a min(), a max()
és a type() rutinokat.