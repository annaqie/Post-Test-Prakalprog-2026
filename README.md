# 🏠 Analisis Tren dan Pemodelan Prediksi Harga Rumah (Kelompok 4 - Kelas C)

Repositori ini dibuat sebagai dokumentasi dan penyimpanan seluruh tugas Post-Test Praktikum Algoritma dan Pemrograman Semester 2 Teknik Elektro Universitas Diponegoro. Proyek ini berfokus pada Analisis Data Eksploratif, visualisasi tren, serta pembangunan model analitik untuk memprediksi harga rumah menggunakan dataset **"Kelas C_Housing.csv"**.

Repositori ini bersifat **Public** agar dapat diakses dengan mudah oleh tim asisten praktikum untuk proses penilaian.

---

## 👥 Akuntabilitas & Distribusi Peran

Sesuai dengan prinsip kolaborasi dan transparansi kerja kelompok, berikut adalah pembagian tugas (*jobdesk*) dan identitas resmi dari setiap anggota Kelompok 4 Kelas C:

| Nama Anggota | NIM | Kontribusi & Rincian Tugas (*Jobdesk*) |
| :--- | :---: | :--- |
| **Aun Nurofiq Fuadi** | 21060125120017 | <ul><li>Membuat program grafik/analisis kategori A</li><li>Berkontribusi aktif dalam mendesain infografis hasil akhir</li></ul> |
| **Habib Azka Ekhwanputra** | 21060125130060 | <ul><li>Membuat program grafik/analisis kategori B</li><li>Berkontribusi aktif dalam mendesain infografis hasil akhir</li></ul> |
| **Muhammad Najamuddin** | 21060125120003 | <ul><li>Menggabungkan program visualisasi dan analisis (Kategori A, B, C, D)</li><li>Berkontribusi aktif dalam mendesain infografis hasil akhir</li></ul> |
| **Musa Annaqi** | 21060125120021 | <ul><li>Membuat program grafik/analisis kategori C</li><li>Mengatur struktur, manajemen, dan pemeliharaan repositori GitHub</li></ul> |
| **Shafa Reswara Nurhadi** | 21060125120011 | <ul><li>Membuat program grafik/analisis kategori D</li><li>Berkontribusi aktif dalam mendesain infografis hasil akhir</li></ul> |

---

## 📊 Deskripsi Dataset

Dataset yang digunakan dalam proyek ini adalah **"Kelas C_Housing.csv"**. Dataset ini berisi informasi struktural dan karakteristik fisik dari properti rumah yang memengaruhi nilai jualnya di pasar.

### Struktur Data Utama:
*   **Fitur Target:** `Price` (Harga Rumah)
*   **Fitur Numerik:** `Area` (Luas Lahan/Bangunan), `Bedrooms` (Jumlah Kamar Tidur), `Bathrooms` (Jumlah Kamar Mandi), `Stories` (Jumlah Lantai).
*   **Fitur Kategorikal:** `Mainroad` (Akses Jalan Utama), `Guestroom` (Ketersediaan Kamar Tamu), `Basement`, `Hotwaterheating` (Pemanas Air), `Airconditioning` (AC), `Parking` (Kapasitas Parkir), `Prefarea` (Area Preferensi), `Furnishingstatus` (Status Perabotan).

---

## 🛠 Arsitektur dan Alur Kode

Aplikasi ini dibagi menjadi beberapa tahapan kode (mencakup program Kategori A, B, C, D, dan program gabungan) yang mengimplementasikan *pipeline* analisis data berikut:

1. **Pra-pemrosesan Data (Data Preprocessing):** Memuat berkas `.csv`, membersihkan data kosong, dan melakukan transformasi data kategorikal menjadi bentuk numerik agar dapat dibaca oleh algoritma.
2. **Analisis Data Eksploratif (EDA):** Menghitung nilai statistik deskriptif dasar seperti rata-rata (mean), median, persebaran data, serta mendeteksi pencilan (*outliers*).
3. **Visualisasi Data & Tren:** Pembuatan visualisasi menggunakan grafik batang (*bar plot*), diagram sebar (*scatter plot*), dan matriks korelasi (*heatmap*).
4. **Pemodelan & Prediksi:** Membagi data menjadi data latih (*training set*) dan data uji (*testing set*) untuk melatih algoritma regresi.
5. **Evaluasi Performa:** Mengukur tingkat akurasi hasil prediksi harga rumah menggunakan metrik $R^2$ Score, MAE (Mean Absolute Error), dan MSE (Mean Squared Error).

---

## 💻 Teknologi dan Library yang Digunakan

*   **Python 3.14** - Bahasa pemrograman utama.
*   **Jupyter Notebook (`.ipynb`)** - Lingkungan kerja interaktif untuk penulisan kode dan penampilan grafik secara langsung.
*   **Pandas & NumPy** - Digunakan untuk manipulasi struktur tabel data dan komputasi matriks numerik.
*   **Matplotlib & Seaborn** - Digunakan untuk memproduksi visualisasi grafik tren yang rapi dan informatif.
*   **Scikit-Learn (Sklearn)** - Digunakan untuk penyediaan algoritma machine learning regresi dan metrik evaluasi.

---

## 🚀 Cara Menjalankan Program di Lokal

1. Pastikan Anda telah mengunduh (atau melakukan clone) seluruh isi repositori ini.
2. Tempatkan berkas kode program (`.ipynb`) dan berkas dataset `Kelas C_Housing.csv` di dalam **satu direktori/folder yang sama**.
3. Buka terminal atau command prompt, lalu pasang *library* pendukung dengan perintah:
```bash
   pip install pandas numpy matplotlib seaborn scikit-learn ipykernel
