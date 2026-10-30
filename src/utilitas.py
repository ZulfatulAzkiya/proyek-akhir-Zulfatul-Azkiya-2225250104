def validasi_nilai(nilai):
    try:
        nilai = float(nilai)

        if 0 <= nilai <= 100:
            return True

        return False

    except ValueError:
        return False