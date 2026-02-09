import time
import sys
import random

class GameMisteri:
    def __init__(self):
        self.pemain_nama = ""
        self.peran = ""
        self.energi = 100
        self.nyawa = 5  # Sistem nyawa - game over jika mencapai 0
        self.petunjuk_terkumpul = []
        self.waktu_tersisa = 48  # 48 jam untuk menyelesaikan misi
        self.ascii_sword = (
            "\n"
            "           />_________________________________\n"
            "  [########[]_________________________________>\n"
            "           \\\\                         \n"
        )
        self.ascii_skull = """

             .-''''-.
            /  .--.  \
           /  /    \  \
           |  |    |  |
           |  |.-""-.|  |
          ///`.::::.`\\
         ||| ::/  \:: |||
         ||; ::\__/:: ;||
          \\ '::::' ///
           `=':-..-'=`
"""

    def tampilkan_cerita(self, teks, jenis="normal", kecepatan=0.05):
        """
        Menampilkan teks cerita dengan efek dramatis
        jenis: 'normal' (karakter per karakter) atau 'kalimat' (jeda antar kalimat)
        kecepatan: berapa detik untuk tiap karakter/kalimat
        """
        if jenis == "normal":
            # Tampilkan karakter per karakter untuk efek dramatis
            for karakter in teks:
                print(karakter, end="", flush=True)
                time.sleep(kecepatan)
            print()  # Newline di akhir
        elif jenis == "kalimat":
            # Tampilkan per kalimat dengan jeda 0.5 detik
            kalimat_list = teks.split(". ")
            for i, kalimat in enumerate(kalimat_list):
                print(kalimat + ("." if i < len(kalimat_list) - 1 else ""))
                time.sleep(0.5)
        else:
            # Default: tampilkan langsung
            print(teks)

    def hitung_keberuntungan(self, konteks=None):
        """Mengembalikan modifier keberuntungan berbasis peran dan faktor acak"""
        base = random.uniform(0, 1)
        role_bonus = 0.0
        if self.peran == "DETEKTIF INVESTIGATOR":
            role_bonus = 0.1
        elif self.peran == "ANGGOTA TIM SAR":
            role_bonus = 0.05
        elif self.peran == "PROFILER KRIMINAL":
            role_bonus = 0.08
        # konteks bisa mengubah peluang (mis. "lokasi", "wawancara", "data")
        konteks_bonus = 0.0
        if konteks == "lokasi":
            konteks_bonus = 0.05
        elif konteks == "wawancara":
            konteks_bonus = 0.07
        elif konteks == "data":
            konteks_bonus = 0.06
        return min(base + role_bonus + konteks_bonus, 0.98)
        
    def tampilkan_status_permainan(self):
        """Menampilkan status permainan saat ini"""
        status_bar = f"❤️  NYAWA: {self.nyawa}/5 | ⚡ ENERGI: {self.energi}% | ⏰ WAKTU: {self.waktu_tersisa}h | 📊 PETUNJUK: {len(self.petunjuk_terkumpul)}"
        print("\n" + "─" * 70)
        print(status_bar)
        print("─" * 70)
    
    def kurangi_nyawa(self, jumlah=1, alasan=""):
        """Mengurangi nyawa pemain"""
        self.nyawa -= jumlah
        print(f"\n❌ KEPUTUSAN SALAH! Nyawa berkurang {jumlah}.")
        if alasan:
            print(f"   Alasan: {alasan}")
        print(f"   Nyawa tersisa: {self.nyawa}/5")
        
        if self.nyawa <= 0:
            print("\n" + "="*70)
            print("💀 GAME OVER! NYAWA HABIS!")
            print("="*70)
            print("\nKarena kelalaian investigasi Anda, kasus ini tidak terpecahkan.")
            print("Korban tidak mendapat keadilan dan keluarganya terus dalam penderitaan.")
            print("\n[Permainan berakhir. Silakan coba lagi dan buat keputusan lebih baik!]")
            print(self.ascii_skull)
            time.sleep(2)
            return False
        return True
    
    def tambah_poin(self, jumlah=1, alasan=""):
        """Menambah energi atau bonus ketika keputusan benar"""
        self.energi = min(self.energi + jumlah, 100)
        print(f"\n✓ KEPUTUSAN TEPAT! Energi bertambah {jumlah}.")
        if alasan:
            print(f"   {alasan}")
        print(f"   Energi sekarang: {self.energi}%")
    
    def tampilkan_loading(self):
        """Menampilkan efek loading yang menarik"""
        print("\n", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        time.sleep(0.5)
        print("\n")
    
    def tampilkan_intro(self):
        """Menampilkan intro game yang atmospheric"""
        print("=" * 70)
        print("╔" + "=" * 68 + "╗")
        print("║" + " " * 15 + "🔍 MISTERI PETUALANGAN 🔍" + " " * 27 + "║")
        print("║" + " " * 68 + "║")
        print("║" + " " * 10 + "Sebuah Kasus Menunggu untuk Dipecahkan..." + " " * 15 + "║")
        print("╚" + "=" * 68 + "╝")
        print("=" * 70)
        
        time.sleep(1)
        print("\n📍 LOKASI: Kantor Polda Regional")
        print("⏰ WAKTU: Hari Jumat, 06.00 Pagi")
        time.sleep(1)
        print("\nAnda memasuki ruang briefing dengan penuh antisipasi.")
        print("Kepala Polres sudah menunggu Anda bersama dengan tim SAR handal.")
        self.tampilkan_loading()
        print("Kepala: 'Terimakasih telah datang. Kami memiliki DUA KASUS URGENT")
        print("         yang membutuhkan perhatian khusus Anda...'")

        # Cerita yang lebih dramatis
        time.sleep(1)
        self.tampilkan_cerita("", "kalimat")  # Jeda
        self.tampilkan_cerita("\n📋 BRIEFING RESMI DIMULAI...", "normal", 0.02)
        time.sleep(0.5)
        self.tampilkan_cerita("\nKepala Polres membuka map detektor di atas meja. Wajahnya terlihat cemas dan lelah.", "kalimat")
        self.tampilkan_cerita("'Dalam tiga hari terakhir, kami menerima DUA laporan hilang yang sangat urgent.'", "kalimat")
        self.tampilkan_cerita("'Satu adalah pencarian orang hilang dengan indikasi kuat penculikan.'", "kalimat")
        self.tampilkan_cerita("'Satunya lagi adalah kasus kematian yang dicatat sebagai bunuh diri, namun kami ragu dengan kesimpulan itu.'", "kalimat")
        time.sleep(1)
        self.tampilkan_cerita("Beliau memandang Anda dengan tatapan yang penuh harapan.", "kalimat")
        self.tampilkan_cerita("'Kami membutuhkan investigator terbaik untuk kasus-kasus ini. Waktu adalah faktor kritis.'", "kalimat")
        self.tampilkan_cerita("'Jiwa-jiwa manusia bergantung pada keputusan dan tindakan Anda mulai dari sini.'", "kalimat")
        self.tampilkan_loading()
    
    def pilih_peran(self):
        """Memilih peran dalam tim investigasi"""
        print("\n" + "=" * 70)
        print("🎭 PILIH PERAN ANDA (Ini Mempengaruhi Kemampuan Khusus)")
        print("=" * 70)
        print("\n1️⃣  DETEKTIF INVESTIGATOR")
        print("    └─ Spesialisasi: Analisis bukti & Wawancara saksi")
        print("       Kemampuan: +30% akurasi dalam menggali informasi")
        print("\n2️⃣  ANGGOTA TIM SAR (Search And Rescue)")
        print("    └─ Spesialisasi: Tracking & Eksplorasi lapangan")
        print("       Kemampuan: +25% jangkauan area investigasi")
        print("\n3️⃣  PROFILER KRIMINAL")
        print("    └─ Spesialisasi: Analisis psikologi & Pola perilaku")
        print("       Kemampuan: +20% memahami motivasi pelaku")
        
        while True:
            pilihan = input("\nPilih peran Anda (1/2/3): ").strip()
            if pilihan == "1":
                self.peran = "DETEKTIF INVESTIGATOR"
                print("\n✓ Anda dipilih sebagai DETEKTIF INVESTIGATOR!")
                print("  Anda akan fokus pada pengumpulan bukti dan wawancara saksi.")
                return
            elif pilihan == "2":
                self.peran = "ANGGOTA TIM SAR"
                print("\n✓ Anda dipilih sebagai ANGGOTA TIM SAR!")
                print("  Anda akan memimpin operasi pencarian lapangan.")
                return
            elif pilihan == "3":
                self.peran = "PROFILER KRIMINAL"
                print("\n✓ Anda dipilih sebagai PROFILER KRIMINAL!")
                print("  Anda akan menganalisis perilaku dan motivasi tersangka.")
                return
            else:
                print("❌ Pilihan tidak valid! Silakan masukkan 1, 2, atau 3.")
    
    def tampilkan_kasus(self):
        """Menampilkan dua pilihan kasus utama"""
        print("\n" + "=" * 70)
        print("📋 BRIEFING KASUS - PILIH SALAH SATU DARI DUA KASUS BERIKUT")
        print("=" * 70)
        
        print("\n" + "─" * 70)
        print("🔴 KASUS 1: TEMUKAN ORANG HILANG")
        print("─" * 70)
        print("""
KORBAN: Siti Rahayu, 32 tahun | Perawat di Rumah Sakit Sentosa
HILANG: Senin, 23.30 Malam (3 hari yang lalu) dari Jalan Pendidikan

INFORMASI:
• Kebiasaan: Selalu pulang sebelum jam 22.00 malam
• Kondisi terakhir: Terlihat cemas saat keluar dari rumah sakit
• Kendaraan: Mobil Honda Jazz Biru, No. Pol B 2023 XYZ
• Telepon: Dalam kondisi MATI sejak Senin malam
• Keadaan: Tidak ada catatan terlilit utang atau masalah keluarga

🔎 TUJUAN INVESTIGASI:
  ► Menemukan keberadaan Siti Rahayu (hidup/meninggal)
  ► Mengungkap alasan hilangnya dan kemana dia pergi
  ► Menyelidiki apakah ada keterlibatan pihak ketiga
  ► Mengumpulkan timeline pergerakan korban
""")
        
        print("─" * 70)
        print("⚫ KASUS 2: MENYELIDIKI KASUS BUNUH DIRI (?)") 
        print("─" * 70)
        print("""
KORBAN: Ahmad Wijaya, 45 tahun | Manager Keuangan PT. Global Invest
STATUS: Meninggal Rabu pagi, ditemukan tergantung di rumahnya
KEMATIAN: Sekitar jam 03.00 pagi - dilaporkan oleh asisten rumah tangga

INFORMASI MENCURIGAKAN:
• Laporan polisi menyebutkan: Bunuh Diri
• NAMUN: Ditemukan bukti fisik yang tidak sesuai (luka-luka aneh)
• Catatan: Tidak ada surat wasiat atau tanda-tanda depresi
• Keadaan keuangan: Stabil, bonus baru saja diterima hari sebelumnya
• Takhir berkomunikasi: Mengatakan 'saya tahu sesuatu yang besar'

🔎 TUJUAN INVESTIGASI:
  ► Membuktikan apakah ini sungguh-sungguh bunuh diri atau pembunuhan
  ► Mengungkap apa yang ingin diketahui Ahmad menjelang kematiannya
  ► Mengidentifikasi motif dan tersangka yang mungkin
  ► Menemukan kronologi sebenarnya dari kejadian malam itu
""")
        
        print("─" * 70)
        self.tampilkan_status_permainan()
        print(f"👤 PERAN ANDA: {self.peran}")
        print("=" * 70)
        
        self.pilih_kasus()
    
    def pilih_kasus(self):
        """Proses pemilihan kasus"""
        while True:
            pilihan = input("\n🎯 Pilih kasus mana yang ingin Anda selidiki? (1/2) atau (K=Kembali): ").strip().upper()
            
            if pilihan == "1":
                print("\n" + "="*70)
                print("✓ Anda memilih KASUS 1: TEMUKAN ORANG HILANG")
                print("="*70)
                self.tampilkan_loading()
                if not self.mulai_kasus_orang_hilang():
                    return  # Game Over
                break
            elif pilihan == "2":
                print("\n" + "="*70)
                print("✓ Anda memilih KASUS 2: MENYELIDIKI KASUS BUNUH DIRI")
                print("="*70)
                self.tampilkan_loading()
                if not self.mulai_kasus_bunuh_diri():
                    return  # Game Over
                break
            elif pilihan == "K":
                self.tampilkan_kasus()
                break
            else:
                print("❌ Pilihan tidak valid! Masukkan 1, 2, atau K untuk kembali.")
    
    def mulai_kasus_orang_hilang(self):
        """Memulai investigasi kasus orang hilang"""
        print("\n🚗 Anda tiba di Jurnalis Polisi Cabang Kelapa Gading...")
        print("   Petugas berpatroli mengarahkan Anda ke tempat kejadiannya.")
        self.tampilkan_loading()
        
        print("\n📍 LOKASI KEJADIAN: Jalan Pendidikan, Kelapa Gading")
        print("   Lebar jalan: 12 meter, lampu jalan redup")
        print("   Area parkir terdekat: 50 meter dari lokasi terakhir terlihat")
        print("\n🔍 PETUNJUK AWAL DITEMUKAN:")
        print("   • Satu sandal wanita berwarna merah - cocok dengan laporan")
        print("   • Bekas rem mobil yang panjang di aspal (kemungkinan pengereman darurat)")
        print("   • Noda darah di tepi jalan (sedang dianalisis)")

        # Cerita dramatis lebih detail
        time.sleep(1)
        self.tampilkan_cerita("\n" + "="*70, "normal", 0)
        self.tampilkan_cerita("⏰ TIMELINE PERISTIWA", "normal", 0.02)
        self.tampilkan_cerita("="*70, "normal", 0)

        self.tampilkan_cerita("\n📅 SENIN KEMARIN, MALAM PUKUL 23:15", "normal", 0.02)
        time.sleep(0.5)
        self.tampilkan_cerita("Siti Rahayu, seorang perawat muda, keluar dari Rumah Sakit Sentosa setelah shift malam yang panjang.", "kalimat")
        self.tampilkan_cerita("Dia terlihat cemas menurut laporan rekan kerjanya.", "kalimat")
        self.tampilkan_cerita("Setelah itu, Siti hilang begitu saja dari radar publik.", "kalimat")

        time.sleep(1)
        self.tampilkan_cerita("\n🔴 SEKARANG INI - 3 HARI KEMUDIAN, PUKUL 09:30 PAGI", "normal", 0.02)
        time.sleep(0.5)
        self.tampilkan_cerita("Keluarganya menjadi panik dan melaporkan ke polisi.", "kalimat")
        self.tampilkan_cerita("Tim SAR mencari dan menemukan jejak-jejak yang mengerikan di lokasi terakhir dia terlihat.", "kalimat")
        self.tampilkan_cerita("Sekarang, giliran Anda untuk mengungkap misteri ini sebelum terlambat.", "kalimat")

        time.sleep(2)
        print("\n" + "="*70)
        print("🎯 APA LANGKAH INVESTIGASI PERTAMA ANDA?")
        print("="*70)
        print("\n1️⃣  Memeriksa Lokasi Kejadian Lebih Dekat")
        print("    └─ Mencari bukti fisik di sekitarnya")
        print("\n2️⃣  Mewawancarai Keluarga Korban")
        print("    └─ Menggali informasi pribadi & kebiasaan Siti")
        print("\n3️⃣  Mengecek CCTV Sekitar Lokasi")
        print("    └─ Mencari rekaman atau saksi kejadian")
        
        self.tampilkan_status_permainan()
        
        while True:
            pilihan = input("\nPilihan Anda (1/2/3): ").strip()
            if pilihan in ["1", "2", "3"]:
                # cek keberuntungan untuk konteks lokasi/wawancara/data
                konteks = "lokasi" if pilihan == "1" else ("wawancara" if pilihan == "2" else "data")
                sukses = self.hitung_keberuntungan(konteks) > 0.25  # ambang dasar
                if not sukses:
                    tetap = self.kurangi_nyawa(1, "Langkah investigasi gagal - Anda kehilangan arah dan waktu")
                    if not tetap:
                        return False
                    # tetap lanjutkan menu agar pemain dapat mencoba lagi
                    continue
                return self.proses_investigasi_kasus1(pilihan)
            else:
                print("❌ Pilihan tidak valid!")
    
    def mulai_kasus_bunuh_diri(self):
        """Memulai investigasi kasus bunuh diri"""
        print("\n🏠 Anda tiba di rumah Ahmad Wijaya di perumahan Bintaro...")
        print("   Polisi sudah mengamankan lokasi TKP.")
        self.tampilkan_loading()
        
        print("\n📍 LOKASI KEJADIAN: Rumah Ahmad Wijaya, Jln. Bintaro Jaya")
        print("   Tipe rumah: Mewah, 3 lantai, perumahan tertutup")
        print("   Kondisi: Pintu depan terkunci dari dalam (aneh untuk bunuh diri)")
        print("\n🔍 PETUNJUK AWAL DITEMUKAN:")
        print("   • Korban ditemukan tergantung di ruang tidur")
        print("   • NE namun ada memar di sekitar pergelangan tangan (tanda perlawanan?)")
        print("   • Meja kerja berantakan & laptop dalam kondisi hidup (browser terbuka)")
        print("   • Ditemukan buklet 'Asuransi Jiwa' di meja nakas")
        print("   • Kesan-kesan kaki ukuran lain ditemukan di lantai")

        # Cerita dramatis lebih detail
        time.sleep(1)
        self.tampilkan_cerita("\n" + "="*70, "normal", 0)
        self.tampilkan_cerita("⚠️  DETAIL KASUS YANG MENCURIGAKAN", "normal", 0.02)
        self.tampilkan_cerita("="*70, "normal", 0)

        self.tampilkan_cerita("\n👤 KORBAN: Ahmad Wijaya, 45 tahun", "normal", 0.02)
        self.tampilkan_cerita("Posisi: Manager Keuangan PT. Global Invest - Perusahaan investasi multinasional besar", "kalimat")
        time.sleep(0.5)

        self.tampilkan_cerita("\n📅 RABU DINI HARI, SEKITAR JAM 03:00", "normal", 0.02)
        time.sleep(0.5)
        self.tampilkan_cerita("Asisten rumah tangga Ahmad menemukan majikannya tergantung di ruang tidur pribadi.", "kalimat")
        self.tampilkan_cerita("Cerita resminya adalah bunuh diri yang disebabkan depresi dan tekanan kerja.", "kalimat")
        time.sleep(0.5)

        self.tampilkan_cerita("\n🔴 NAMUN ADA YANG SANGAT ANEH...", "normal", 0.02)
        time.sleep(0.5)
        self.tampilkan_cerita("Ahmad tidak menunjukkan tanda-tanda depresi di hari-hari sebelumnya.", "kalimat")
        self.tampilkan_cerita("Dia bahkan baru saja menerima bonus besar dan promosi.", "kalimat")
        self.tampilkan_cerita("Yang paling mengganggu: ada memar-memar di tubuhnya yang TIDAK konsisten dengan bunuh diri.", "kalimat")
        self.tampilkan_cerita("Ada jejak tangan lain di lehernya, dan tanda-tanda perlawanan di pergelangan tangannya.", "kalimat")
        time.sleep(1)

        self.tampilkan_cerita("\n❓ PERTANYAAN BESAR", "normal", 0.02)
        self.tampilkan_cerita("Apakah Ahmad benar-benar bunuh diri? Atau ini adalah pembunuhan yang dirancang sedemikian rupa?", "kalimat")
        self.tampilkan_cerita("Apa yang ingin Ahmad lakukan sebelum dia mati? Email terakhirnya penuh dengan kode-kode aneh.", "kalimat")

        time.sleep(2)
        print("\n" + "="*70)
        print("🎯 APA LANGKAH INVESTIGASI PERTAMA ANDA?")
        print("="*70)
        print("\n1️⃣  Memeriksa Posisi Mayat & Tanda-Tanda Fisik")
        print("    └─ Menganalisis bukti medis & kronologi kematian")
        print("\n2️⃣  Menganalisis Data dari Laptop & Telepon")
        print("    └─ Mengecek email, pesan, & riwayat browsing")
        print("\n3️⃣  Mewawancarai Orang-Orang Terdekat (Keluarga, Kolega)")
        print("    └─ Mencari motif & tekanan yang dialami Ahmad")
        
        self.tampilkan_status_permainan()
        
        while True:
            pilihan = input("\nPilihan Anda (1/2/3): ").strip()
            if pilihan in ["1", "2", "3"]:
                konteks = "lokasi" if pilihan == "1" else ("data" if pilihan == "2" else "wawancara")
                sukses = self.hitung_keberuntungan(konteks) > 0.25
                if not sukses:
                    tetap = self.kurangi_nyawa(1, "Analisa Anda meleset dan menimbulkan konsekuensi")
                    if not tetap:
                        return False
                    continue
                return self.proses_investigasi_kasus2(pilihan)
            else:
                print("❌ Pilihan tidak valid!")
    
    def proses_investigasi_kasus1(self, pilihan):
        """Memproses pilihan investigasi kasus 1"""
        print("\n" + "="*70)
        if pilihan == "1":
            print("🔎 MEMERIKSA LOKASI KEJADIAN LEBIH DEKAT")
            print("="*70)
            print("\nAnda dengan teliti memeriksa area sekitar Jalan Pendidikan...")
            self.tampilkan_loading()
            # peluang keberuntungan kecil menambah kemungkinan temuan ekstra
            print("✓ Petunjuk baru ditemukan!")
            print("  • Menemukan catatan tangan di dalam semak: 'Jangan percaya siapapun'")
            print("  • Ada jejak ban mobil yang berbeda dari mobil Siti (kemungkinan mobil lain)")
            print("  • Warna cat hitam menempel di batu besar (dari mobil penabrak?)")
            self.petunjuk_terkumpul.append("Catatan misterius & bukti mobilitas ganda")
            self.tambah_poin(10, "Pendekatan investigasi langsung sangat efektif!")
            if random.random() < 0.25:
                self.tampilkan_cerita("Tambahan: Anda menemukan serpihan kain dengan aroma parfum mahal.", "kalimat")
                self.petunjuk_terkumpul.append("Serpihan kain bermerek & petunjuk parfum")

        elif pilihan == "2":
            print("👨‍👩‍👧 MEWAWANCARAI KELUARGA KORBAN")
            print("="*70)
            print("\nAnda tiba di rumah keluarga Siti untuk mewawancara...")
            self.tampilkan_loading()
            print("📞 Ibu Siti (Ibu Kartini, 65 tahun) menangis:")
            print("  'Siti mengatakan ada masalah di pekerjaan. Dia disuruh")
            print("   mengurus sesuatu yang tidak boleh dibuka orang lain.'")
            print("\n   Lalu dia terima telepon misterius dari nomor tidak terdaftar.")
            print("   Setelah itu Siti bilang harus ke suatu tempat penting.'")
            self.petunjuk_terkumpul.append("Masalah di pekerjaan & telepon misterius")
            self.tambah_poin(10, "Wawancara keluarga mengungkap motif penting!")
            if random.random() < 0.2:
                self.tampilkan_cerita("Tambahan: Ibu mengingat potongan suara yang aneh di telepon - suara laki-laki dengan aksen asing.", "kalimat")
                self.petunjuk_terkumpul.append("Potongan suara telepon: aksen asing")

        elif pilihan == "3":
            print("📹 MENGECEK CCTV SEKITAR LOKASI")
            print("="*70)
            print("\nAnda meminta rekaman CCTV dari merchant terdekat...")
            self.tampilkan_loading()
            print("✓ Rekaman CCTV ditemukan!")
            print("  • 23:15 - Siti terlihat berjalan sendirian (tampak gelisah)")
            print("  • 23:22 - Mobil misterius berbentuk sedan hitam berhenti di dekatnya")
            print("  • 23:24 - Siti naik ke mobil itu (terlihat dipaksa?)")
            print("  • 23:25 - Mobil itu menghilang ke arah Tol Jagorawi")
            self.petunjuk_terkumpul.append("CCTV: Bukti penculikan potensial & plat nomor sebagian")
            self.tambah_poin(15, "Bukti visual CCTV adalah kunci untuk breakthrough!")
            if random.random() < 0.3:
                self.tampilkan_cerita("Tambahan: Seorang pejalan kaki merekam dengan ponsel - terlihat logo perusahaan logistic di pintu mobil.", "kalimat")
                self.petunjuk_terkumpul.append("Logo perusahaan logistic pada mobil misterius")

        print(f"\n📊 Petunjuk terkumpul: {len(self.petunjuk_terkumpul)}")
        print(f"⏰ Waktu tersisa: {self.waktu_tersisa} jam")
        self.tampilkan_status_permainan()
        # Cek apakah sudah cukup petunjuk untuk 'menang'
        if len(self.petunjuk_terkumpul) >= 4:
            self.tampilkan_cerita("\nAnda berhasil mengumpulkan cukup bukti untuk membongkar kasus ini!", "kalimat")
            print(self.ascii_sword)
            self.tampilkan_cerita("SELAMAT! Anda membawa kebenaran ke permukaan dan menyelamatkan korban.", "kalimat")
            return False
        print("\n[Investigasi akan dilanjutkan pada tahap berikutnya...]")
        return True
    
    def proses_investigasi_kasus2(self, pilihan):
        """Memproses pilihan investigasi kasus 2"""
        print("\n" + "="*70)
        if pilihan == "1":
            print("💀 MEMERIKSA POSISI MAYAT & TANDA-TANDA FISIK")
            print("="*70)
            print("\nAnda melakukan pemeriksaan bekerja sama dengan forensik...")
            self.tampilkan_loading()
            print("⚠️  TEMUAN MENCURIGAKAN!")
            print("  • Memar di pergelangan tangan: PERTANDA PERLAWANAN")
            print("  • Posisi tali: Tidak konsisten dengan bunuh diri (arah aneh)")
            print("  • Tanda lecet di leher: Ada bekas jepitan KUAT sebelum penggantungan")
            print("  • Waktu kematian: Estimasi 02:00-03:30 (tidak sesuai laporan awal)")
            self.petunjuk_terkumpul.append("Bukti PEMBUNUHAN tersamar sebagai bunuh diri")
            self.tambah_poin(15, "Analisis forensik membuktikan ini bukan bunuh diri!")
            if random.random() < 0.2:
                self.tampilkan_cerita("Tambahan: Jejak sidik jari samar ditemukan di bingkai pintu - milik seseorang yang tidak tercatat.", "kalimat")
                self.petunjuk_terkumpul.append("Sidik jari asing pada bingkai pintu")
            
                        # Narasi cerita detail
                        time.sleep(1)
                        self.tampilkan_cerita("\n" + "─"*70, "normal", 0)
                        self.tampilkan_cerita("Ruang tidur Ahmad sunyi dan menyeramkan. Lampu forensik menerangi setiap sudut.", "kalimat")
                        self.tampilkan_cerita("Dokter forensik membuka jubah mayat Ahmad perlahan-lahan dengan sikap profesional namun serius.", "kalimat")
                        time.sleep(0.5)
            
                        self.tampilkan_cerita("'Lihatlah di sini,' kata ahli forensik sambil menunjuk ke leher Ahmad.", "kalimat")
                        self.tampilkan_cerita("'Ada DUA jenis memar di leher. Yang pertama adalah dari jepitan tangan - SANGAT KERAS.'", "kalimat")
                        time.sleep(0.5)
            
                        self.tampilkan_cerita("'Memar kedua adalah dari tali. Tapi WAKTU TERJADINYA BERBEDA.'", "kalimat")
                        self.tampilkan_cerita("'Ahmad pertama-tama dia DICINCANG oleh seseorang. Baru setelah itu, talinya ditambahkan.'", "kalimat")
                        time.sleep(1)
            
                        self.tampilkan_cerita("\nPergelangan tangan Ahmad juga penuh dengan memar berbentuk TANGAN - bukti nyata perlawanan.", "kalimat")
                        self.tampilkan_cerita("'Orang ini melawan dengan keras sebelum meninggal. Ini TIDAK MUNGKIN bunuh diri,' kata ahli itu tegas.", "kalimat")
                        self.tampilkan_cerita("'Minimal ada DUA atau TIGA orang yang menahan Ahmad saat ini terjadi.'", "kalimat")
                        time.sleep(1)
            
                        self.tampilkan_cerita("Nafas Anda jadi berat. Kasus ini bukan hanya pembunuhan - ini PERTUNJUKAN BRUTAL.", "kalimat")
            
        elif pilihan == "2":
            print("💻 MENGANALISIS DATA LAPTOP & TELEPON")
            print("="*70)
            print("\nAnda bekerja dengan IT forensik untuk menganalisis perangkat...")
            self.tampilkan_loading()
            print("✓ DATA PENTING DITEMUKAN!")
            print("  • Email rahasia ke 'MysteryContact': 'Saya punya bukti korupsi PT Global'")
            print("  • Chat terenkripsi (Telegram): Perjanjian untuk bertemu SECRET MEETING")
            print("  • Search history: 'Cara melaporkan korupsi ke KPK' & 'Perlindungan whistle blower'")
            print("  • Foto tertanam di laptop: Ahmad bersama pejabat tinggi (sedang transaksi uang)")
            self.petunjuk_terkumpul.append("Bukti korupsi besar & niat Ahmad untuk jadi whistleblower")
            self.tambah_poin(20, "Bukti digital mengungkap jaringan korupsi yang luas!")
            if random.random() < 0.3:
                self.tampilkan_cerita("Tambahan: Terdapat file terenkripsi berlabel 'DO NOT OPEN'.", "kalimat")
                self.petunjuk_terkumpul.append("File terenkripsi: DO NOT OPEN")
            
                        # Narasi cerita detail
                        time.sleep(1)
                        self.tampilkan_cerita("\n" + "─"*70, "normal", 0)
                        self.tampilkan_cerita("Anda dan tech specialist duduk di ruang dark room yang dilengkapi server dan monitor besar.", "kalimat")
                        self.tampilkan_cerita("Mereka telah berhasil men-crack enkripsi dari laptop Ahmad dan membuka file-file tersembunyi.", "kalimat")
                        time.sleep(0.5)
            
                        self.tampilkan_cerita("'Ini... gila,' bisik tech specialist sambil membaca email-email Ahmad.", "kalimat")
                        self.tampilkan_cerita("'Ahmad mengirimkan email ke sebuah alamat bernama 'MysteryContact@protonmail.com'.'", "kalimat")
                        time.sleep(0.5)
            
                        self.tampilkan_cerita("Subject: 'BUKTI KORUPSI TERBESAR DI INDONESIA'", "normal", 0.02)
                        time.sleep(0.5)
            
                        self.tampilkan_cerita("Di dalam email tersebut, Ahmad menulis:", "kalimat")
                        time.sleep(0.5)
                        self.tampilkan_cerita("\n>>> 'Saya telah mengumpulkan bukti selama 5 tahun.'", "normal", 0.02)
                        self.tampilkan_cerita(">>> 'Transaksi uang haram senilai MILIARAN rupiah setiap bulannya.'", "normal", 0.02)
                        self.tampilkan_cerita(">>> 'Pejabat tinggi di pemerintah dan korporasi terlibat langsung.'", "normal", 0.02)
                        self.tampilkan_cerita(">>> 'Saya akan membuka semuanya kepada KPK dalam 48 jam ke depan. Baik atau mati.' <<<", "normal", 0.02)
                        time.sleep(1)
            
                        self.tampilkan_cerita("'Ini adalah motif pembunuhan yang PALING KUAT yang pernah saya lihat,' kata tech specialist dengan nada ngeri.", "kalimat")
                        self.tampilkan_cerita("'Ahmad menjadi ancaman bagi jaringan korupsi terbesar di negara kita.'", "kalimat")
            
        elif pilihan == "3":
            print("👥 MEWAWANCARAI ORANG-ORANG TERDEKAT")
            print("="*70)
            print("\nAnda melakukan wawancara dengan rasa mencurigai...")
            self.tampilkan_loading()
            print("📞 Istri Ahmad (Siti Nurhaliza, 42 tahun) bercerita:")
            print("  'Ahmad belakangan gelisah. Dia bilang kalau sesuatu terjadi padanya,")
            print("   jangan percaya versi resmi. Tapi dia takut berbicara lebih jauh.'")
            print("\n   Malam kejadian, dia mendengar suara gaduh & percakapan keras di tlp.")
            print("   Kemudian Ahmad tutup pintu kamar dari dalam.")
            print("\n🤔 Catatan: Istri terlihat GELISAH & kemungkinan MENYEMBUNYIKAN sesuatu")
            self.petunjuk_terkumpul.append("Istri Ahmad tahu sesuatu yang PENTING & mengkhawatirkan")
            self.tambah_poin(10, "Wawancara mengungkap kekhawatiran istri terhadap ancaman!")
            if random.random() < 0.25:
                self.tampilkan_cerita("Tambahan: Siti menyebut sebuah nama samar yang terdengar seperti 'Rudra'.", "kalimat")
                self.petunjuk_terkumpul.append("Nama samar disebut: Rudra")
            
              # Narasi cerita detail
              time.sleep(1)
              self.tampilkan_cerita("\n" + "─"*70, "normal", 0)
              self.tampilkan_cerita("Ruang interogasi sunyi. Siti Nurhaliza, istri Ahmad, duduk berseberangan dengan Anda.", "kalimat")
              self.tampilkan_cerita("Matanya merah membengkak dari menangis. Tangannya gemetar saat memegang cangkir kopi.", "kalimat")
              time.sleep(0.5)
            
              self.tampilkan_cerita("'Dua minggu sebelum Ahmad meninggal, dia sangat gelisah sekali,' Siti mulai bercerita dengan suara lemah.", "kalimat")
              self.tampilkan_cerita("'Dia tidak bisa tidur, terus-menerus menulis sesuatu di laptop, dan selalu memandang pintu seperti menunggu sesuatu.'", "kalimat")
              time.sleep(0.5)
            
              self.tampilkan_cerita("'Suatu malam, Ahmad mengambil tangan saya dan berkata dengan suara yang sangat serius:'", "kalimat")
              time.sleep(0.5)
            
              self.tampilkan_cerita("\n>>> 'Jika sesuatu terjadi padaku, jangan percaya pada laporan kepolisian yang akan mereka buat.'", "normal", 0.02)
              self.tampilkan_cerita(">>> 'Jangan percaya kepada siapapun di pemerintah. Yang harus kamu percaya hanya pada investigator yang jujur.' <<<", "normal", 0.02)
              time.sleep(1)
            
              self.tampilkan_cerita("Siti mulai menangis lebih keras. 'Dia tahu! Ahmad sudah tahu dia akan dibunuh!'", "kalimat")
              self.tampilkan_cerita("'Pada malam terakhir, saya mendengar suara pembicaraan keras di kamarnya.'", "kalimat")
              self.tampilkan_cerita("'Ada orang lain. Suara-suara yang tidak saya kenal. Ahmad berteriak - PA-PA-PA - (suara tembakan)'", "kalimat")
              self.tampilkan_cerita("Jantung Anda berhenti sejenak. BUKAN HANYA PEMBUNUHAN - INI ADALAH RENCANA MATANG.", "kalimat")
        
        print(f"\n📊 Petunjuk terkumpul: {len(self.petunjuk_terkumpul)}")
        print(f"⏰ Waktu tersisa: {self.waktu_tersisa} jam")
        self.tampilkan_status_permainan()
        if len(self.petunjuk_terkumpul) >= 4:
            self.tampilkan_cerita("\nAnda berhasil mengumpulkan cukup bukti untuk membongkar kasus ini!", "kalimat")
            print(self.ascii_sword)
            self.tampilkan_cerita("SELAMAT! Anda membawa kebenaran ke permukaan dan menyelamatkan korban.", "kalimat")
            return False
        print("\n[Investigasi akan dilanjutkan pada tahap berikutnya...]")
        return True

def game_utama():
    """Fungsi utama permainan"""
    while True:
        game = GameMisteri()

        # Intro awal
        game.tampilkan_intro()

        # Input nama pemain
        nama = input("\n🎭 Siapa nama Anda, para investigator? ")
        game.pemain_nama = nama if nama.strip() else "Detective Unknown"

        print(f"\n➜ Selamat datang, {game.pemain_nama}!")
        time.sleep(1)

        # Pilih peran
        game.pilih_peran()
        time.sleep(1)

        # Tampilkan dua pilihan kasus
        game.tampilkan_kasus()

        # Setelah sesi kasus selesai (menang/kalah atau berhenti), tanyakan apakah mau main lagi
        while True:
            ulang = input("\nMain lagi? (y/n): ").strip().lower()
            if ulang == 'y':
                break  # restart loop utama, membuat game baru
            elif ulang == 'n':
                print("\nTerima kasih telah bermain. Sampai jumpa di kasus berikutnya!")
                return
            else:
                print("Masukkan y atau n.")

if __name__ == "__main__":
    game_utama()