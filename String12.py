# -*- coding: utf-8 -*-
"""
String12. Satr va N natural soni berilgan. Shu satr belgilari orasiga N tadan ‘*’ belgisi qo’yilgan satr
hosil qiluvchi va ekranga chiqaruvchi programma tuzilsin.

Created on Wed Jun 23 12:15:56 2021

@author: Mansurjon Kamolov
"""

satr = input('satrni kiriting: ')
n=int(input('Son kiriting: '))
m='*'*n
for i in satr:
    if i==satr[-1]:
        print(i,end='')
    else:
        print(i,end=m)