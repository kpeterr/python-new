Alap oper�torok:
+ �sszead�s
- kivon�s
* szorz�s
/ oszt�s
** hatv�nyoz�s

**          a leger�sebben k�t
+ �s -      ha el�jelk�nt �llnak (egyform�n er�sek),
            pl.: -2**4=-16 lesz, de (-2)**4 =16
* �s /      (egyform�n er�sek)
+ �s -      ha k�t operandust k�tnek �ssze (egyform�n er�sek)

----------------------------------------------------
Feladat:
Budapestr�l Amszterdamba szeretn�nk aut�val utazni,
�s k�v�ncsiak vagyunk az �tik�lts�gre:
a t�vols�g 1395 km, az aut�nk fogyaszt�sa
7 liter 100 km-en, �s 1 liter benzin �ra 327.9 Ft

Megold�s:
1395/100*7*327.9    # 32019 Ft

V�c-�zd t�vols�gban az utik�lts�g:
168/100*6.5*383.6   # 4200 Ft
----------------------------------------------------


----------------------------------------------------
Feladat:
A k�vetkez� kalkul�ci�ban meghat�rozzuk 100 000 forint kamat�t, amelyet megtakar�t�sk�nt
f�lre szeretn�nk tenni. Az �sszeget (az � nev� v�ltoz�ban t�roljuk) 5 h�napra (h�) szeretn�nk
lek�tni a bankban, az �ves kamatl�b 3.5% (�kl_sz), �s a nyert kamat ut�n 22% (ad�_sz) ad�t kell
fizetn�nk. A k v�ltoz�ba tett�k az 5 h�nap ut�n j�r� kamatot. El�sz�r kisz�m�tottuk az �sszegnek
az �ves kamatl�b szerinti sz�zal�k�t (�/100*�kl_sz), de ez az eg�sz �vre j�r� kamatot jelenti, azaz
ezt az �rt�ket el kell osztani 12-vel, �gy megkapva az 1 h�napra jut� kamatot, majd ezt
megszorozva 5-tel, a k�v�nt megtakar�t�si id�vel. Teh�t 5 h�napra a kamat kerek�tve 1458.3 Ft. A
kamat ad�j�t az a v�ltoz�ban t�roljuk, ami kerek�tve 320.8 Ft-ot tesz ki, azaz a �hazavihet��
nyeres�g 1137.5 Ft-nak ad�dik (term�szetesen az eredeti �sszeget, a t�k�t is visszakapjuk).

Megold�s:
>>> �= 100000
>>> h�= 5
>>> �kl_sz= 3.5
>>> ad�_sz= 22
>>> k= �/100*�kl_sz/12*h�
>>> k
1458.3333333333335
>>> a= k/100*ad�_sz
>>> a
320.83333333333337
>>> k-a
1137.5
>>>

A k�vetkez� p�ld�ban ugyanezt a feladatot oldjuk meg bemutatva, hogy az el�bbi program nem
az egyetlen, amivel a helyes �rt�keket el��ll�thatjuk. Minden fejleszt�n�l kialakul majd egy r�
jellemz� programoz�si st�lus, ami az id�k folyam�n �ltal�ban v�ltozik is (rem�lhet�leg
t�k�letesedik).

>>> �= 10**5
>>> h�= 5
>>> �sz= 3.5/100
>>> asz= 22/100
>>> k= �*�sz/12*h�
>>> k - k*asz
1137.5
>>>

