import csv
from datetime import datetime, time

# INPUT ABSEN DATANG
class Absen:
    def __init__(self):
        self.date = datetime.now().time()
        self.ontime = time(8, 0, 0)
        self.late = time(9, 15, 0)
        self.nim = input("Masukan NIM Anda = ")

        #CARI NIM
        self.nama = self.cari_nama()

        if self.nama == "FILE_NOT_FOUND":
            print("File data_mahasiswa.csv tidak ditemukan")
            return

        if self.nama == "NIM_TIDAK_DITEMUKAN":
            pilih = input("NIM tidak terdaftar. Tambahkan NIM baru? (y/n): ").lower()

            if pilih == "y":
                self.nama = input("Masukkan Nama Mahasiswa: ")
                self.tambah_mahasiswa()
                print("NIM berhasil ditambahkan")
            else:
                print("Absensi dibatalkan")
                return
            return
        #LOGIKA PROGRAM ABSEN
        if self.date <= self.ontime:
            self.status = "Tepat Waktu"
        elif self.date <= self.late:
            self.status = "Terlambat"
        else:
            self.status = "Tidak Hadir"

        self.simpan_absen()

        print("Jam datang :", self.date.strftime("%H:%M:%S"))
        print("Status     :", self.status)
        print("Nama       :", self.nama)

    def cari_nama(self):
        try:
            with open("data_mahasiswa.csv", "r") as f1:
                reader = csv.reader(f1)
                for row in reader:
                    if len(row) < 2:
                        continue

                    if row[0] == self.nim:
                        return row[1]

                return "NIM_TIDAK_DITEMUKAN"  

        except FileNotFoundError:
            return "FILE_NOT_FOUND"  

    def simpan_absen(self):
        with open("data_absensi.csv", "a", newline="") as f2:
            writer = csv.writer(f2)
            writer.writerow([
                self.nim,
                self.nama,
                self.date.strftime("%H:%M:%S"),
                self.late,
                self.status
            ])
    def tambah_mahasiswa(self):
        with open("data_mahasiswa.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.nim, self.nama])

absen1 = Absen()

