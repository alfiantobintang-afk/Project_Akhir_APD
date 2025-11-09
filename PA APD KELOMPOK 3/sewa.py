from datetime import datetime, timedelta
from prettytable import PrettyTable
from colorama import Fore, Style
from data_mobil import mobil_list, clear
from transaksi import catat_transaksi

def sewa_mobil(username):
    clear()
    print(Fore.CYAN + "=== SEWA MOBIL ===\n" + Style.RESET_ALL)
    table = PrettyTable()
    table.field_names = ["Plat", "Nama Mobil", "Harga (Rp)", "Status"]
    for plat, data in mobil_list.items():
        table.add_row([plat, data["nama"], f"{data['harga']:,}", data["status"]])
    print(table)

    for data in mobil_list.values():
        if data["status"] == f"Disewa oleh {username}":
            print(Fore.YELLOW + "\nAnda sudah menyewa mobil! Kembalikan dulu sebelum menyewa lagi." + Style.RESET_ALL)
            input("Tekan Enter...")
            return

    plat_sewa = input("\nMasukkan plat mobil yang ingin disewa: ").upper().strip()
    if plat_sewa in mobil_list and mobil_list[plat_sewa]["status"] == "Tersedia":
        hari = input("Berapa hari ingin disewa?: ").strip()
        if not hari.isdigit():
            print(Fore.RED + "Input tidak valid!" + Style.RESET_ALL)
            input("Tekan Enter...")
            return
        hari = int(hari)
        data = mobil_list[plat_sewa]
        total = data["harga"] * hari

        tanggal_kembali = datetime.now() + timedelta(days=hari)
        mobil_list[plat_sewa]["status"] = f"Disewa oleh {username}"
        mobil_list[plat_sewa]["batas_waktu"] = tanggal_kembali

        print(Fore.GREEN + f"\nMobil {data['nama']} berhasil disewa!" + Style.RESET_ALL)
        print(f"Batas pengembalian: {tanggal_kembali.strftime('%d-%m-%Y %H:%M')}")
        print(f"Total sewa: Rp {total:,}")
        input("\nTekan Enter...")

    else:
        print(Fore.RED + "Mobil tidak tersedia atau plat tidak ditemukan!" + Style.RESET_ALL)
        input("Tekan Enter...")

def kembalikan_mobil(username):
    clear()
    print(Fore.CYAN + "=== PENGEMBALIAN MOBIL ===\n" + Style.RESET_ALL)
    ditemukan = False
    for plat, data in mobil_list.items():
        if data["status"] == f"Disewa oleh {username}":
            ditemukan = True
            batas = data["batas_waktu"]
            harga = data["harga"]
            nama_mobil = data["nama"]

            sekarang = datetime.now()
            terlambat = (sekarang - batas).days
            denda = 0
            if terlambat > 0:
                denda = terlambat * (harga * 0.2)

            total = harga
            total_bayar = total + denda

            print(f"Mobil: {nama_mobil}")
            print(f"Terlambat: {max(0, terlambat)} hari")
            print(f"Denda: Rp {int(denda):,}")
            print(f"Total bayar: Rp {int(total_bayar):,}")
            input("Tekan Enter untuk konfirmasi pembayaran...")

            catat_transaksi(username, plat, nama_mobil, harga, 1, total, int(denda), int(total_bayar))
            mobil_list[plat]["status"] = "Tersedia"
            del mobil_list[plat]["batas_waktu"]
            print(Fore.GREEN + "Mobil telah dikembalikan & pembayaran selesai." + Style.RESET_ALL)
            break

    if not ditemukan:
        print(Fore.YELLOW + "Anda belum menyewa mobil." + Style.RESET_ALL)
    input("Tekan Enter...")
