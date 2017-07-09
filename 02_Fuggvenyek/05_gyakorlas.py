# -*- coding:utf-8 -*-

# Utiköltség számítás
# Vác - Ózd


def koltseg(tavolsag, benzinar):
    print(tavolsag/100*6.5*benzinar)
    return
koltseg(168, 378.9)


# Megtakarítási számítás
def megtakaritas(osszeg, idotartam, kamatlab):
    ado_sz = 22
    k = osszeg/100*kamatlab/12*idotartam
    a = k/100*ado_sz
    print(k-a)
    return
megtakaritas(100000, 5, 3.5)


# Hőmérséklet átváltó
def fc(f):
    print((f-32)*5/9)
    return


def cf(c):
    print(c*9/5 + 32)
    return


fc(55)
cf(10)
