
import csv
import os

FILE_CSV = "material.csv"

# Queue untuk permintaan material
antrian_permintaan = []


# Membuat file CSV jika belum ada
def buat_file():
    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["kode", "nama_material", "stok", "satuan", "lokasi"]
            )


# Membaca data CSV ke Dictionary
def baca_data():
    data = {}

    with open(FILE_CSV, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data[row["kode"]] = row

    return data


# Menyimpan Dictionary ke CSV
def simpan_data(data):
    with open(FILE_CSV, "w", newline="") as file:
        fieldnames = ["kode", "nama_material", "stok", "satuan", "lokasi"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in data.values():
            writer.writerow(item)


# CREATE
def tambah_material():
    data = baca_data()

    kode = input("Kode Material : ")

    if kode in data:
        print("Kode sudah ada!")
        return

    nama = input("Nama Material : ")
    stok = int(input("Stok Awal : "))
    satuan = input("Satuan : ")
    lokasi = input("Lokasi Gudang : ")

    data[kode] = {
        "kode": kode,
        "nama_material": nama,
        "stok": str(stok),
        "satuan": satuan,
        "lokasi": lokasi
    }

    simpan_data(data)
    print("Material berhasil ditambahkan.")


# READ
def tampilkan_material():
    data = baca_data()

    print("\n===== DATA MATERIAL =====")

    if not data:
        print("Data kosong")
        return

    for item in data.values():
        print(
            f"{item['kode']} | "
            f"{item['nama_material']} | "
            f"Stok: {item['stok']} | "
            f"{item['satuan']} | "
            f"{item['lokasi']}"
        )


# UPDATE BARANG MASUK
def barang_masuk():
    data = baca_data()

    kode = input("Kode Material : ")

    if kode not in data:
        print("Material tidak ditemukan.")
        return

    jumlah = int(input("Jumlah Masuk : "))

    stok_lama = int(data[kode]["stok"])
    data[kode]["stok"] = str(stok_lama + jumlah)

    simpan_data(data)

    print("Stok berhasil ditambahkan.")


# UPDATE BARANG KELUAR
def barang_keluar():
    data = baca_data()

    kode = input("Kode Material : ")

    if kode not in data:
        print("Material tidak ditemukan.")
        return

    jumlah = int(input("Jumlah Keluar : "))
    stok_lama = int(data[kode]["stok"])

    if jumlah > stok_lama:
        print("Stok tidak mencukupi.")
        return

    data[kode]["stok"] = str(stok_lama - jumlah)

    simpan_data(data)

    print("Stok berhasil dikurangi.")


# UPDATE DATA
def edit_material():
    data = baca_data()

    kode = input("Kode Material yang akan diedit : ")

    if kode not in data:
        print("Data tidak ditemukan.")
        return

    data[kode]["nama_material"] = input("Nama Baru : ")
    data[kode]["satuan"] = input("Satuan Baru : ")
    data[kode]["lokasi"] = input("Lokasi Baru : ")

    simpan_data(data)

    print("Data berhasil diperbarui.")


# DELETE
def hapus_material():
    data = baca_data()

    kode = input("Kode Material : ")

    if kode not in data:
        print("Data tidak ditemukan.")
        return

    del data[kode]

    simpan_data(data)

    print("Data berhasil dihapus.")


# SEARCHING
def cari_material():
    data = baca_data()

    keyword = input("Masukkan kode/nama material : ").lower()

    ditemukan = False

    for item in data.values():
        if (keyword in item["kode"].lower() or
                keyword in item["nama_material"].lower()):

            print(
                f"{item['kode']} | "
                f"{item['nama_material']} | "
                f"Stok: {item['stok']}"
            )

            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.")


# SORTING
def urutkan_stok():
    data = list(baca_data().values())

    data.sort(key=lambda x: int(x["stok"]), reverse=True)

    print("\n===== STOK TERBESAR =====")

    for item in data:
        print(
            f"{item['kode']} | "
            f"{item['nama_material']} | "
            f"Stok: {item['stok']}"
        )


# QUEUE
def tambah_antrian():
    kode = input("Kode Material : ")
    antrian_permintaan.append(kode)

    print("Permintaan masuk ke antrian.")


def lihat_antrian():
    print("\n===== ANTRIAN PERMINTAAN =====")

    if not antrian_permintaan:
        print("Antrian kosong.")
        return

    for i, item in enumerate(antrian_permintaan, start=1):
        print(i, ".", item)


# MENU
def menu():
    buat_file()

    while True:
        print("\n===== SISTEM WAREHOUSE =====")
        print("1. Tambah Material")
        print("2. Lihat Material")
        print("3. Barang Masuk")
        print("4. Barang Keluar")
        print("5. Edit Material")
        print("6. Hapus Material")
        print("7. Cari Material")
        print("8. Urutkan Stok")
        print("9. Tambah Antrian")
        print("10. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih Menu : ")

        if pilihan == "1":
            tambah_material()

        elif pilihan == "2":
            tampilkan_material()

        elif pilihan == "3":
            barang_masuk()

        elif pilihan == "4":
            barang_keluar()

        elif pilihan == "5":
            edit_material()

        elif pilihan == "6":
            hapus_material()

        elif pilihan == "7":
            cari_material()

        elif pilihan == "8":
            urutkan_stok()

        elif pilihan == "9":
            tambah_antrian()

        elif pilihan == "10":
            lihat_antrian()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


menu()

