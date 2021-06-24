a = input('Ikkilik sanoq sistemasidagi son kiriting: ')
unlik=0
daraja = 1
d=a;
#birinchi usul
while int(a)!=0:
    b=int(a)%10
    b=b*(daraja)
    unlik = unlik + b
    daraja*=2
    a=int(a)//10
print(unlik)

#ikkinchi usul
un = 0
for i in str(d):
    un = un * 2 + int(i)
    
print(un)
