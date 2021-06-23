# -*- coding: utf-8 -*-
"""
String8. N natural soni va belgi berilgan. N ta kiritilgan belgidan iborat satr hosil qiling va ekranga
chiqaring. Masalan: N = 5; Belgi = ‘A’; Natija = AAAAA

Created on Wed Jun 23 10:27:30 2021

@author: User
"""

n=int(input('Son kiriting: '))
Belgi = input('Belgini kiriting: ')
if len(Belgi) ==1:
    Natija = Belgi*n
else:
    Natija = "1 ta belgi kiriting"

print(Natija)