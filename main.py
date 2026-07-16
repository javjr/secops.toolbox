
import os
import auth
from logger import fungsiLog
from parser import read_parser
import time

database = auth.data_json_keluar ()
if "admin" not in database:
    database["admin"]= {'password': auth.enkripsi('hengkerberbahaya001'),
                     'status': 'AKTIF',
                     'salah_input': 0}
    auth.data_json_masuk (database)
    
masuk = ""

#__________________
#| LOOP CLI UTAMA | 

while True:
    os_type = os.name
    match os_type:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print("\n")
    print("="*50)
    print("SECOPS TOOLBOX v1.0".center(50))
    print("="*50)
    print("\n1. Register\n2. Login\n3. Cek Database (Admin Only)\n4. Log Parser (Amin Only)\n5. Log Out")
    print("_"*50,"\n")

    pilih = input("Masukkan No. Pilihan: ")
    print("\n")

    #Logika
    if pilih == "1":
        if not masuk:
            try:
                auth.daftar(database)
            except Exception as e:
                print(f"[ALERT] Anda {e}")
                break
        else:
            print("Anda Sudah Daftar!")
            time.sleep(1)
        
    elif pilih == "2":
        if not masuk:
            try:
                masuk = auth.login(database)
            except Exception as e:
                print(f"[ALERT] Anda {e}")
                break
        else:
            print("Anda Sudah Login!")
            time.sleep()

    elif pilih == "3":
        if not masuk:
            print("(!) Silakan Login Terlebih Dahulu, sebagai ADMIN!\n")
            input("\n[Tekan ENTER untuk kembali ke menu]")
            continue
        try:
            if masuk != 'admin':
                fungsiLog(masuk, ngapain = "mencoba masuk database as admin", note = "[WARNING] LOG OUT")
                raise Exception ("WARNING! Anda Bukan Admin")
            else:
                auth.cek_database(database)
                input("\n[Tekan ENTER untuk kembali ke menu]")
        except Exception as pesan:
            print(pesan)
            input("\n[Tekan ENTER untuk kembali ke menu]")
            continue
    elif pilih == "4":
        if not masuk:
            print("(!) Silakan Login Terlebih Dahulu, sebagai ADMIN!\n")
            input("\n[Tekan ENTER untuk kembali ke menu]")
            continue
        try:
            if masuk != 'admin':
                fungsiLog(masuk, ngapain = "mencoba masuk database as admin", note = "[WARNING] LOG OUT")
                raise Exception ("WARNING! Anda Bukan Admin")
            read_parser()
            input("\n[Tekan ENTER untuk kembali ke menu]")
        except Exception as pesan:
            print(pesan)
            input("\n[Tekan ENTER untuk kembali ke menu]")
            continue
    elif pilih == "5":
        if auth.keluar():
            fungsiLog(masuk, ngapain = "Log Out")
            auth.data_json_masuk (database)
            break
        else:
            continue
    else:
        print("(!) TIDAK VALID!")
        continue

