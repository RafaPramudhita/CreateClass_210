class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
    try:
        # input panjang dan lebar
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))

        # Memastikan nilai panjang dan lebar tidak negatif
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")

        # Membuat objek PersegiPanjang
        persegi_panjang = PersegiPanjang(panjang, lebar)

        # Menampilkan informasi objek
        print(persegi_panjang)
        print("Keliling:", persegi_panjang.keliling(), "cm")
        print("Luas:", persegi_panjang.luas(), "cm^2")
    
    # buat fungsi hanya angka yg bisa di input
    except ValueError:
        print("Input tidak valid:", "pastikan masukan angka")
    
# panggil main
if __name__ == "__main__":
    main()


