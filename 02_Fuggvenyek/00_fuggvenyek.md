--------------------------------------------------------
-------------------- F�GGV�NYEK I. ---------------------
--------------------------------------------------------


Programok �r�sa k�zben a legt�bbsz�r azzal szembes�l�nk, hogy utas�t�sok egym�s
ut�n k�vetkez� csoportj�t t�bb helyre is be kellene �rni, s ez egyr�szt f�raszt�, m�sr�szt
megn�veli a programf�jl m�ret�t, harmadr�szt a sok ism�tl�s �ttekinthetetlenn� teszi a
programot. Erre tal�lt�k ki a programoz�sban haszn�lt f�ggv�ny fogalm�t, aminek seg�ts�g�vel a
gyakran ism�telt utas�t�sok sorozat�t egy k�l�n egys�gbe szervezik, ezt csak egyszer �rj�k le,
nevet adnak neki, �s ezzel a n�vvel a program b�rmelyik r�sz�r�l r�viden hivatkozhatnak r�. A
f�ggv�ny �neves�t�s�t� a defini�l�s�nak nevezz�k, a f�ggv�nyre t�rt�n� hivatkoz�st pedig a
f�ggv�ny megh�v�s�nak. Megh�v�s eset�n el�sz�r megt�rt�nik a f�ggv�nyben le�rt utas�t�sok
v�grehajt�sa, majd a program ott folytat�dik, ahonnan a f�ggv�nyt megh�vt�k, �s a megh�v�
utas�t�s hely�be a f�ggv�ny utas�t�sai �ltal eredm�nyezett �rt�k ker�l. Tal�n nem meglep�, hogy
egy f�ggv�ny belsej�ben az utas�t�sok m�s f�ggv�nyeket is megh�vhatnak. S�t egy f�ggv�ny saj�t
mag�t is megh�vhatja (�n. rekurz�v f�ggv�ny), ami nagyon hat�kony m�dszer bizonyos esetekben,
de ekkor nagyon k�r�ltekint�en kell elj�rni, mert esetleg a program soha nem j�n ki a
f�ggv�nyb�l, azaz v�gtelen ciklusba ker�l.

A programoz�sban a f�ggv�nyeket m�s nevekkel is szokt�k illetni, mint p�ld�ul elj�r�s,
met�dus, rutin, szubrutin. Egyes programnyelvekben egyik-m�sik kifejez�st arra haszn�lj�k, hogy
bizonyos tulajdons�g� f�ggv�nyeket megk�l�nb�ztessenek a t�bbit�l: p�ld�ul az elj�r�s jel�lheti
azt a f�ggv�nyt�pust, amelyiknek nincs visszat�r�si �rt�ke (err�l lesz sz� a k�s�bbiekben). A
met�dus �ltal�ban azoknak a f�ggv�nyeknek a megnevez�se, amelyek nem ��n�ll�an�, hanem
valamilyen objektumhoz kapcsoltan lettek defini�lva (err�l is lesz m�g sz�).

A sok besz�d ut�n ismerkedj�nk meg n�h�ny alapf�ggv�nnyel:
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
Az els� az abszol�t�rt�k-f�ggv�ny, amelyet a matematika �r�r�l ismer�nk, csak ott nem �gy
jel�lt�k, itt a f�ggv�ny neve abs. Amely sz�mnak az abszol�t �rt�k�re k�v�ncsiak vagyunk, azt a
n�v ut�n z�r�jelben kell megadnunk. Azt mondjuk, hogy az abs() f�ggv�ny egyetlen
argumentumot v�r bemeneti �rt�kk�nt, �s egyetlen visszat�r�si �rt�ke van, most �ppens�ggel a
bemenet abszol�t �rt�ke. Az ut�bbit egy v�ltoz�ban elt�rolhatjuk, s ezt a b=abs(a*5) utas�t�sban
meg is tett�k. A p�ld�kon l�thatjuk, hogy az argumentum nem csak egy konkr�t sz�m lehet,
hanem v�ltoz�kat is tartalmaz� kifejez�s is, de ennek ki�rt�kel�se egyetlen sz�mot kell hogy
eredm�nyezzen.

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
A k�vetkez� megismerend�k a min() �s max() f�ggv�nyp�r, amelyeket t�bb
argumentummal is megh�vhatunk, �s elnevez�s�knek megfelel�en ezek k�z�l a legkisebbet ill. a
legnagyobbat adj�k meg visszat�r�si �rt�kk�nt. Figyelj�k meg, hogy a bemeneti �rt�keket
vessz�vel kell elv�lasztani, �s ez�rt is kell a tizedes t�rtek �r�s�n�l pontot haszn�lnunk a
tizedesvessz� helyett:
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
A sz�mok kerek�t�s�re haszn�lt round() f�ggv�ny alkalmazhat� egy ill. k�t bemeneti �rt�kkel
is. Az els� esetben a be�rt sz�mnak az eg�szre kerek�tett �rt�ket adja vissza. A k�t
argumentummal t�rt�n� h�v�sn�l a m�sodik bemeneti �rt�k azt mondja meg, hogy az els�nek
megadott sz�m h�ny tizedesjegyre legyen kerek�tve. Az argumentumok sorrendje fontos!

Most tekints�k a type() �s print() f�ggv�nyeket, amelyeknek m�r t�nyleg nincs k�z�k a
matematik�hoz! A type() a bemenetk�nt kapott �rt�k t�pus�t adja vissza, a p�ld�ban a float a
tizedespontot is tartalmaz� adatra vonatkozik, az int pedig az eg�sz sz�mra:
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

A print() f�ggv�ny az argumentumk�nt beadott �rt�keket jelen�ti meg a k�perny�n. Ez az
interakt�v m�d ismeret�ben feleslegesnek t�nik, de egy programf�jlt ind�tva a v�ltoz�k �rt�ke m�r
nem fog automatikusan ki�r�dni, m�gpedig az�rt nem, hogy a programoz� teljesen ellen�rz�se
alatt tarthassa a megjelen�t�st: az �rtelmez�t a print() f�ggv�nnyel k�zvetlen�l kell a
megjelen�t�sre utas�tani. A f�ggv�ny v�ltoz� sz�m� bemeneti �rt�ket kaphat. Figyelj�k meg,
hogy van olyan h�v�sa, amelyben valamely argumentum maga is f�ggv�nyt h�v: a min(), a max()
�s a type() rutinokat.