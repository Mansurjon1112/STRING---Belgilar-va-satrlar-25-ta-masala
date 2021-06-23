# -*- coding: utf-8 -*-
"""
String6. Kiritilgan belgining nimaligini aniqlovchi programma tuzilsin. Agar kiritilgan belgi raqam
bo’lsa - “digit”, lotincha harf bo’lsa – “lotin” yozuvhi chiqarilsin. Boshqa xolatlar uchun nol chiqarilsin

@author: Mansurjon Kamolov
"""

belgi = input('Belgi kiriting: ')
if len(belgi)==1:  
    n = ord(belgi)
    if ((n>=64) and (n<=90)) or ((n>=97) and (n<=122)):
        print('lotin')
    elif n>=48 and n<=57:
        print('digit')
    else:
        print('0')
else:
    print('Faqat 1 ta belgi kiriting')
