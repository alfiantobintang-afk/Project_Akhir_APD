from datetime import datetime, timedelta

transaksi_list = []

def tambah_transaksi(username, plat, nama_mobil, harga):
    tanggal_sewa = datetime.now()
    batas_kembali = tanggal_sewa + timedelta(days=3)
    transaksi = {
        "user": username,
        "plat": plat,
        "mobil": nama_mobil,
        "harga": harga,
        "tanggal_sewa": tanggal_sewa,
        "batas_kembali": batas_kembali,
        "tanggal_kembali": None,
        "denda": 0
    }
    transaksi_list.append(transaksi)

def update_pengembalian(username, plat):
    from data_mobil import mobil_list
    now = datetime.now()
    for t in transaksi_list:
        if t["user"] == username and t["plat"] == plat and t["tanggal_kembali"] is None:
            t["tanggal_kembali"] = now
            selisih = (now - t["batas_kembali"]).days
            if selisih > 0:
                t["denda"] = selisih * 500000
            mobil_list[plat]["status"] = "Tersedia"
            return t
    return None

def lihat_transaksi():
    from prettytable import PrettyTable
    from utils import clear, header
    clear()
    header("DAFTAR TRANSAKSI")
    table = PrettyTable()
    table.field_names = ["User", "Plat", "Mobil", "Tanggal Sewa", "Batas", "Kembali", "Denda (Rp)"]

    for t in transaksi_list:
        table.add_row([
            t["user"],
            t["plat"],
            t["mobil"],
            t["tanggal_sewa"].strftime("%d-%m-%Y %H:%M"),
            t["batas_kembali"].strftime("%d-%m-%Y"),
            t["tanggal_kembali"].strftime("%d-%m-%Y %H:%M") if t["tanggal_kembali"] else "-",
            f"{t['denda']:,}"
        ])
    print(table)
    input("\nTekan Enter untuk kembali...")
