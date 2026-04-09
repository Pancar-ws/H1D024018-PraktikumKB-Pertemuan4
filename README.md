# H1D024018-PraktikumKB-Pertemuan4

## Penjelasan sisPakNew.py

Script ini adalah sistem pakar sederhana untuk diagnosa kerusakan komputer/laptop berbasis aturan. Alur utamanya:

1. **Knowledge base**
	- Disimpan dalam dictionary `knowledge_base`.
	- Setiap kerusakan memiliki daftar `gejala` dan `solusi` singkat.

2. **Pengumpulan gejala dari pengguna**
	- Semua gejala unik dikumpulkan dari knowledge base.
	- Program menanyakan setiap gejala ke pengguna dengan input `y/t`.

3. **Mesin inferensi (pencocokan)**
	- Gejala dari pengguna dibandingkan dengan gejala tiap kerusakan.
	- Dihitung skor kecocokan berdasarkan jumlah gejala yang sama.

4. **Hasil diagnosa**
	- Jika tidak ada gejala, program memberi pesan bahwa komputer normal.
	- Jika ada kecocokan, hasil diurutkan dari skor tertinggi.
	- Ditampilkan kerusakan dengan skor tertinggi beserta solusi singkat.

### Cara menjalankan

Jalankan file dengan Python:

```bash
python sisPakNew.py
```

Kemudian jawab pertanyaan dengan `y` (ya) atau `t` (tidak).