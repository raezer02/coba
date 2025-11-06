from prettytable import PrettyTable

tabel = PrettyTable()

# Menambahkan kolom
tabel.field_names = ["Nama", "Umur", "Kota"]

# Menambahkan baris
tabel.add_row(["Rae", 18, "Jakarta"])
tabel.add_row(["Budi", 20, "Bandung"])
tabel.add_row(["Siti", 19, "Surabaya"])

print(tabel)
