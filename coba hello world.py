# ---------------------------------------------------------------------
# Bagian untuk mendeskripsikan struktur class Data Koleksi dan turunannya
# ---------------------------------------------------------------------
# kelas abstrak menunjukkan struktur Data Koleksi
# Script ini dibuat oleh Developer A

from abc import ABC, abstractmethod

class Koleksi(ABC):
    # konstruktor atribut: kode, judul, tahun, penerbit
    def __init__(self, kode, judul, tahun, penerbit):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun
        self.penerbit = penerbit

    # abstract method 
    @abstractmethod
    def tampilkan_info(self):
        pass

# class Buku yang merupakan turunan dari Koleksi
class Buku(Koleksi):
    # konstruktor atribut Buku
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        # inisialisasi atribut untuk super class nya
        super().__init__(kode, judul, tahun, penerbit)
        # inisialisasi atribut untuk selainnya
        self.pengarang = pengarang

    # overriding method abstrak milik super class
    def tampilkan_info(self):
        return f"Buku [{self.kode}] - {self.judul} ({self.tahun}), Pengarang: {self.pengarang}, Penerbit: {self.penerbit}"

# class Majalah yang merupakan turunan dari Koleksi
class Majalah(Koleksi):
    # konstruktor atribut Majalah
    def __init__(self, kode, judul, tahun, penerbit, edisi):
         # inisialisasi atribut untuk super class nya
        super().__init__(kode, judul, tahun, penerbit)
        # inisialisasi atribut untuk selainnya
        self.edisi = edisi

     # overriding method abstrak milik super class
    def tampilkan_info(self):
        return f"Majalah [{self.kode}] - {self.judul} ({self.tahun}), Penerbit: {self.penerbit}, Edisi: {self.edisi}"

# class Jurnal yang merupakan turunan dari Koleksi
class Jurnal(Koleksi):
     # konstruktor atribut Jurnal
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        # inisialisasi atribut untuk super class nya
        super().__init__(kode, judul, tahun, penerbit)
        # inisialisasi atribut untuk selainnya
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    # overriding method abstrak milik super class
    def tampilkan_info(self):
        return f"Jurnal [{self.kode}] - {self.judul} ({self.tahun}), Penerbit: {self.penerbit}, Bidang: {self.bidang_studi}, Impact Factor: {self.impact_factor}"