import csv
from datetime import datetime, time

class Absen:
    def __init__(self):
        while True:
            self.date = datetime.now().time()
            self.ontime = time(8, 0, 0)
            self.late = time(9, 15, 0)

            # INPUT NIM
            self.nim = input("\nMasukkan NIM Anda = ")

            # CARI NAMA BERDASARKAN NIM
            self.nama = self.cari_nama()

            if self.nama == "FILE_NOT_FOUND":
                print("File data_mahasiswa.csv tidak ditemukan")
                break

            #NIM TIDAK TERDAFTAR
            if self.nama == "NIM_TIDAK_DITEMUKAN":
                pilih = input("NIM tidak terdaftar. Tambahkan NIM baru? (y/n): ").lower()

                if pilih == "y":
                    self.nama = input("Masukkan Nama Mahasiswa = ")
                    self.tambah_mahasiswa()
                    print("Data mahasiswa berhasil ditambahkan.")
                    print("Silakan lakukan absensi ulang.")
                    continue   # ⬅️ KEMBALI KE INPUT NIM
                else:
                    print("Absensi dibatalkan.")
                    break

            #STATUS ABSEN
            if self.date <= self.ontime:
                self.status = "Tepat Waktu"
            elif self.date <= self.late:
                self.status = "Terlambat"
            else:
                self.status = "Tidak Hadir"

            # SIMPAN ABSENSI
            self.simpan_absen()

            # OUTPUT
            print("\nNama       :", self.nama)
            print("Jam Datang :", self.date.strftime("%H:%M:%S"))
            print("Status     :", self.status)

            break

    def cari_nama(self):
        try:
            with open("data_mahasiswa.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    if row[0] == self.nim:
                        return row[1]
                return "NIM_TIDAK_DITEMUKAN"
        except FileNotFoundError:
            return "FILE_NOT_FOUND"

    def simpan_absen(self):
        with open("data_absensi.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                self.nim,
                self.nama,
                self.date.strftime("%H:%M:%S"),
                self.status
            ])

    def tambah_mahasiswa(self):
        with open("data_mahasiswa.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.nim, self.nama])


Absen()
