"""
    1. kalau tahun boleh dibahagi dengan 4, pergi ke langkah 2. Kalau tidak, terus ke langkah 5.
    2. kalau tahun boleh dibahagi dengan 100, pergi ke langkah 3. Kalau tidak, terus ke langkah 4.
    3. kalau tahun boleh dibahagi dengan 400, pergi ke langkah 4. Kalau tidak, terus ke langkah 5.
    4. tahun tersebut adalah tahun lompat (366 hari)
    5. tahun tersebut adalah bukan tahun lompat (365 hari)
"""

input_tahun = int(input("Masukkan Tahun: "))
tahun_lompat = input_tahun % 4 == 0 and (input_tahun % 100 != 0 or input_tahun % 400 == 0)
print(f"Bilangan hari pada tahun {input_tahun} adalah {365 + int(tahun_lompat)} hari.")   
