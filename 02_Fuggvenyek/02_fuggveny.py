# -*- coding:utf-8 -*-

# Itt az ideje, hogy elkészítsük a saját rutinjainkat is:
"""
    >>> def lini(x):
    ... y= 3*x + 1
    ... return y
    ...
    >>> lini(1)
    4
    >>> lini(2)
    7
    >>> lini(10)
    31
    >>> lini(1.5)
    5.5
    >>>
"""


# Az első függvényünk
def lini(x):
    y = 3 * x + 1  # Ez egy lineáris függvény
    return y

print(lini(1))
print(lini(2))
# print(lini(10))
print(lini(1.5))

input("A befejezéshez nyomja meg az Enter-t!")


"""
Először még interaktív módban mutatjuk meg a függvény definiálását, ami a sor
elején a def kulcsszóval kezdődik, és ezt szóközzel elválasztva a függvény neve
követi. A név után zárójelben egy x nevű változó áll, amit másképpen is
hívhatnánk, de most szándékosan egy matematikai függvényt szeretnénk utánozni.
Lehet, hogy a figyelmes olvasó most felszisszen, hiszen azt tanultuk, hogy egy
változóra csak akkor lehet hivatkozni, ha korábban már értékadással
létrehoztuk, de akkor mi helyzet itt az x-szel? A függvény definícióját, hiába
szerepel akár a program első sorában, a Python-értelmező még nem fogja
végrehajtani. A függvény végrehajtására csak akkor kerül sor, ha a programból
valahol meghívjuk, és ha nem hívjuk meg, akkor lesz a programban egy nem
használt definíciónk. Az x-et a függvény definíciójában paraméternek nevezzük,
és a függvény meghívásakor a Python-értelmező a hívásban szereplő konkrét
értéket, az argumentumot adja át az x-nek. Így például a lini(1) kifejezésben
az x paraméter az 1-et kapja meg argumentumként. E függvénnyel szeretnénk egy
értéket is visszaadatni, amit a return utasítás után leírva kell megadni;
most az y változót adtuk meg, azaz a függvényhívás helyébe majd ennek az
értéke fog bekerülni. A függvény végrehajtása itt a return utasítással be is
fejeződik. Még jegyezzük meg, hogy a definíció első sora egy kettősponttal
zárul, amiből az értelmező tudja, hogy egy új utasításblokk fog következni.
Az utasításblokk beírásakor a „>>>” jelsorozat a figyelem felkeltése céljából
három pontra változik, jelezve, hogy a következő sorokat beljebb, azaz
behúzással kell kezdeni. A blokkban egy-egy szóközzel kezdtük beljebb az
utasításokat. A blokk utolsó sorának beírása után, az Enter-t lenyomva
megkapjuk az újabb „...” jelsorozatot, itt rögtön ismét Enter-t nyomva az
értelmező a blokk írását befejezettnek tekintve a következő sorban már újra
a „>>>” jelsorozatot adja.

Ezután a programfájlként írt példában a blokk minden sorát egy tabulátor
pozícióval beljebb kezdtük. A fájl első két soráról, ami kettős kereszttel
(angolul: hash mark) kezdődik, már volt szó az „Egy Python program futtatása”
című fejezetben. Itt további '#' jeleket helyeztünk el, amelyek után példaként
magyarázó-emlékeztető szövegeket írtunk be, amelyek segíthetik a program
megértését. Az értelmező a '#' jeltől kezdve az adott sor végéig átugorja az
ott leírtakat, meg sem próbálva azokat végrehajtani. Ugyancsak beszúrtunk egy
'#' jelet az egyik print()-tel kezdődő sor elejére és így az sem fog
végrehajtódni, e művelet elnevezése az utasítás „kommentbe tevése”.
Hibakeresésnél bevett gyakorlat, hogy egyes gyanús sorokat a programozó
kicserélne egy másikra, de kitörölni a régit nem akarja, mert hátha mégis az
lesz a jó, ezért a régi sort csak „kommentbe teszi”, s mellé írja az újat.
"""
