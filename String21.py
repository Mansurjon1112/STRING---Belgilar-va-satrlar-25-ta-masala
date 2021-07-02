# -*- coding: utf-8 -*-
"""
String21.  Butun  musbat  sonni  ifodalovchi  satr  berilgan.  Uning  belgilarini  (raqamlarini)  
ongdan
chapga qarab chiqaruvchi programma tuzilsin.


Created on Wed Jun 23 20:19:59 2021

@author: Mansurjon Kamolov
"""
satr = input('Musbat son kiriting: ')
for i in satr[::-1]:
    print(i, end = '')

"""
satr = input('Musbat son kiriting: ')
yangi=''
index=0
for i in satr[0:-1]:
    index +=1
    yangi += satr[index]
    
yangi += satr[0]
print(yangi)
"""
