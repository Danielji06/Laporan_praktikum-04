jumlah_matakuliah = int(input("masukkan jumlah mata kuliah: "))

total_bobot = 0
total_sks = jumlah_matakuliah * 3

for i in range(jumlah_matakuliah):
    nilai = input(f"masukkan nilai mata kuliah ke(i+1) (A/B/C/D):")
    if nilai == "A":
        bobot = 4
    elif nilai == "B":
        bobot = 3
    elif nilai == "C":
        bobot = 2
    elif nilai == "D":
        bobot = 1
    else:
        print("Nilai yang dimasukkan tidak valid")
        bobot = 0

    total_bobot += bobot * 3

    ips = total_bobot / total_sks 

print(f"IPS anda adalah {ips:2f}")