import soal1 #Mengimpor modul Soal1 untuk mengakses variabel biodata
from datetime import datetime #import library datetime untuk mencatat waktu

# Fungsi utama program
def main():
   
   # Mengakses variabel biodata dari modul Soal1
    nama = soal1.nama
    nim = soal1.nim
    prodi = soal1.Prodi

    
    biodata = f"Nama: {nama}\nNIM: {nim}\nProdi: {prodi}\n"

    
    log = datetime.now().strftime("Data diakses pada tanggal %Y-%m-%d dan pada jam %H:%M\n")

    # Menyimpan biodata beserta log waktu ke dalam file
    with open('biodata.txt', 'a') as log_file:
        log_file.write(biodata)
        log_file.write(log)

    # Output konfirmasi data berhasil disimpan
    with open('biodata.txt', 'r') as file:
        for line in file:
            print(line, end='')  

if __name__== "_main_":
    main()