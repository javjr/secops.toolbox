import socket
from datetime import datetime

with open('security.txt', 'a') as file:
        file.write(
                   f"{'='*102}\n"
                   f"{'TIME':^27}| {'IP ADDRESS':^10} |{'USER':^10}|{'AKTIVITY':^35}|   {'NOTE':<30}\n"
                   f"{'='*102}\n")


def fungsiLog(username, ngapain, note="-"):
    name = socket.gethostname()
    ip_address = socket.gethostbyname(name)
    tanggal = datetime.now()
    time = tanggal.strftime("%d-%m-%Y %H:%M:%S")
    nama = username
    aksi = ngapain
    info = note

    with open('security.txt', 'a') as file:
        file.write(
                   f"{time:^27}| {ip_address:^10} |{nama:^10}|{aksi:^35}|   {info:<30}\n"
                   )
    return

    
    



