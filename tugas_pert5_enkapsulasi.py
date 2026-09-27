class Employee:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji


class Company:
    # Bikin blueprint perusahaan sesuai spesifikasi tugas
    def __init__(self, nama_perusahaan):
        self.nama_perusahaan = nama_perusahaan

        # Enkapsulasi array data karyawan (Private Attribute pakai double underscore)
        self.__employees = []

    def tambah_karyawan(self, karyawan_baru):
        # Petunjuk teknis: Validasi input object menggunakan isinstance() sebelum masuk list
        if isinstance(karyawan_baru, Employee):
            self.__employees.append(karyawan_baru)
            print(f"[Sukses] Karyawan {karyawan_baru.nama} berhasil ditambahkan.")
        else:
            print(
                "[Error] Input ditolak! Data yang dimasukkan harus berupa objek dari kelas Employee."
            )

    # Private method (hanya bisa dipanggil internal dari dalam class)
    def __calculate_payroll(self):
        total_gaji = sum(emp.gaji for emp in self.__employees)
        return total_gaji

    # Method publik untuk memanggil private method secara internal
    def proses_pembayaran_gaji(self):
        print(f"Menghitung gaji untuk {len(self.__employees)} karyawan...")
        total = self.__calculate_payroll()
        print(f"Total Payroll {self.nama_perusahaan}: Rp{total:,}")


# ==========================================
# Pengujian Program (Live Code Test)
# ==========================================
if __name__ == "__main__":
    kantor = Company("Tech Nusantara")

    # Siapkan sampel objek karyawan
    emp1 = Employee("Jonathan", 8000000)
    emp2 = Employee("Briana", 8500000)

    # Masukkan data karyawan yang valid
    kantor.tambah_karyawan(emp1)
    kantor.tambah_karyawan(emp2)

    # Uji coba memasukkan data tidak valid (string) untuk membuktikan fitur isinstance berjalan
    kantor.tambah_karyawan("Tania (Bukan Objek)")

    # Eksekusi proses pembayaran gaji
    print("-" * 35)
    kantor.proses_pembayaran_gaji()
