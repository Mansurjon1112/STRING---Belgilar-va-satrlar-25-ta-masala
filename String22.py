# -*- coding: utf-8 -*-
"""
String22. Butun musbat sonni ifodalovchi satr berilgan. Shu son raqamlari yig’indisini chiqaruvchi
programma tuzilsin.

Created on Wed Jun 23 20:24:51 2021

@author: Mansurjon Kamolov
"""

son = int(input("Butun son kiriting "))

summa = 0
while (son != 0):
    summa = summa + son % 10
    son = son // 10
print("Raqamlari yig'indisi: ", summa)