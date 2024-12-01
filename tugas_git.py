data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

# 1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
for i, j in data_panen.items():
    print(i, j)

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
jagung_lokasi_2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"\nJumlah panen jagung lokasi 2: {jagung_lokasi_2}") 

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi_3 = data_panen["lokasi3"]["nama_lokasi"]
print(f"\nNama lokasi dari lokasi 3: {nama_lokasi_3}")

# 4. Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda
# 5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi
# 6. Buat Percabangan Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus. Jika tidak, maka lokasi tersebut dalam kondisi baik.
for i, j in data_panen.items():
    lokasi = i
    padi = j["hasil_panen"]["padi"]
    kedelai = j["hasil_panen"]["kedelai"]
    jumlah_hasil_panen = padi + kedelai
    print(f"\n{lokasi} padi: {padi} kedelai: {kedelai}")
    print(f"Jumlah hasil panen padi dan kedelai {lokasi} adalah {jumlah_hasil_panen}")

    if padi > 1300 or kedelai > 800:
        print(f"{lokasi}  memerlukan perhatian khusus.")
    else:
        print(f"{lokasi} dalam kondisi baik.")
