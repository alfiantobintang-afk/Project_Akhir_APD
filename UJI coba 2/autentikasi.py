from utils import clear, header, info, warning
from data_mobil import lihat_mobil, tambah_mobil, update_mobil, hapus_mobil
from sewa import sewa_mobil, kembalikan_mobil
from transaksi import lihat_transaksi

users = {"admin": {"password": "admin123", "role": "admin"}}

def login():
    clear()
    header("LOGIN SISTEM RENTAL")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        info(f"Login berhasil sebagai {users[username]['role'].upper()}")
        input("Tekan Enter untuk lanjut...")
        if users[username]["role"] == "admin":
            menu_admin()
        else:
            menu_user(username)
    else:
        warning("Username atau password salah!")
        input("Tekan Enter...")

def register():
    clear()
    header("REGISTER AKUN BARU")
    username = input("Masukkan username baru: ").strip()
    if username in users:
        warning("Username sudah terdaftar!")
    else:
        password = input("Masukkan password: ").strip()
        users[username] = {"password": password, "role": "user"}
        info("Registrasi berhasil! Silakan login.")
    input("Tekan Enter...")

def menu_admin():
    while True:
        clear()
        header("MENU ADMIN")
        print("1. Lihat daftar mobil")
        print("2. Tambah mobil")
        print("3. Update mobil")
        print("4. Hapus mobil")
        print("5. Lihat transaksi")
        print("6. Logout")

        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            lihat_mobil()
        elif pilih == "2":
            tambah_mobil()
        elif pilih == "3":
            update_mobil()
        elif pilih == "4":
            hapus_mobil()
        elif pilih == "5":
            lihat_transaksi()
        elif pilih == "6":
            break
        else:
            warning("Pilihan tidak valid!")
            input("Tekan Enter...")

def menu_user(username):
    while True:
        clear()
        header(f"MENU PENGGUNA ({username})")
        print("1. Lihat daftar mobil")
        print("2. Sewa mobil")
        print("3. Kembalikan mobil")
        print("4. Logout")

        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            lihat_mobil()
        elif pilih == "2":
            sewa_mobil(username)
        elif pilih == "3":
            kembalikan_mobil(username)
        elif pilih == "4":
            break
        else:
            warning("Pilihan tidak valid!")
            input("Tekan Enter...")
