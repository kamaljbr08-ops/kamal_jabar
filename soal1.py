import os

os.system('cls' if os.name == 'nt' else 'clear')
nama = input("Masukan Nama:")
nim = input("Masukan NIM:")
Prodi = input("Masukan Prodi:")

with open('biodata.txt','w') as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Prodi: {Prodi}\n")
print(f"Halo {nama}, biodata kamu telah disimpan, Terimakasih!")
print(" \n")
with open('biodata.txt','r') as file:
    print(f"\nIsi biodata {nama}:")
    print(file.read())
file.close()