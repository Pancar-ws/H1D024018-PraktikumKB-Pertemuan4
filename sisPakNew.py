# ==========================================
# TUGAS PRAKTIKUM SISTEM PAKAR 1
# Diagnosa Kerusakan Komputer/Laptop
# ==========================================

# 1. KNOWLEDGE BASE (Menggunakan Dictionary)
# Berisi minimal 5 kerusakan dengan daftar gejala dan solusinya
knowledge_base = {
    "RAM Rusak": {
        "gejala": ["Sering muncul Blue Screen", "Terdengar bunyi beep berkali-kali saat komputer dinyalakan", "Komputer menyala tapi tidak ada tampilan di layar (No Display)"],
        "solusi": "Coba bersihkan pin emas pada RAM dengan penghapus karet secara perlahan, lalu pasang kembali. Jika tetap gagal, coba ganti dengan RAM lain."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["Komputer sering restart sendiri", "Komputer mati tiba-tiba saat membuka aplikasi berat/game", "Terdapat bau hangus dari bagian belakang casing"],
        "solusi": "Periksa apakah kipas PSU berputar dengan normal. Sebaiknya ganti PSU dengan kapasitas daya (Watt) yang lebih besar dan memiliki sertifikasi 80+."
    },
    "Overheat (Prosesor)": {
        "gejala": ["Kipas pendingin berputar sangat kencang dan bising", "Komputer mati mendadak setelah beberapa menit digunakan", "Kinerja komputer tiba-tiba menjadi sangat lambat (throttling)"],
        "solusi": "Bersihkan tumpukan debu pada kipas dan heatsink prosesor, lalu oleskan kembali thermal paste (pasta pendingin) yang baru."
    },
    "VGA Bermasalah": {
        "gejala": ["Muncul garis-garis aneh atau kotak-kotak (artefak) pada layar", "Layar tiba-tiba blank atau hitam saat memutar video", "Resolusi layar macet di ukuran kecil dan tidak bisa diubah"],
        "solusi": "Update atau install ulang driver VGA Anda. Pastikan suhu VGA aman dan kipasnya berputar. Jika artefak tetap muncul, kemungkinan chip VGA mulai rusak."
    },
    "Hardisk Corrupt": {
        "gejala": ["Sistem Windows sangat lambat saat melakukan booting", "Terdengar suara berdecit, 'klik', atau 'krek' dari dalam casing", "Sering muncul pesan error 'Disk Boot Failure' saat dinyalakan"],
        "solusi": "Segera backup data-data penting Anda ke penyimpanan eksternal. Gunakan software pengecek kesehatan disk, dan sangat disarankan untuk upgrade ke SSD."
    }
}

def diagnosa_kerusakan():
    print("=========================================================")
    print("       Sistem Pakar Diagnosa Kerusakan Komputer          ")
    print("=========================================================")
    print("Jawablah pertanyaan berikut dengan 'y' (ya) atau 't' (tidak).")
    print("-" * 57)
    
    # Kumpulkan semua gejala unik dari knowledge base
    daftar_gejala_unik = set()
    for info in knowledge_base.values():
        for gejala in info["gejala"]:
            daftar_gejala_unik.add(gejala)
    
    gejala_user = []
    
    # Proses tanya jawab dengan pengguna
    for gejala in daftar_gejala_unik:
        jawaban = input(f"Apakah {gejala}? (y/t): ").strip().lower()
        if jawaban == 'y':
            gejala_user.append(gejala)
            
    print("\n=========================================================")
    print("                   HASIL DIAGNOSA                        ")
    print("=========================================================")
    
    # 2. MESIN INFERENSI
    # Mencocokkan gejala user dengan knowledge base
    if not gejala_user:
        print("Anda tidak memasukkan gejala apapun. Komputer Anda sepertinya normal.")
        return

    hasil_diagnosa = []
    
    for kerusakan, info in knowledge_base.items():
        gejala_kerusakan = info["gejala"]
        # Menghitung seberapa banyak gejala yang cocok dengan database
        kecocokan = len(set(gejala_user).intersection(gejala_kerusakan))
        
        if kecocokan > 0:
            hasil_diagnosa.append({
                "kerusakan": kerusakan,
                "skor_kecocokan": kecocokan,
                "solusi": info["solusi"]
            })
            
    # 3. OUTPUT
    # Menampilkan hasil jika cocok atau jika tidak ada yang cocok
    if not hasil_diagnosa:
        print("Gejala yang dimasukkan tidak cocok dengan kerusakan apa pun di sistem kami.")
    else:
        # Mengurutkan berdasarkan gejala yang paling banyak cocok
        hasil_diagnosa = sorted(hasil_diagnosa, key=lambda x: x["skor_kecocokan"], reverse=True)
        
        # Ambil hasil dengan kecocokan tertinggi (elemen pertama setelah sort)
        kerusakan_teratas = hasil_diagnosa[0]
        
        # Format output ini sudah sesuai dengan kriteria yang meminta 
        # untuk menampilkan nama kerusakan dan solusi singkat
        print(f"Diagnosa Kerusakan : {kerusakan_teratas['kerusakan']}")
        print(f"Solusi Singkat     : {kerusakan_teratas['solusi']}")
        print(f"(Cocok dengan {kerusakan_teratas['skor_kecocokan']} gejala)")

# Menjalankan program utama
if __name__ == "__main__":
    diagnosa_kerusakan()