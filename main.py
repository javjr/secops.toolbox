
import os
import auth

database = {}
masuk = ""


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

    pilih = input("Masukkan No. Pilihan: ")
    print("\n")

    #Logika
    if pilih == "1":
        auth.daftar(database)
    elif pilih == "2":
        auth.login(database)
    elif pilih == "3":
        auth.cek_database(database)
    elif pilih == "4":
        if auth.keluar():
            break
        else:
            continue
    else:
        print("(!) TIDAK VALID!")
        continue

