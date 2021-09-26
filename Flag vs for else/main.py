# Flag vs for...else


def guna_flag():
    print("Guna Flag")
    senarai_nama = ["Zamir", "Rasyid", "Kumar", "Mimi", "Putri", "Amirah"]
    jumpa = False
    for nama in senarai_nama:
        if nama.startswith("A"):
            jumpa = True
            print("Sudah jumpa")
            break
    if not jumpa:
        print("Tidak Jumpa")


def guna_for_else():
    print("Guna for...else")
    senarai_nama = ["Zamir", "Rasyid", "Kumar", "Mimi", "Putri", "Amirah"]
    for nama in senarai_nama:
        if nama.startswith("A"):
            print("Sudah Jumpa")
            break
    else:
        print("Tidak Jumpa")


# Bonus
def guna_any():
    print("Bonus")
    senarai_nama = ["Zamir", "Rasyid", "Kumar", "Mimi", "Putri", "Amirah"]
    if any([nama.startswith("A") for nama in senarai_nama]):
        print("Sudah Jumpa")
    else:
        print("Tidak Jumpa")


if __name__ == "__main__":
    guna_any()
