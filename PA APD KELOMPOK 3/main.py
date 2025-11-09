from autentikasi import login, register
from data_mobil import clear

def main():
    while True:
        clear()
        print("=== SISTEM RENTAL MOBIL MAHAL===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            input("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
