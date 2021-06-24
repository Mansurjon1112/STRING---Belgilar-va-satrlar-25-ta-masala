unlik = input("O'nlik sanoq sistemasidagi sonni kiriting: ")
ikki = ''
qol = 0
while unlik!=0:
    qol = int(unlik) % 2
    unlik = int(unlik) // 2
    ikki += str(qol)
print(ikki[::-1])


