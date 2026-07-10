import hashlib
from logger import fungsiLog
import json
from parser import parserLog

rekap_salah = {}
#__________
#| FUNGSI |
def enkripsi(password):
    password_to_encrypt = password.encode('utf-8')
    return hashlib.sha256(password_to_encrypt).hexdigest()

def data_json_masuk (database):
    with open ("data_users.json", "w") as file:
        return json.dump(database, file, indent = 4)

def data_json_keluar ():
    with open ("data_users.json", "r") as file:
        return json.load(file)


def daftar(database):
    while True:
        username = input("Masukkan Username unik: ").strip()
        if not username:
            print("(!) Username tidak boleh kosong")
            continue
        elif username in database:
            print("(!) Pengguna Sudah Terdaftar")
            continue
        password = input("Masukkan Password: ")
        encrypted = enkripsi(password) #meng-enkripsi password dengan fungsi
        print("\n(!) Register Berhasil!")
        
        fungsiLog(username, ngapain = "Register Berhasil")

        status = "aktif"
        salah = 0
        database[username] = {'password' : encrypted,
                               'status' : status,
                               'salah_input' : salah}
        data_json_masuk (database)
        print("\n(!) Register Berhasil!")
        return 



def login(database):
    while True:
        username = input("Masukkan Username: ")
        if username not in database:
            print("\n(!) Pengguna Tidak Ditemukan\n")
            
            q = input("Kembali ke Menu Utama? y/n  ")
            if q == "Y" or q == "y":
                return
            elif q == "N" or q == "n":
                continue
            else:
                print("Tidak Valid!")
                continue
        elif database[username]['status'] == "NONAKTIF":
            print("(!) Anda Sudah Gagal Log in Lebih dari Tiga Kali, Akun di Nonaktifkan Sementara\n")
            print("==> Silakan Hubungi Admin Untuk Memulihkan Akun\n")
            return

        password = input("Masukkan Password: ")
        print("\n")
        encrypted = enkripsi(password)

        if encrypted != database[username]['password']:
            fungsiLog(username, ngapain = "Salah Password")
            parserLog(rekap_salah)
            database[username]['salah_input'] += 1
            print("(!) Password Salah!\n")

            if database[username]['salah_input'] >= 3:
                database[username]['status'] = "NONAKTIF"
                data_json_masuk (database)
                fungsiLog(username, ngapain = "Salah Password 3 Kali", note = "[WARNING] Indikasi Brute Force, Akun di Non-Aktifkan. LOG OUT.")
                
                raise Exception ("Terindikasi Melakukan Brute-Force")
            continue
        else:
            database[username]['salah_input'] = 0
            data_json_masuk (database)
            print("(!) Log in Berhasil!")

            fungsiLog(username, ngapain = "Login Berhasil")
        return username
    
      
    
def cek_database(database):
    print("~"*43)
    print("DATABASE".center(43))
    print("~"*43)
    print(f"{'NO.':<4}|{'USERNAME':^15}|{'STATUS':^10}")
    print("~"*43)
    for number, (key, values) in enumerate(database.items()):
        print(f"{number+1:<4}|{key:^15}|{values['status'].upper():^10}")




def keluar():
    yakin_keluar = input("(?) Anda Yakin untuk Keluar? (y/n) ")
    print("\n")

    if yakin_keluar == "Y" or yakin_keluar == "y":
        return True

    else:
        return False