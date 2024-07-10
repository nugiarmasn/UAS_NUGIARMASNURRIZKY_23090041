import pandas as pd

# Data mahasiswa dalam bentuk array 2 dimensi
data = [
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70]
]

# Membuat DataFrame
df = pd.DataFrame(data, columns=["Nama", "Algoritma dan Struktur Data 2", "Matematika Numerik"])


print("Data Mahasiswa:")
print(df)

# Menghitung rata-rata nilai untuk setiap mata kuliah
rata_rata_mata_kuliah = df.mean(numeric_only=True)
print("\nRata-rata Nilai untuk Setiap Mata Kuliah:")
print(rata_rata_mata_kuliah)

# Menghitung rata-rata nilai untuk setiap mahasiswa
df['Rata-rata'] = df.mean(axis=1, numeric_only=True)
print("\nData Mahasiswa dengan Rata-rata:")
print(df)

# Menampilkan rata-rata nilai untuk setiap mahasiswa
rata_rata_mahasiswa = df[['Nama', 'Rata-rata']]
print("\nRata-rata Nilai untuk Setiap Mahasiswa:")
print(rata_rata_mahasiswa)
