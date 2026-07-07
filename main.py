
import os
import auth
from logger import fungsiLog

database = {'admin':{'password': auth.enkripsi('hengkerberbahaya001'),
                     'status': 'AKTIF',
                     'salah_input': 0}}
masuk = ""


#__________________
#| LOOP CLI UTAMA | 
os.system("clear")
while True:
    print("\n")
    print("="*50)
    print("SECOPS TOOLBOX v1.0".center(50))
    print("="*50)
    print("\n1. Register\n2. Login\n3. Cek Database (Admin Only)\n4. Log Out ")
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
        
    elif pilih == "2":
        if not masuk:
            try:
                masuk = auth.login(database)
            except Exception as e:
                print(f"[ALERT] Anda {e}")
                break
        else:
            print("Anda Sudah Login!")

    elif pilih == "3":
        if not masuk:
            print("(!) Silakan Login Terlebih Dahulu, sebagai ADMIN!\n")
            continue
        try:
            if masuk != 'admin':
                fungsiLog(masuk, ngapain = "mencoba masuk database as admin", note = "[WARNING] LOG OUT")
                raise Exception ("WARNING! Anda Bukan Admin")
            auth.cek_database(database)
        except Exception as pesan:
            print(pesan)
            break
    elif pilih == "4":
        if auth.keluar():
            fungsiLog(masuk, ngapain = "Log Out")
            break
        else:
            continue
    else:
        print("(!) TIDAK VALID!")
        continue

