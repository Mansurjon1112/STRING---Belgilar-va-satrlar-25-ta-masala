#String2. n butun soni berilgan (32 < n <= 126). Kodi n ga teng bo’lgan belgini chiqaruvchi
#programma tuzilsin.

n=int(input('N='))

if (n>32) and (n<=126):
	print(chr(n))
else:
	print('Masala shartiga mos son kiriting. 32<n<=126')