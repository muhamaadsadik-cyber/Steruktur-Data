# Data awal mahasiswa
data_mahasiswa = [
   
    ["neza",  95],
    ["rhido", 75],
    ["sahdik",90],
    ["riski", 85],
    ["habib", 98],
    ["aldo",  65],
    ["sandi", 68],
    ["lale",  92],
    ["rofal", 90],
    ["gazi",  90],
    ["rifi",  89],
    ["ciba",  98],
    ["pina",  90],
    ["diah",  95]
]

while True:
    print("\n===================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("===================================")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Tambah Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Cari Data Mahasiswa")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")

    # 1. Tampilkan Data
    if pilihan == "1":
        print("\nDAFTAR MAHASISWA")
        print("-" * 30)

        if len(data_mahasiswa) == 0:
            print("Data mahasiswa kosong.")
        else:
            for i, mahasiswa in enumerate(data_mahasiswa, start=1):
                print(f"{i}. {mahasiswa[0]} - Nilai: {mahasiswa[1]}")

    # 2. Tambah Data
    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))

        data_mahasiswa.append([nama, nilai])

        print("Data berhasil ditambahkan.")

    # 3. Ubah Data
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")

        ditemukan = False

        for mahasiswa in data_mahasiswa:
            if mahasiswa[0].lower() == nama.lower():
                nilai_baru = int(input("Masukkan nilai baru: "))
                mahasiswa[1] = nilai_baru

                ditemukan = True
                print("Data berhasil diubah.")
                break

        if not ditemukan:
            print("Mahasiswa tidak ditemukan.")

    # 4. Hapus Data
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")

        ditemukan = False

        for mahasiswa in data_mahasiswa:
            if mahasiswa[0].lower() == nama.lower():
                data_mahasiswa.remove(mahasiswa)

                ditemukan = True
                print("Data berhasil dihapus.")
                break

        if not ditemukan:
            print("Mahasiswa tidak ditemukan.")

    # 5. Cari Data
    elif pilihan == "5":
        nama = input("Masukkan nama mahasiswa yang dicari: ")

        ditemukan = False

        for mahasiswa in data_mahasiswa:
            if mahasiswa[0].lower() == nama.lower():
                print("\nData Ditemukan")
                print("Nama  :", mahasiswa[0])
                print("Nilai :", mahasiswa[1])

                ditemukan = True
                break

        if not ditemukan:
            print("Mahasiswa tidak ditemukan.")

    # 6. Urutkan Nilai Tertinggi
    elif pilihan == "6":
        if len(data_mahasiswa) > 0:
            data_mahasiswa.sort(key=lambda x: x[1], reverse=True)

            print("\nData berhasil diurutkan berdasarkan nilai tertinggi")
            print("-" * 40)

            for mahasiswa in data_mahasiswa:
                print(f"{mahasiswa[0]} - {mahasiswa[1]}")
        else:
            print("Data mahasiswa kosong.")

    # 7. Hitung Rata-rata
    elif pilihan == "7":
        if len(data_mahasiswa) > 0:
            total = 0

            for mahasiswa in data_mahasiswa:
                total += mahasiswa[1]

            rata_rata = total / len(data_mahasiswa)

            print(f"\nRata-rata nilai mahasiswa = {rata_rata:.2f}")
        else:
            print("Data mahasiswa kosong.")

    # 8. Keluar
    elif pilihan == "8":
        print("Terima kasih telah menggunakan program.")
        break

    # Jika pilihan salah
    else:
        print("Pilihan tidak valid! Silakan pilih 1-8.")