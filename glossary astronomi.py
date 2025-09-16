# glossary_astronomi.py

# Kamus istilah astronomi
glossary = {
    "Astronomi": "Ilmu yang mempelajari benda-benda langit dan fenomena luar angkasa.",
    "Bintang": "Benda langit yang memancarkan cahaya sendiri melalui reaksi nuklir di intinya.",
    "Planet": "Benda langit yang mengorbit bintang, tidak memancarkan cahaya sendiri.",
    "Galaksi": "Kumpulan bintang, gas, debu, dan materi gelap yang terikat oleh gravitasi.",
    "Tata Surya": "Sistem yang terdiri atas Matahari dan semua benda langit yang mengorbitnya.",
    "Nebula": "Awan besar gas dan debu di angkasa tempat lahirnya bintang baru.",
    "Lubang Hitam": "Objek dengan gravitasi sangat kuat sehingga cahaya pun tidak bisa lolos.",
    "Asteroid": "Batu kecil atau benda padat yang mengorbit Matahari, biasanya di sabuk asteroid.",
    "Komet": "Benda langit kecil dengan inti es dan debu yang menghasilkan ekor saat dekat Matahari.",
    "Supernova": "Ledakan besar pada akhir kehidupan bintang masif."
}

def tampilkan_glossary():
    print("=== GLOSSARY ASTRONOMI ===")
    for istilah, definisi in glossary.items():
        print(f"\n{istilah}:\n  {definisi}")

def cari_istilah():
    kata = input("\nMasukkan istilah yang ingin dicari: ").strip().title()
    if kata in glossary:
        print(f"\n{kata}: {glossary[kata]}")
    else:
        print("\nIstilah tidak ditemukan dalam glossary.")

# Menu interaktif
while True:
    print("\nMenu:")
    print("1. Tampilkan semua glossary")
    print("2. Cari istilah")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        tampilkan_glossary()
    elif pilihan == "2":
        cari_istilah()
    elif pilihan == "3":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
