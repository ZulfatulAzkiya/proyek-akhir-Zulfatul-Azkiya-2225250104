KKM = 60


def hitung_statistik(data_siswa):
    if not data_siswa:
        return None

    nilai = [siswa["nilai"] for siswa in data_siswa]

    return {
        "jumlah": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "tertinggi": max(nilai),
        "terendah": min(nilai),
        "tuntas": sum(1 for n in nilai if n >= KKM),
        "belum_tuntas": sum(1 for n in nilai if n < KKM)
    }