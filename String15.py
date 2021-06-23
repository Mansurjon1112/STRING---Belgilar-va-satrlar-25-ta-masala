# -*- coding: utf-8 -*-
"""
String15. Satr berilgan. Satrdagi kichik lotin va kirill harflarining umumiy sonini aniqlovchi
programma tuzilsin.

Created on Wed Jun 23 19:20:17 2021

@author: Mansurjon Kamolov
"""

satr = input('satrni kiriting: ')
lot=0
kri=0
for i in satr:
    if i>='a' and i<='z':
        lot +=1 
    elif i>='а' and i<='я':
        kri +=1

if (lot==0) and (kri == 0):
    print('Kichik lotin ham, kichik kiril harflari ham yo\'q')
else :
    print('Kichik lotin harfi bor, ularning soni', lot,'ta')
    print('Kichik kirill harfi bor, ularning soni', kri,'ta')

        