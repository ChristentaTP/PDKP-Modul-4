import os
proses = True

def daftar_menu():
        print("=================================="
              "\nDaftar Tiket Pesawat yang Tersedia"
              "\n=================================="
              "\n1. Semarang-Jakarta"
              "\n2. Semarang-Surabaya"
              "\n3. Semarang-Medan"
              "\n4. Semarang-Balikpapan"
              "\n=================================="
              "\nKetik 0 untuk Keluar")
    
def pemesanan():
        jum_tiket = int(input("Masukkan Jumlah tiket: "))
        numArray = list()
        num = input("berapa orang yang ingin memesan tiket: ")
        print("masukkan nama pemesan: ")
        for i in range (int(num)):
            i+=1
            n = input("orang ke {}: ".format(i))
            numArray.append(str(n))
        tot_tiket = jum_tiket*harga
        os.system('cls')
        print("\n============================================="
              "\nAnda telah berhasil melakukan pembelian tiket"
              "\n============================================="
              "\nNama pemesan:{}".format(len(numArray)))
        for x in numArray:
                print(("-{}").format(x))
        print("Total Harga","Rp.",(tot_tiket))

