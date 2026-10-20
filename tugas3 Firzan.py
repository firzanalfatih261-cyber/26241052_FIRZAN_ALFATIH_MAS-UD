# Latihan tugas 3
# Mata kuliah: pemrograman dasar
# Materi: variabel dan input data pengguna

print("=======================================")
print("        IDENTITAS MAHASISWA")
print("=======================================")

#input data      
nama = input("masukan nama anda:")
nim = input("masukan nim anda:")
prodi = input("masukan prodi anda:")
dua_digit_terakhir_nim = input("masukan 2 digit nim anda:")

#hasil program
print("=================================")
print("         HASIL PROGRAM")
print("=================================")

print("nama anda         :", nama)
print("nim anda          :", nim)
print("prodi anda        :", prodi)
print("2 digit nim anda    :", dua_digit_terakhir_nim )

#tipe data
print("tipe data nama:", type(nama))
print("tipe data nim:", type(nim))
print("tipe data prodi:", type(prodi))
print("tipe data 2 digit nim:", type(dua_digit_terakhir_nim))