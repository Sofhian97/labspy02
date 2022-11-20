a = (int(input("Masukkan bilangan pertama : ")))
b = (int(input("Masukkan bilangan kedua : ")))
c = (int(input("Masukkan bilangan ketiga : ")))
if a > b and a > c :
    print("Bilangan pertama lebih besar dari bilangan kedua dan ketiga")
elif b > a and b > c :
    print("Bilangan kedua lebih besar dari bilangan pertama dan ketiga")
elif c > a and c > b :
    print("Bilangan ketiga lebih besar dari bilangan pertama dan kedua")