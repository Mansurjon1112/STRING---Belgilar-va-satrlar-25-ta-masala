# -*- coding: utf-8 -*-
"""
String5. n butun soni berilgan (1 <= n <= 26). Lotin alfavitidagi n ta kichik harflarni teskari tartibda
chiqaruvchi programma tuzilsin. Ya’ni z da a gacha chiqarilsin.

@author: Mansurjon Kamolov
"""

n = int(input('n= '))
#1-usul
for i in range(1,n+1):
    print(chr(123-i))

#2-usul
s=''
for i in range(ord('z'), ord('a')-1,-1):
    s+=chr(i)
print(s[:n])
