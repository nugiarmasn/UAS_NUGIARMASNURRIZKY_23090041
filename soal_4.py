class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def atur_nama(self, nama):
        self.nama = nama

    def atur_warna(self, warna):
        self.warna = warna

    def atur_rasa(self, rasa):
        self.rasa = rasa

    def informasi(self):
        #Menampilkan informasi buah
        print(f"Nama Buah: {self.nama}")
        print(f"Warna Buah: {self.warna}")
        print(f"Rasa Buah: {self.rasa}")

class KelolaBuah(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def atur_vitamin(self, vitamin):
        self.vitamin = vitamin

    def informasi(self):
        """Menampilkan informasi buah beserta vitaminnya"""
        super().informasi()
        print(f"Vitamin Buah: {self.vitamin}")

# Contoh penggunaan kelas
if __name__ == "__main__":
    # Membuat objek dari kelas anak
    buah = KelolaBuah("Apel", "Merah", "Manis", "Vitamin C")

    # Memanggil atribut dan metode
    buah.informasi()
    
    # Mengubah atribut menggunakan metode atur
    buah.atur_nama("Pisang")
    buah.atur_warna("Kuning")
    buah.atur_rasa("Manis")
    buah.atur_vitamin("Vitamin B6")


    print("\nInformasi setelah perubahan:")
    buah.informasi()
