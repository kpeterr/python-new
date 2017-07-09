# -*- coding:utf-8 -*-

# Az alábbi kis programban megmutatjuk mi módon lehet a struktúra
# elemeihez hozzáférni:

import time as tt

ts = tt.localtime()
év = ts.tm_year
hónap = ts.tm_mon
nap = ts.tm_mday

print(" év :", év)
print(" hó :", hónap)
print(" nap:", nap)

input("A befejezéshez nyomja meg az Enter-t!")
