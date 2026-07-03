import os

database = {}
out = 0
masuk = 0
#__________
#| FUNGSI |

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
        print("\n(!) Register Berhasil!")
        status = "aktif"
        salah = 0
        database[username] = {'password' : password,
                               'status' : status,
                               'salah_input' : salah}
        return


def login(database):
    while True:

        username = input("Masukkan Username: ")
        if username not in database:
            print("\n(!) Pengguna Tidak Ditemukan\n")
            continue
        elif database[username]['status'] == "NONAKTIF":
            print("(!) Akun Anda Sedang DiNonaktifkan\nHubungi Admin Untuk Memulihkan Akun\n")
            return

        password = input("Masukkan Password: ")
        print("\n")
        if password != database[username]['password']:
            database[username]['salah_input'] += 1
            print("(!) Password Salah!\n")

            if database[username]['salah_input'] >= 3:
                database[username]['status'] = "NONAKTIF"
                print("\n(!) ALERT: Anda Sudah Gagal Log in Lebih dari Tiga Kali, Akun di Nonaktifkan Sementara")
                print("==> Silakan Hubungi Admin Untuk Memulihkan Akun\n")
                break
            continue
        else:
            global masuk
            masuk = 1
            print("(!) Log in Berhasil!")
        return
    
      
    
def cek_database(database):
    if not masuk:
        print("(!) Silakan Login Terlebih Dahulu!\n")
        return
    print("~"*43)
    print("DATABASE".center(43))
    print("~"*43)
    print(f'{'NO.':<4}|{'USERNAME':^15}|{'PASSWORD':^10}|{'STATUS':^10}')
    print("~"*43)
    for number, (key, values) in enumerate(database.items()):
        print(f'{number+1:<4}|{key:^15}|{values['password']:^10}|{values['status'].upper():^10}')




def keluar():
    yakin_keluar = input("(?) Anda Yakin untuk Keluar? (y/n) ")
    print("\n")

    if yakin_keluar == "N" or yakin_keluar == "n":
        return
    else:
        global out
        out = 1
        return





#__________________
#| LOOP CLI UTAMA | 
os.system("clear")
while True:
    print("\n")
    print("="*50)
    print("SECOPS TOOLBOX v1.0".center(50))
    print("="*50)
    print("\n1. Register\n2. Login\n3. Cek Database\n4. Log Out ")
    print("_"*50,"\n")

    pilih = int(input("Masukkan No. Pilihan: "))
    print("\n")

    #Logika
    if pilih == 1:
        daftar(database)
    elif pilih == 2:
        login(database)
    elif pilih == 3:
        cek_database(database)
    elif pilih == 4:
        keluar()
        if out:
            break
    else:
        print("(!) TIDAK VALID!")
        continue

