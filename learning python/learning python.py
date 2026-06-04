# Ini adalah contoh program sederhana (teks dengan tanda pagar adalah komentar. 
# tidak dibaca oleh komputer)
#Aturan Penamaan Variabel di Python:
#Hanya boleh berisi huruf, angka, dan underscore (_).
#Tidak boleh diawali dengan angka (contoh: 1koin itu salah, koin1 itu benar).
#Tidak boleh ada spasi (gunakan underscore sebagai pemisah, misalnya harga_koin).
#Membedakan huruf besar dan kecil (case-sensitive). Umur dan umur dianggap sebagai 
# dua kotak yang berbeda.
#tipe data dasar
aset = "Solana"             # Tipe data String
jumlah_koin = 10            # Tipe data Integer
harga_beli = 145.75         # Tipe data Float
sedang_ditahan = True       # Tipe data Boolean

# Menampilkan isi variabel ke layar
print("Nama Aset:", aset)
print("Jumlah:", jumlah_koin)
print("Harga Masuk:", harga_beli)
print("Masih Dipegang?", sedang_ditahan)
#Kalau kamu bingung suatu variabel itu tipe datanya apa, Python punya alat bernama type().
# Contoh: print(type(aset)) nanti akan memunculkan tulisan <class 'str'> yang artinya String.