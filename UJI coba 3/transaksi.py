from datetime import datetime, timedelta
from prettytable import PrettyTable
from utils import clear, header

transaksi_list = []

def tambah_transaksi(user, plat, nama, harga):
    tanggal_sewa = datetime.now()
    batas_kembali = tanggal_sewa + timedelta(days=3)
    transaksi = {
        "user": user,
        "plat": plat,
        "mobil": nama,
        "harga": harga,
        "tanggal_sewa": tanggal_sewa,
        "batas_kembali": batas_kembali,
        "tanggal_kembali": None,
        "denda": 0
    }
    transaksi_list.append(transaksi)

def update_pengembalian(user, plat):
    from data_mobil import mobil_list
    now = datetime.now()
    for t in transaksi_list:
        if t["user"] == user and t["plat"] == plat and t["tanggal_kembali"] is None:
            t["tanggal_kembali"] = now
            selisih = (now - t["batas_kembali"]).days
            if selisih > 0:
                t["denda"] = selisih * 500000
            mobil_list[plat]["status"] = "Tersedia"
            return t
    return None

def lihat_transaksi():
    clear()
    header("RIWAYAT TRANSAKSI")
    table = PrettyTable()
    table.field_names = ["User", "Plat", "Mobil", "Sewa", "Batas", "Kembali", "Denda (Rp)"]
    for t in transaksi_list:
        table.add_row([
            t["user"],
            t["plat"],
            t["mobil"],
            t["tanggal_sewa"].strftime("%d-%m-%Y"),
            t["batas_kembali"].strftime("%d-%m-%Y"),
            t["tanggal_kembali"].strftime("%d-%m-%Y") if t["tanggal_kembali"] else "-",
            f"{t['denda']:,}"
        ])
    print(table)
    input("\nTekan Enter untuk kembali...")

