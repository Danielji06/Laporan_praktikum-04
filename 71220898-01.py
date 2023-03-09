def perkalian(a, b):
    hasil = 0 
    for i in range(b):
        hasil += a
    return hasil

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
print(f"{a} x {b} = {perkalian(a, b)}")