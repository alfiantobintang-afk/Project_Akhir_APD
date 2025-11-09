from prettytable import PrettyTable
from utils import clear, header, info, warning
from data_mobil import mobil_list
from transaksi import tambah_transaksi, update_pengembalian

def sewa_mobil(username):
    clear()
    header("SEWA MOBIL")
    table = PrettyTable()
    table.field_names = ["Plat", "Nama Mobil", "Harga (Rp)", "Status"]
    for plat, data in mobil_list.items():
        table.add_row([plat, data["nama"], f"{data['harga']:,}", data["status"]])
    print(table)

    # Cegah user menyewa lebih dari satu
    for data in mobil_list.values():
        if data["status"] == f"Disewa oleh {username}":
            warning("Anda sudah menyewa mobil! Kembalikan dulu sebelum menyewa lagi.")
            input("Tekan Enter...")
            return

    plat_sewa = input("\nMasukkan plat mobil yang ingin disewa: ").upper().strip()
    if plat_sewa in mobil_list:
        if mobil_list[plat_sewa]["status"] == "Tersedia":
            mobil_list[plat_sewa]["status"] = f"Disewa oleh {username}"
            tambah_transaksi(username, plat_sewa, mobil_list[plat_sewa]["nama"], mobil_list[plat_sewa]["harga"])
            info(f"Mobil {mobil_list[plat_sewa]['nama']} berhasil disewa selama 3 hari.")
        else:
            warning("Mobil sedang disewa!")
    else:
        warning("Plat tidak ditemukan!")
    input("Tekan Enter...")

def kembalikan_mobil(username):
    clear()
    header("PENGEMBALIAN MOBIL")
    plat = input("Masukkan plat mobil yang Anda sewa: ").upper().strip()
    transaksi = update_pengembalian(username, plat)
    if transaksi:
        if transaksi["denda"] > 0:
            warning(f"Terlambat! Anda dikenakan denda Rp{transaksi['denda']:,}")
        info(f"Mobil {transaksi['mobil']} telah dikembalikan. Terima kasih!")
    else:
        warning("Tidak ditemukan data sewa aktif dengan plat tersebut.")
    input("Tekan Enter...")
