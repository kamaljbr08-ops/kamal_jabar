from datetime import datetime  #import library datetime untuk mencatat waktu

# Variabel untuk meminta input Jumlah dan Pencatat waktu
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
log = datetime.now().strftime("Data disimpan pada tanggal %Y-%m-%d dan pada jam %H:%M\n")

with open('rekapnilai.txt', 'w') as file:
    for jumlah in range(jumlah_mahasiswa):
        nama = input(f"Masukan nama mahasiswa ke-{jumlah + 1}: ")
        tugas = float(input(f"Nilai Tugas {nama}:"))
        uts = float(input(f"Nilai UTS {nama}:"))
        uas = float(input(f"Nilai UAS {nama}:"))
        
        file.write(f"{nama}, {tugas}, {uts}, {uas}\n")
        
print("\n Selamat 🥳🎉!, Data berhasil disimpan🫂")

print("\n === Rekap Nilai Mahasiswa ===")
print(f"{'Nama':<20} {'Tugas':<10} {'UTS':<10} {'UAS':<10} {'Rata2':<10}")

with open('rekapnilai.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("Data disimpan"):  # Lewati baris log atau kosong
            continue
        try:
            nama, tugas, uts, uas = line.split(',')
            rata2 = (float(tugas.strip()) + float(uts.strip()) + float(uas.strip())) / 3
            print(f"{nama.strip():<20} {float(tugas.strip()):<10.0f} "
                  f"{float(uts.strip()):<10.0f} {float(uas.strip()):<10.0f} {rata2:<10.2f}")
        except ValueError:
            print(f"Peringatan: Format data tidak valid pada baris: {line}")
        
with open('rekapnilai.txt', 'a') as file:
    file.write(log)