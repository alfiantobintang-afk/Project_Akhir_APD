from autentikasi import login, register
from utils import clear, header

while True:
    clear()
    header(" SISTEM PENGELOLAAN RENTAL MOBIL MEWAH")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ").strip()

    if pilihan == "1":
        login()
    elif pilihan == "2":
        register()
    elif pilihan == "3":
        clear()
        print("Terima kasih telah menggunakan program rental mobil!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")
