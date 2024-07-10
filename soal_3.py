class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        #Fungsi untuk menambahkan pesanan baru ke dalam antrian
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        #Fungsi untuk menghapus antrian dari depan
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Pesanan '{order}' telah dihapus dari antrian.")
            return order
        else:
            print("Antrian kosong, tidak ada pesanan untuk dihapus.")
            return None

    def display(self):
        #Fungsi untuk menampilkan semua pesanan dalam antrian
        if len(self.queue) > 0:
            print("Daftar pesanan dalam antrian:")
            for idx, order in enumerate(self.queue, start=1):
                print(f"{idx}. {order}")
        else:
            print("Antrian kosong, tidak ada pesanan.")

# Contoh penggunaan class RestaurantQueue
if __name__ == "__main__":
    queue = RestaurantQueue()
    
    # Menambahkan pesanan ke dalam antrian
    queue.enqueue("Pesanan 1: Nasi Goreng")
    queue.enqueue("Pesanan 2: Ayam Bakar")
    queue.enqueue("Pesanan 3: Sate Ayam")
    
    # Menampilkan antrian saat ini
    queue.display()
    
    # Menghapus pesanan dari antrian
    queue.dequeue()
    queue.dequeue()
    
    # Menampilkan antrian setelah penghapusan
    queue.display()
    
    # Menghapus pesanan terakhir dari antrian
    queue.dequeue()
    
    # Mencoba menghapus dari antrian kosong
    queue.dequeue()
    
    # Menampilkan antrian kosong
    queue.display()
