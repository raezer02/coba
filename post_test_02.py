print("=" * 80)
print("TOKO BAHAN BANGUNAN".center(50))
print("=" * 80)

nama = input("masukan nama pelanggan: ")
print("-" * 80)

print("barang | harga satuan   | jumlah")
print("-" * 80)

bata: int = 100
semen: int = 100000
total: float

print(f"bata   | Rp{bata}          |", end=" ")
jum_bata = int(input(""))

print(f"semen  | Rp{semen:,}      |".replace(",", "."), end=" ")
jum_semen = int(input(""))

print("-" * 80)

total = (bata * jum_bata) + (semen * jum_semen)

if jum_bata >= 2000 and jum_semen >= 16:
    diskon = 0.30
    diskon_check = True
elif jum_bata >= 500 and jum_semen >= 5:
    diskon = 0.15
    diskon_check = True
else:
    diskon = 0.0
    diskon_check = False

jum_diskon = total * diskon
total_setelah = total * (1 - diskon)

if diskon_check:
    print("harga sebelum diskon: Rp {:,.0f}".format(total).replace(",", "."))
    
    if diskon == 0.30:
        print(f"dapat diskon gacor {int(diskon * 100)}%")
    elif diskon == 0.15:
        print(f"dapat diskon sheees {int(diskon * 100)}%")
    
    print("jumlah diskon Rp {:,.0f}".format(jum_diskon).replace(",", "."))
else:
    print("Tidak dapat diskon")

print("-" * 80)
print("harga akhir:  Rp {:,.0f}".format(total_setelah).replace(",", "."))
print("=" * 80)