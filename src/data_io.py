from src.utilitas import validasi_nilai


def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                bagian = baris.strip().split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor} tidak valid.")
                    continue

                nama = bagian[0].strip()

                if not nama:
                    print(f"Nama pada baris {nomor} kosong.")
                    continue

                if not validasi_nilai(bagian[1]):
                    print(f"Nilai pada baris {nomor} tidak valid.")
                    continue

                data_siswa.append({
                    "nama": nama,
                    "nilai": float(bagian[1])
                })

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    return data_siswa


def simpan_laporan(teks):
    with open(
        "output/hasil_analisis.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(teks)