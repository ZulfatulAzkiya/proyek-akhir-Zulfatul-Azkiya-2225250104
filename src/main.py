import os

from src.data_io import baca_data, simpan_laporan
from src.analisis import hitung_statistik


def main():
    os.makedirs("output", exist_ok=True)

    data = baca_data("data/nilai_contoh.txt")

    statistik = hitung_statistik(data)

    if statistik is None:
        print("Tidak ada data nilai yang valid.")
        return

    laporan = (
        "HASIL ANALISIS NILAI MATEMATIKA\n"
        "================================\n"
        f"Jumlah siswa: {statistik['jumlah']}\n"
        f"Rata-rata: {statistik['rata_rata']:.2f}\n"
        f"Nilai tertinggi: {statistik['tertinggi']}\n"
        f"Nilai terendah: {statistik['terendah']}\n"
        f"Siswa tuntas: {statistik['tuntas']}\n"
        f"Siswa belum tuntas: {statistik['belum_tuntas']}\n"
    )

    print(laporan)

    simpan_laporan(laporan)

    print("Laporan berhasil disimpan.")


if __name__ == "__main__":
    main()