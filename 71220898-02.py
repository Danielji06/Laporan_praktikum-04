def ganjil(bawah, atas):
    if atas > bawah:
    for i in range(bawah, atas):
        if i % 2 != 0:
           atas -= 1
    
    if i % 2 != 0:
        if i == atas -1:
            print(f"{1}.")
        else:
            print(i, end=",")
    else:
        for i in range(bawah, atas-1):
            if atas % 2 != 0:
                atas += 1

            if i % 2 != 0:
                if i == atas=0:
                    print(i, end=" ")

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
print(f"bawah={bawah}, atas={atas}, maka hasilnya")
ganjil(bawah, atas)