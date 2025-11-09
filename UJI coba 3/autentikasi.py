from navigasi import menu_interaktif
from utils import clear, header, info, warning
from data_mobil import lihat_mobil, tambah_mobil, update_mobil, hapus_mobil
from sewa import sewa_mobil, kembalikan_mobil
from transaksi import lihat_transaksi

users = {"admin": {"password": "admin123", "role": "admin"}}

def login():
    clear()
    header("LOGIN")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        info(f"Login sebagai {users[username]['role']}")
        if users[username]["role"] == "admin":
            menu_admin()
        else:
            menu_user(username)
    else:
        warning("Username atau password salah!")
        input("Tekan Enter...")

def register():
    clear()
    header("REGISTER")
    username = input("Username baru: ").strip()
    if username in users:
        warning("Username sudah ada!")
    else:
        password = input("Password: ").strip()
        users[username] = {"password": password, "role": "user"}
        info("Registrasi berhasil!")
    input("Tekan Enter...")

def menu_admin():
    while True:
        pilihan = menu_interaktif("MENU ADMIN", [
            "Lihat daftar mobil",
            "Tambah mobil",
            "Update mobil",
            "Hapus mobil",
            "Lihat transaksi",
            "Logout"
        ])
        if pilihan == 0: lihat_mobil()
        elif pilihan == 1: tambah_mobil()
        elif pilihan == 2: update_mobil()
        elif pilihan == 3: hapus_mobil()
        elif pilihan == 4: lihat_transaksi()
        elif pilihan == 5: break

def menu_user(username):
    while True:
        pilihan = menu_interaktif(f"MENU USER ({username})", [
            "Lihat mobil",
            "Sewa mobil",
            "Kembalikan mobil",
            "Logout"
        ])
        if pilihan == 0: lihat_mobil()
        elif pilihan == 1: sewa_mobil(username)
        elif pilihan == 2: kembalikan_mobil(username)
        elif pilihan == 3: break
