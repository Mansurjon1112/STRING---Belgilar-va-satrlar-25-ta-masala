# -*- coding: utf-8 -*-
"""
String20. Butun musbat sonni ifodalovchi satr berilgan. Uning belgilarini (raqamlarini) chapdan
o’ngga qarab chiqaruvchi programma tuzilsin.

Created on Wed Jun 23 20:08:20 2021

@author: Mansurjon Kamolov
"""

satr = input('Musbat son kiriting: ')
yangi=satr[-1]
index=0
for i in satr[0:-1]:
    yangi += satr[index]
    index +=1
print(yangi)