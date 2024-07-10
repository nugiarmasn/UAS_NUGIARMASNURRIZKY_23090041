def main():
    # List untuk menyimpan nama mahasiswa
    mahasiswa_list = []

    while True:
        # Memasukkan nama mahasiswa
        nama = input("Masukkan nama mahasiswa: ")
        mahasiswa_list.append(nama)

        # Menanyakan apakah ingin menambah lagi
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi != 'ya':
            break

    # Menampilkan data mahasiswa
    print("\nData Mahasiswa:")
    for idx, mahasiswa in enumerate(mahasiswa_list, start=1):
        print(f"{idx}. {mahasiswa}")

if __name__ == "__main__":
    main()
