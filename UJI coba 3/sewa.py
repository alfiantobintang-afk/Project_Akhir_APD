from prettytable import PrettyTable
from utils import clear, header, info, warning
from data_mobil import mobil_list
from transaksi import tambah_transaksi, update_pengembalian

def sewa_mobil(user):
    clear()
    header("SEWA MOBIL")
    table = PrettyTable()
    table.field_names = ["Plat", "Nama Mobil", "Harga", "Status"]
    for plat, data in mobil_list.items():
        table.add_row([plat, data["nama"], f"{data['harga']:,}", data["status"]])
    print(table)

    for data in mobil_list.values():
        if data["status"] == f"Disewa oleh {user}":
            warning("Anda sudah menyewa mobil!")
            input("Tekan Enter...")
            return

    plat = input("Masukkan plat mobil: ").upper().strip()
    if plat in mobil_list and mobil_list[plat]["status"] == "Tersedia":
        mobil_list[plat]["status"] = f"Disewa oleh {user}"
        tambah_transaksi(user, plat, mobil_list[plat]["nama"], mobil_list[plat]["harga"])
        info(f"Mobil {mobil_list[plat]['nama']} berhasil disewa 3 hari!")
    else:
        warning("Mobil tidak tersedia atau salah plat!")
    input("Tekan Enter...")

def kembalikan_mobil(user):
    clear()
    header("PENGEMBALIAN MOBIL")
    plat = input("Masukkan plat mobil Anda: ").upper().strip()
    transaksi = update_pengembalian(user, plat)
    if transaksi:
        if transaksi["denda"] > 0:
            warning(f"Terlambat! Denda: Rp{transaksi['denda']:,}")
        info(f"Mobil {transaksi['mobil']} dikembalikan!")
    else:
        warning("Tidak ada data sewa aktif!")
    input("Tekan Enter...")

