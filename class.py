
class ListWaifu:
    waifu = []

    def tambah(self):
        self.tambah_waifu = input("Masukkan nama waifu anda: ")
        self.waifu.append(self.tambah_waifu)

    def hapus(self):
        self.hapus_waifu = input(
            "Masukkan nama waifu anda yang ingin dihapus: ")
        self.waifu.remove(self.hapus_waifu)

    def tampil(self):
        for self.i in self.waifu:
            print(self.i, end=" ")
        if self.waifu == []:
            print("List msih kosong, SIlahkan Input")


a = 10


def main():
    l = ListWaifu()
    pilih = int(input("Masukkan Pilihan: "))

    if pilih == 1:
        l.tambah()
    elif pilih == 2:
        l.hapus()
    elif pilih == 3:
        l.tampil()
    else:
        print("Masukkan yang benar")


while a < 1000:
    main()
    ulang = input("\nUlang?: ")
    if ulang == "N":
        break
    a += 1
