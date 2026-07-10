# secops-toolbox

Sistem autentikasi CLI dan tool untuk parsing log security.

## Fitur
- **Autentikasi:** Fitur registrasi dan login user/admin (data disimpan di `data_users.json`).
- **Log Parser:** Membaca `security.txt` untuk menghitung total percobaan gagal per user secara real-time.
- **Hak Akses:** Menu cek database dan hasil parser di-protect khusus untuk akun `admin`.

## Struktur Folder
```text
.
├── auth.py          # Logika register & login
├── parser.py        # Ekstraksi data dari security.txt
├── main.py          # Menu utama CLI
├── security.txt     # Input file log
├── data_users.json  # DB User
└── log_parser.json  # DB Hasil rekap log