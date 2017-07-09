A programoz�sban a kor�bban megszerzett ismereteket, p�ld�ul a gyakran elv�gzend�
feladatok unalmas utas�t�ssorozatait vagy az �ppens�ggel nagy matematikai j�rtass�got
megk�vetel� elj�r�sok (algoritmusok) programk�djait az �n. f�ggv�nyk�nyvt�rak t�rolj�k,
melyeket a Pythonban moduloknak nevez�nk. A kedves olvas� is k�pes lesz majd modulok
k�sz�t�s�re, de itt most csak �ttekintj�k a haszn�latuk m�dj�t. A moduloknak mindenekel�tt van
egy nev�k, amelyre hivatkozva �gymond be kell �import�lnunk� �ket a programunkba. A
modulok �nmagukban is objektumnak tekintend�k, amelyekbe tov�bbi objektumok (v�ltoz�k,
f�ggv�nyek) vannak �be�gyazva�. Az import�l�s t�bbf�lek�ppen is t�rt�nhet. Az egyik m�dszert
alkalmazva a programunk �s a modul v�ltoz�i elk�l�n�tve maradnak, ekkor a bels� elemekre a '.'
-tal kell hivatkozni, hasonl�an ahhoz, amint azt az �egyszer�� objektumokn�l (pl. a karakterl�nc
eset�ben az upper() met�dusn�l) l�ttuk. A m�sik m�dszer szerint a programunk �s a modul
v�ltoz�i ��sszef�s�l�dnek�, s �gy a modul elemei ugyan�gy haszn�lhat�k, mintha a saj�t
programunkban lettek volna defini�lva. Az ut�bbi elj�r�st nem aj�nlott k�vetni, ha a modulban �s
a programunkban azonos nev� objektumok l�teznek.

Az al�bbi keretekben a math matematikai modul import�l�s�ra l�tunk p�ld�kat. A math
t�pusa �module� objektum. A k�z�ps� keretben a bels� objektumokra a math. el�taggal
hivatkozunk, a math.pi �rt�k�t egy saj�t v�ltoz�ba is be�rjuk. A jobb oldali keretben az �import *�
utas�t�ssal minden bels� objektumot �beleolvasztunk� a programk�dunkba, �gy nincs sz�ks�g az
el�tagra, de ez kevered�st okozhat, mint azt a pi v�ltoz�n�l l�tjuk, amint �j �rt�ket kap.
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

A modulb�l elegend� csak azokat az objektumokat import�lni, amelyekre sz�ks�g�nk lesz. A fenti
bal oldali keretben a pi-t import�ltuk, de az sqrt()-t nem. A jobb oldali keretben az import hat�sa
megegyezik a legels� k�t p�ld�ban adottal, de itt a math modult a tov�bbiakban a r�videbb mm
n�ven fogjuk tudni haszn�lni.
Az al�bbiakban csak egyes objektumokat import�lunk �s mindegyiknek �j nevet adunk,
amelyek ezut�n a modulbeli bels� nev�k�n nem lesznek el�rhet�k (l�sd a pi -re adott hib�t):
	>>> from math import pi as Pi, e as Ex, sqrt as sq
	>>> Pi, Ex, sq(4)
	(3.141592653589793, 2.718281828459045, 2.0)
	>>> pi
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'pi' is not defined
	>>>

