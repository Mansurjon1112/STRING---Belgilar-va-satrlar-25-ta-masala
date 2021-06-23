# -*- coding: utf-8 -*-
"""
String3. Kodlar jadvalida kiritilgan belgidan oldin va keyin turuvchi belgilarni chiqaruvchi programma
tuzilsin.

@author: Mansurjon Kamolov
"""

belgi = input('Belgi kiriting: ')

if len(belgi)==1:
    print(ord(belgi))
else:
    print('Faqat 1 ta belgi kiriting')
