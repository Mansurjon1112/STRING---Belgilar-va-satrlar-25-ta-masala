# -*- coding: utf-8 -*-
"""
String4. n butun soni berilgan (1 <= n <= 26). Lotin alfavitidagi dastlabki n ta katta harflarni
chiqaruvchi programma tuzilsin.

@author: Mansurjon Kamolov
"""

n = int(input('n= '))
for i in range(1,n+1):
  print(chr(i+64))
