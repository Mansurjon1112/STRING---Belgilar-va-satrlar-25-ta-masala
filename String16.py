# -*- coding: utf-8 -*-
"""
String16. Satr berilgan. Satrdagi xamma katta lotin harflari kichigiga almashtiruvchi programma
tuzilsin.

Created on Wed Jun 23 19:41:07 2021

@author: Mansurjon Kamolov
"""

satr = input('satrni kiriting: ')
yangi=''
for i in satr:
    if (i>='A')and(i<='Z'):
        yangi=yangi+i.lower()
    else:
        yangi=yangi+i
print(yangi)
