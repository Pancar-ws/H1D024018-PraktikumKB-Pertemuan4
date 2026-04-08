def main():
    knowledge_base = {
        "RAM Rusak": {
            "gejala": ["Terdengar bunyi beep berulang saat dinyalakan", "Sering mengalami Blue Screen (BSOD)", "Layar blank hitam tapi mesin menyala"],
            "solusi_singkat": "Cabut RAM, bersihkan pin dengan penghapus, lalu pasang kembali."
        },
        "Power Supply (PSU) Lemah": {
            "gejala": ["Komputer mati tiba-tiba saat digunakan", "Komputer sering restart sendiri tanpa peringatan", "Terdengar suara letupan atau bau gosong"],
            "solusi_singkat": "Cek kabel power; bila sering mati mendadak, ganti PSU."
        },
        "Overheat (Prosesor)": {
            "gejala": ["Kipas berputar sangat kencang dan berisik", "Suhu casing/laptop terasa sangat panas", "Komputer mati saat menjalankan aplikasi/game berat"],
            "solusi_singkat": "Bersihkan kipas/heatsink dan ganti thermal paste."
        },
        "VGA Bermasalah": {
            "gejala": ["Layar menampilkan garis-garis (artefak)", "Warna pada layar terlihat aneh/pudar", "Tidak ada tampilan di monitor meski indikator nyala"],
            "solusi_singkat": "Update driver VGA dan cek kabel monitor."
        },
        "Hardisk Corrupt": {
            "gejala": ["Proses booting dan loading aplikasi sangat lambat", "Terdengar bunyi 'klik' atau suara kasar dari dalam PC", "Muncul pesan 'Disk Boot Failure' atau 'No Bootable Device'"],
            "solusi_singkat": "Segera backup data dan pertimbangkan ganti ke SSD."
        }
    }

    semua_gejala = []
    for data in knowledge_base.values():
        for gejala in data["gejala"]:
            if gejala not in semua_gejala:
                semua_gejala.append(gejala)

    print("="*70)
    print("SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER / LAPTOP".center(70))
    print("="*70)
    print("Jawablah pertanyaan berikut dengan 'Y' (Ya) atau 'T' (Tidak)\n")

    gejala_dialami = []

    for gejala in semua_gejala:
        while True:
            jawaban = input(f"Apakah Anda mengalami: {gejala}? (Y/T): ").strip().upper()
            if jawaban in ['Y', 'T']:
                break
            print("Input tidak valid. Harap masukkan 'Y' atau 'T'.")
        
        if jawaban == 'Y':
            gejala_dialami.append(gejala)

    print("\n" + "="*70)
    print("HASIL DIAGNOSA".center(70))
    print("="*70)

    hasil_diagnosa = []

    for kerusakan, data in knowledge_base.items():
        cocok = sum(1 for g in data["gejala"] if g in gejala_dialami)
        
        if cocok > 0:
            persentase = (cocok / len(data["gejala"])) * 100
            hasil_diagnosa.append({
                "kerusakan": kerusakan,
                "kecocokan": persentase,
                "solusi_singkat": data["solusi_singkat"]
            })

    if not gejala_dialami:
        print("Anda tidak memilih gejala apa pun. Komputer Anda sepertinya dalam kondisi baik-baik saja.")
    elif not hasil_diagnosa: # Menangani jika tidak ada yang cocok sama sekali
        print("Kerusakan Tidak Diketahui.")
        print("Solusi    : Gejala yang Anda masukkan tidak cocok dengan database kami. Coba bawa ke tempat servis terdekat.")
    else:
        # Mengurutkan hasil diagnosa berdasarkan persentase kecocokan tertinggi
        hasil_diagnosa.sort(key=lambda x: x["kecocokan"], reverse=True)
        
        # Mengambil kerusakan dengan probabilitas tertinggi
        diagnosa_utama = hasil_diagnosa[0]
        
        print(f"Diagnosa Utama   : {diagnosa_utama['kerusakan']} (Kecocokan: {diagnosa_utama['kecocokan']:.0f}%)")
        print(f"Solusi Singkat   : {diagnosa_utama['solusi_singkat']}")
        
        # Opsi: Menampilkan kemungkinan lain jika pengguna mengalami gejala campuran
        if len(hasil_diagnosa) > 1:
            print("\nKemungkinan kerusakan lainnya:")
            for diagnosa_lain in hasil_diagnosa[1:]:
                 print(f"- {diagnosa_lain['kerusakan']} ({diagnosa_lain['kecocokan']:.0f}%)")

    print("="*70)

if __name__ == "__main__":
    main()