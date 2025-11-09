from autentikasi import login, register
from navigasi import menu_interaktif
from utils import clear, header

while True:
    pilihan = menu_interaktif("SISTEM PENGELOLAAN RENTAL MOBIL MEWAH", [
        "Login",
        "Register",
        "Keluar"
    ])

    if pilihan == 0:
        login()
    elif pilihan == 1:
        register()
    elif pilihan == 2:
        clear()
        print("Terima kasih telah menggunakan Rental Mobil Python!")
        break
