from datetime import datetime


def dapatkan_harga_tiket():
    _dewasa = 15.00
    _kanak = 8.00

    print(f"Dewasa       : RM{_dewasa:.2f}")
    print(f"Kanak-kanak    : RM{_kanak:.2f}")
    return {"dewasa": _dewasa, "kanak-kanak": _kanak}


def dapatkan_tarikh_masa():
    # Dapatkan tarikh dan masa sekarang
    tarikh_semasa = datetime.now().date()
    waktu_semasa = datetime.now().time()

    # Format Tarikh dan Masa
    tarikh_semasa = tarikh_semasa.strftime("%d %B %Y")
    waktu_semasa = waktu_semasa.strftime("%H:%M")

    return tarikh_semasa, waktu_semasa


def papar_tiket(kategori, harga_tiket, tarikh, masa):
    print("=" * 25)
    print(f"Tiket {kategori.capitalize()}")
    print(f"Harga Tiket = RM{harga_tiket:.2f}")
    print(f"Tarikh  = {tarikh}")
    print(f"Masa    = {masa}")
    print("=" * 25)


def dapatkan_jumlah_harga(harga_tiket, n_dewasa=0, n_kanak=0):
    _diskaun = 5.00
    jumlah = harga_tiket["dewasa"] * n_dewasa + harga_tiket["kanak-kanak"] * n_kanak

    if jumlah > 80.00:
        return float(jumlah - _diskaun)

    return float(jumlah)


def main():
    harga_tiket = dapatkan_harga_tiket()

    n_dewasa = int(input("Bilangan Dewasa: "))
    n_kanak = int(input("Bilangan Kanak-Kanak: "))

    # Turunkan harga tiket jika >= 5
    if n_dewasa >= 5:
        harga_tiket["dewasa"] = 13.00

    if n_kanak >= 5:
        harga_tiket["kanak-kanak"] = 6.50

    tarikh, masa = dapatkan_tarikh_masa()

    # Papar tiket untuk setiap individu
    for _ in range(n_dewasa):
        papar_tiket("Dewasa", harga_tiket["dewasa"], tarikh, masa)

    for _ in range(n_kanak):
        papar_tiket("Kanak-Kanak", harga_tiket["kanak-kanak"], tarikh, masa)

    jumlah_harga_tiket = dapatkan_jumlah_harga(harga_tiket, n_dewasa, n_kanak)
    print(f"Jumlah Selepas Diskaun  = RM{jumlah_harga_tiket:.2f}")


if __name__ == "__main__":
    main()
