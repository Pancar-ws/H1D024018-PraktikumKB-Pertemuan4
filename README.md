# H1D024018-PraktikumKB-Pertemuan4
## Sistem Pakar Diagnosa Kerusakan Komputer/Laptop

Sistem pakar berbasis aturan (Rule-Based Expert System) untuk mendiagnosa kerusakan komputer/laptop berdasarkan gejala yang dipilih pengguna. Implementasi utama menggunakan antarmuka GUI (Tkinter) dengan knowledge base berbentuk dictionary, mesin inferensi berbasis pencocokan gejala, serta rekomendasi solusi singkat.

---

## Cara Kerja Program

### 1. Knowledge Base
Knowledge base berisi 6 kerusakan, masing-masing dengan 3 gejala dan 1 solusi singkat:
- RAM Rusak
- Power Supply (PSU) Lemah
- Overheat (Prosesor)
- VGA Bermasalah
- Hardisk Corrupt
- Motherboard Rusak

### 2. Pengumpulan Gejala (GUI)
Semua gejala unik ditampilkan sebagai daftar checkbox pada GUI. Pengguna memilih gejala yang dialami, lalu menekan tombol Diagnosa.

Catatan:
- Daftar gejala sudah mendukung scroll agar tetap nyaman saat gejala bertambah.
- Tombol Reset menghapus semua pilihan gejala dan hasil sebelumnya.

### 3. Mesin Inferensi (Dictionary-Based)
Inferensi dilakukan tanpa if-else panjang, melainkan dengan iterasi dictionary knowledge base:
- Hitung jumlah gejala cocok untuk setiap kerusakan.
- Ubah menjadi persentase kecocokan:
    persentase = (gejala cocok / total gejala kerusakan) x 100
- Urutkan hasil dari persentase tertinggi.
- Tetapkan tingkat keyakinan:
    - Tinggi: >= 67%
    - Sedang: 34% sampai 66%
    - Rendah: <= 33%

### 4. Output Diagnosa
Program menampilkan:
- Diagnosa utama (kerusakan dengan kecocokan tertinggi)
- Persentase kecocokan
- Tingkat keyakinan
- Jumlah gejala cocok (x dari 3)
- Solusi singkat
- Hingga 3 kemungkinan lain

Penanganan kondisi khusus:
- Jika tidak memilih gejala sama sekali: muncul pesan informasi.
- Jika gejala tidak cukup spesifik (kecocokan tertinggi < 34%):
    tampil Kerusakan Belum Dapat Dipastikan.
- Jika benar-benar tidak ada kecocokan: tampil Kerusakan Tidak Diketahui.

---

## Cara Menjalankan

Jalankan versi GUI:

python sistemPakar_gui.py

Alternatif lain yang juga tersedia di repositori:
- sistemPakar.py (console)
- sisPakNew.py (console)

---

## Contoh Penggunaan (GUI)

### Skenario 1: Motherboard Rusak
Pengguna memilih gejala:
- Komputer tidak merespon saat tombol power ditekan
- Terdengar bunyi beep panjang atau pola beep tertentu saat dinyalakan
- Perangkat keras lain (RAM/VGA) sudah dicek dan berfungsi baik

Output utama:
- Diagnosa Utama: Motherboard Rusak
- Kecocokan: 100%
- Tingkat Keyakinan: Tinggi
- Solusi: Bawa ke teknisi untuk pemeriksaan lebih lanjut; kemungkinan perlu ganti motherboard.

### Skenario 2: Gejala Kurang Spesifik
Pengguna memilih hanya 1 gejala umum.
Output:
- Kerusakan Belum Dapat Dipastikan
- Saran menambah gejala agar diagnosa lebih akurat

### Skenario 3: Tidak Memilih Gejala
Output:
- Muncul dialog informasi agar pengguna memilih gejala terlebih dahulu.

---

## Struktur Inti Kode

Struktur dictionary knowledge base:

knowledge_base = {
        "Nama Kerusakan": {
                "gejala": [list gejala],
                "solusi_singkat": "solusi"
        }
}

Alur inferensi:
1. Ekstrak semua gejala unik dari knowledge base
2. Kumpulkan gejala terpilih dari checkbox GUI
3. Hitung jumlah gejala cocok per kerusakan
4. Konversi ke persentase kecocokan
5. Urutkan dari nilai tertinggi
6. Tampilkan diagnosa utama dan kemungkinan lain

---

## Ringkasan Knowledge Base

| Kerusakan | Gejala | Solusi |
|---|---|---|
| RAM Rusak | 3 | Bersihkan/ganti RAM |
| PSU Lemah | 3 | Cek kabel power/ganti PSU |
| Overheat | 3 | Bersihkan debu & thermal paste |
| VGA Bermasalah | 3 | Update driver dan cek kabel monitor |
| Hardisk Corrupt | 3 | Backup data & upgrade SSD |
| Motherboard Rusak | 3 | Pemeriksaan teknisi/ganti motherboard |

---

## Poin Penting

- Tipe sistem: Rule-Based Expert System
- Mesin inferensi: Dictionary + pencocokan gejala
- Scoring: Persentase kecocokan (berdasarkan jumlah gejala cocok)
- Knowledge base: 6 kerusakan x 3 gejala = 18 gejala total
- Penanganan no-match: Sudah tersedia (Tidak Diketahui / Belum Dapat Dipastikan)
- Akurasi akhir tetap perlu validasi teknisi profesional

---

## Struktur File Proyek

```
H1D024018-PraktikumKB-Pertemuan4/
├── sistemPakar_gui.py  # Program GUI utama
├── Tugas 4.txt         # Instruksi tugas
├── README.md           # Dokumentasi
└── .git/
```