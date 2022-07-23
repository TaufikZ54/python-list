waifu = []


def tambah():
    tambah_waifu = input("Masukkan nama waifu anda: ")
    waifu.append(tambah_waifu)


def hapus():
    hapus_waifu = input("Masukkan nama waifu anda yang ingin dihapus: ")
    waifu.remove(hapus_waifu)


def edit():
    ganti_waifu = input("Masukkan nama waifu anda yang ingin diganti: ")
    waifu_baru = input("Masukkan nama waifu anda yang baru: ")
    waifu[ganti_waifu] = waifu_baru


def tampil():
    for i in waifu:
        print(i, end=" ")
    if waifu == []:
        print("List msih kosong, SIlahkan Input")


def main():
    a = 1
    while a < 1000:
        print("\nPilih")
        print("1. Tambah")
        print("2. Hapus")
        print("3. Edit")
        print("4. Tampil")

        pilihan = int(input("Masukkan Pilihan: "))
        if pilihan == 1:
            tambah()
        elif pilihan == 2:
            hapus()
        elif pilihan == 3:
            edit()
        elif pilihan == 4:
            tampil()
        else:
            print("Masukkan pilihan yang benar!!!")
        ulang = input("Ulang?: ")
        if ulang == "N":
            print("Bye.......")
            break
        a += 1


main()
