# -*- coding: utf-8 -*-
"""
String14. Satr berilgan. Satrdagi katta lotin harflari sonini aniqlovchi programma tuzilsin

Created on Wed Jun 23 12:36:36 2021

@author: Mansurjon Kamolov
"""

satr = input('satrni kiriting: ')
sanoq=0
for i in satr:
    if i>='A' and i<='Z':
        sanoq +=1 

if sanoq>0:
    print('Katta lotin harfi bor, ularning soni', sanoq,'ta')
else:
    print('Katta lotin harfi mavjud emas')

        
    