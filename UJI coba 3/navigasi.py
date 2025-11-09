import msvcrt
import os
from colorama import Back, Fore, Style

def menu_interaktif(judul, opsi):
    posisi = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "=" * 60)
        print(Fore.YELLOW + judul.center(60))
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        for i, o in enumerate(opsi):
            if i == posisi:
                print(Fore.BLACK + Back.YELLOW + f"> {o}" + Style.RESET_ALL)
            else:
                print(f"  {o}")
        print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        key = msvcrt.getch()

        if key == b'\xe0':  # tombol arah
            arah = msvcrt.getch()
            if arah == b'H':  # atas
                posisi = (posisi - 1) % len(opsi)
            elif arah == b'P':  # bawah
                posisi = (posisi + 1) % len(opsi)
        elif key == b'\r':  # Enter
            return posisi
