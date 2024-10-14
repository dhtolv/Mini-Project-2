print("--------------------------------")
print("------- Dhita Olivia R.K -------")
print("---------- 2409116040 ----------")
print("-------- Mini Project 2 --------")
print("--------------------------------")

from prettytable import PrettyTable

# Login Sebagai Bendahara dan Pengguna 
users = {
    "bendahara": "bendahara610",
    "pengguna": "user610"
}

# List Kas Yang Harus Dibayar
kas = {
    "Januari": "30000",
    "Februari": "25000",
    "Maret": "35000",
    "April": "30000",
    "Mei": "30000"
}

# Menu Sebagai Bendahara
def menu_bendahara():
    while True:
        print("\n******* Silahkan Pilih Menu Yang Anda Inginkan *******")
        print("1. Menampilkan Data List Kas")
        print("2. Menambah Data List Kas")
        print("3. Menghapus Data Kas Yang Tidak Perlu Dibayar")
        print("4. Mengganti Data Kas Dengan Yang Baru")
        print("5. Keluar Dari Menu")
        print("******************************************************")
        memilih = int(input("Masukkan Menu Yang Sudah Anda Pilih: "))
        while memilih < 1 or memilih > 5:
            print("Menu Yang Anda Pilih Salah! Ulangi Pilihan Anda")
            memilih = int(input("Masukkan Menu Yang Anda Pilih: "))

        if memilih == 1:
            tampilkan_kas()
        elif memilih == 2:
            list_kas_ditambah()
        elif memilih == 3:
            menghapus_kas()
        elif memilih == 4:
            ganti_kas()
        elif memilih == 5:
            print("Keluar Dari Menu.")
            break

def tampilkan_kas():
    table = PrettyTable()
    table.field_names = ["Bulan", "Jumlah Kas"]
    
    for bulan, jumlah_kas in kas.items():
        table.add_row([bulan, jumlah_kas])
    
    print(table)

def list_kas_ditambah():
    tampilkan_kas()
    bulan = input("Masukkan Bulan Yang Diinginkan: ")
    data = input("Masukkan Data Kas Yang Baru: ")  # Menggunakan input string
    kas[bulan] = data
    tampilkan_kas()

def menghapus_kas():
    tampilkan_kas()
    bulan = input("Masukkan Kas Yang Ingin Dihapus: ")
    del kas[bulan]
    tampilkan_kas()

def ganti_kas():
    tampilkan_kas()
    bulan = input("Masukkan Bulan Yang Ingin Diganti: ")
    if bulan in kas:
        baru = input("Masukkan Data Kas Yang Baru: ")
        kas[bulan] = baru
    tampilkan_kas()

# Menu Sebagai Pengguna
def menu_pengguna():
    while True:
        print("\n******* Silahkan Pilih Menu Yang Anda Inginkan *******")
        print("1. Pembayaran")
        print("2. Keluar Dari Menu")
        print("******************************************************")
        memilih = int(input("Masukkan Menu Pembayaran Yang Sudah Anda Pilih: "))
        while memilih < 1 or memilih > 2:
            print("Menu Yang Anda Pilih Salah! Ulangi Pilihan Anda")
            memilih = int(input("Masukkan Menu Yang Anda Pilih: "))

        if memilih == 1:
            print("Silahkan Bayar Sesuai Dengan Kas Yang Dikenakan Kepada Bendahara")
        elif memilih == 2:
            print("Keluar Dari Menu")
            break

# Mencoba Login
def login():
    uname = input("Masukkan Uname Anda: ")
    password = input("Masukkan Password Anda: ")

    if uname in users and users[uname] == password:
        return uname

# Menajalankan Program
def main():
    while True:
        uname = login()
        if uname == "bendahara":
            menu_bendahara()
        elif uname == "pengguna":
            menu_pengguna()

if __name__ == "__main__":
    main()