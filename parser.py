import json


def masuk_parser_json(rekap_salah):
    with open("log_parser.json","w") as file:
        return json.dump(rekap_salah, file, indent = 4)

def keluar_parser_json ():
    with open("log_parser.json", "r") as file:
        return json.load(file)

# rekap_salah = {}
def parserLog(rekap_salah):
    with open ("security.txt", "r") as file:
        for line in file:
            if "Salah Password" in line:
                indeks = line.split("|")
                user = indeks[2]
                if user not in rekap_salah.keys():
                    rekap_salah[user] = {"times" : 1}
                else:
                    rekap_salah[user]["times"] +=1
        masuk_parser_json(rekap_salah)
    return rekap_salah

def read_parser():
    data = keluar_parser_json ()
    print("="*50)
    print(f'{"LOG PARSER":.50}')
    print("="*50)
    if not data:
        print("Log Parser Masih Kosong!")
    else:
        count = 1
        for user, kali in data.items():
            print(f"{count}. {user.strip()} telah salah password sebanyak {kali["times"]} kali")
            count+=1

#belum selesai!

