import tkinter as tk
from tkinter import messagebox

MIN_CONFIDENT_MATCH = 34.0

def build_knowledge_base():
    return {
        "RAM Rusak": {
            "gejala": [
                "Terdengar bunyi beep berulang saat dinyalakan",
                "Sering mengalami Blue Screen (BSOD)",
                "Layar blank hitam tapi mesin menyala",
            ],
            "solusi_singkat": "Cabut RAM, bersihkan pin dengan penghapus, lalu pasang kembali.",
        },
        "Power Supply (PSU) Lemah": {
            "gejala": [
                "Komputer mati tiba-tiba saat digunakan",
                "Komputer sering restart sendiri tanpa peringatan",
                "Terdengar suara letupan atau bau gosong",
            ],
            "solusi_singkat": "Cek kabel power; bila sering mati mendadak, ganti PSU.",
        },
        "Overheat (Prosesor)": {
            "gejala": [
                "Kipas berputar sangat kencang dan berisik",
                "Suhu casing/laptop terasa sangat panas",
                "Komputer mati saat menjalankan aplikasi/game berat",
            ],
            "solusi_singkat": "Bersihkan kipas/heatsink dan ganti thermal paste.",
        },
        "VGA Bermasalah": {
            "gejala": [
                "Layar menampilkan garis-garis (artefak)",
                "Warna pada layar terlihat aneh/pudar",
                "Tidak ada tampilan di monitor meski indikator nyala",
            ],
            "solusi_singkat": "Update driver VGA dan cek kabel monitor.",
        },
        "Hardisk Corrupt": {
            "gejala": [
                "Proses booting dan loading aplikasi sangat lambat",
                "Terdengar bunyi 'klik' atau suara kasar dari dalam PC",
                "Muncul pesan 'Disk Boot Failure' atau 'No Bootable Device'",
            ],
            "solusi_singkat": "Segera backup data dan pertimbangkan ganti ke SSD.",
        },
        "Motherboard Rusak": {
            "gejala": [
                "Komputer tidak merespon saat tombol power ditekan",
                "Terdengar bunyi beep panjang atau pola beep tertentu saat dinyalakan",
                "Perangkat keras lain (seperti RAM, VGA) sudah dicek dan berfungsi baik",
            ],
            "solusi_singkat": "Bawa ke teknisi untuk pemeriksaan lebih lanjut; kemungkinan perlu ganti motherboard.",
        },
    }

def collect_unique_symptoms(knowledge_base):
    semua_gejala = []
    for data in knowledge_base.values():
        for gejala in data["gejala"]:
            if gejala not in semua_gejala:
                semua_gejala.append(gejala)
    return semua_gejala

def diagnose(knowledge_base, gejala_dialami):
    hasil_diagnosa = []
    for kerusakan, data in knowledge_base.items():
        cocok = sum(1 for g in data["gejala"] if g in gejala_dialami)
        if cocok > 0:
            persentase = (cocok / len(data["gejala"])) * 100
            if persentase >= 67:
                tingkat_keyakinan = "Tinggi"
            elif persentase >= 34:
                tingkat_keyakinan = "Sedang"
            else:
                tingkat_keyakinan = "Rendah"
            hasil_diagnosa.append(
                {
                    "kerusakan": kerusakan,
                    "kecocokan": persentase,
                    "jumlah_gejala_cocok": cocok,
                    "total_gejala": len(data["gejala"]),
                    "tingkat_keyakinan": tingkat_keyakinan,
                    "solusi_singkat": data["solusi_singkat"],
                }
            )
    hasil_diagnosa.sort(key=lambda x: x["kecocokan"], reverse=True)
    return hasil_diagnosa

class SistemPakarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Komputer")
        self.knowledge_base = build_knowledge_base()
        self.semua_gejala = collect_unique_symptoms(self.knowledge_base)
        self.var_gejala = {}

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER/LAPTOP",
            font=("Segoe UI", 11, "bold"),
        )
        title.pack(pady=(10, 6))

        info = tk.Label(
            self.root,
            text="Pilih gejala yang Anda alami, lalu klik Diagnosa.",
            font=("Segoe UI", 9),
        )
        info.pack(pady=(0, 10))

        frame_gejala = tk.Frame(self.root)
        frame_gejala.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        canvas = tk.Canvas(frame_gejala, highlightthickness=0)
        scrollbar = tk.Scrollbar(frame_gejala, orient="vertical", command=canvas.yview)
        daftar_gejala = tk.Frame(canvas)

        daftar_gejala.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )

        canvas.create_window((0, 0), window=daftar_gejala, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for gejala in self.semua_gejala:
            var = tk.BooleanVar(value=False)
            cb = tk.Checkbutton(
                daftar_gejala,
                text=gejala,
                variable=var,
                anchor="w",
                justify="left",
                wraplength=520,
            )
            cb.pack(fill="x", anchor="w")
            self.var_gejala[gejala] = var

        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=(0, 10))

        btn_diagnosa = tk.Button(frame_btn, text="Diagnosa", command=self.on_diagnose)
        btn_diagnosa.pack(side="left", padx=5)

        btn_reset = tk.Button(frame_btn, text="Reset", command=self.on_reset)
        btn_reset.pack(side="left", padx=5)

        self.text_hasil = tk.Text(self.root, height=8, width=70, wrap="word")
        self.text_hasil.pack(padx=10, pady=(0, 10))
        self.text_hasil.configure(state="disabled")

    def on_diagnose(self):
        gejala_dialami = [g for g, v in self.var_gejala.items() if v.get()]

        if not gejala_dialami:
            messagebox.showinfo(
                "Info",
                "Anda belum memilih gejala apa pun. Silakan pilih gejala terlebih dahulu.",
            )
            return

        hasil_diagnosa = diagnose(self.knowledge_base, gejala_dialami)

        if not hasil_diagnosa:
            output = (
                "Kerusakan Tidak Diketahui.\n"
                "Solusi: Gejala tidak cocok dengan database kami.\n"
                "Coba bawa ke tempat servis terdekat."
            )
        elif hasil_diagnosa[0]["kecocokan"] < MIN_CONFIDENT_MATCH:
            output = (
                "Kerusakan Belum Dapat Dipastikan.\n"
                "Solusi: Gejala yang dipilih masih terlalu umum atau kurang spesifik.\n"
                "Tambahkan gejala lain agar hasil diagnosa lebih akurat."
            )
        else:
            diagnosa_utama = hasil_diagnosa[0]
            lines = [
                "HASIL DIAGNOSA",
                f"Diagnosa Utama: {diagnosa_utama['kerusakan']} ",
                f"Kecocokan: {diagnosa_utama['kecocokan']:.0f}%",
                f"Tingkat Keyakinan: {diagnosa_utama['tingkat_keyakinan']}",
                f"Gejala Cocok: {diagnosa_utama['jumlah_gejala_cocok']} dari {diagnosa_utama['total_gejala']}",
                f"Solusi Singkat: {diagnosa_utama['solusi_singkat']}",
            ]
            if len(hasil_diagnosa) > 1:
                lines.append("")
                lines.append("Kemungkinan lain:")
                for diagnosa_lain in hasil_diagnosa[1:4]:
                    lines.append(
                        f"- {diagnosa_lain['kerusakan']} ({diagnosa_lain['kecocokan']:.0f}%, {diagnosa_lain['tingkat_keyakinan']})"
                    )
            output = "\n".join(lines)

        self.text_hasil.configure(state="normal")
        self.text_hasil.delete("1.0", tk.END)
        self.text_hasil.insert(tk.END, output)
        self.text_hasil.configure(state="disabled")

    def on_reset(self):
        for var in self.var_gejala.values():
            var.set(False)
        self.text_hasil.configure(state="normal")
        self.text_hasil.delete("1.0", tk.END)
        self.text_hasil.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("640x560")
    app = SistemPakarGUI(root)
    root.mainloop()