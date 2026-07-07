import socket
from datetime import datetime

# with open('security.txt', 'a', encoding='utf-8') as file:
#     file.write(
#         f"{'='*150}\n"
#         f"{'TIME'.center(27)} | {'IP ADDRESS'.center(14)} | {'USER'.center(12)} | {'ACTIVITY'.center(35)} |   {'NOTE'.center(35)}\n"
#         f"{'='*150}\n"
#     )

def fungsiLog(username, ngapain, note="-"):
    name = socket.gethostname()
    try:
        ip_address = socket.gethostbyname("goole.com")
    except Exception as e:
        ip_address = "127.0.0.1"
        
    tanggal = datetime.now()
    time = tanggal.strftime("%d-%m-%Y %H:%M:%S")
    nama = username
    aksi = ngapain
    info = note

    with open('security.txt', 'a', encoding='utf-8') as file:
        file.write(
                   f"{time:^27} | {ip_address:^14} | {nama:^12} | {aksi:^35} |   {info:^35}\n"
                   )
    return


