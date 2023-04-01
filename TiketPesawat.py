from Methodnya import*
class TugasLaperak :
    pilihan = 0
     
    def buat_tiket():
        nomor_penerbangan = int(input("Masukkan nomor penerbangan: "))

    # def pilihan_pesawat():
    while True:
        print("Pilih kelas:")
        print("1. Ekonomi")
        print("2. Bisnis")
        print("3. Eksekutif")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == 1:
            nama = str(input("Masukkan nama penumpang: "))
            Methodnya.tambah_penumpang('ekonomi', nama)
        elif pilihan == 2:
            nama = str(input("Masukkan nama penumpang: "))
            Methodnya.tambah_penumpang('bisnis', nama)
        elif pilihan == 3:
            nama = str(input("Masukkan nama penumpang: "))
            Methodnya.tambah_penumpang('eksekutif', nama)
        elif pilihan == 0:
            break
        else:
            print("Pilihan yang dimasukkan salah!")

    print("Tiket berhasil dibuat untuk nomor penerbangan", Methodnya.nomor_penerbangan)
    print("Daftar penumpang:")
    print("Kelas Ekonomi:", Methodnya.daftar_penumpang('ekonomi'))
    print("Kelas Bisnis:", Methodnya.daftar_penumpang('bisnis'))
    print("Kelas Eksekutif:", Methodnya.daftar_penumpang('eksekutif'))

