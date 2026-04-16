class Calculator:
    def __init__(self, initial_value=0):
        """
        Konstruktor kelas Calculator.
        - self: Mengacu pada instance yang dibuat.
        - initial_value: Nilai awal dari kalkulator.
        """
        self.value = initial_value
        print(f"Kalkulator diinisialisasi dengan nilai: {self.value}")

    def add(self, number):
        """
        Menambahkan 'number' ke nilai yang tersimpan di objek.
        - self.value: Menunjukkan nilai saat ini yang disimpan di objek tersebut.
        - number: Nilai yang akan ditambahkan.
        """
        self.value += number
        print(f"Setelah penambahan {number}, nilai sekarang adalah: {self.value}")

    def subtract(self, number):
        """
        Mengurangi 'number' dari nilai yang tersimpan.
        - self.value: Nilai saat ini dalam objek.
        - number: Nilai yang akan dikurangkan.
        """
        self.value -= number
        print(f"Setelah pengurangan {number}, nilai sekarang adalah: {self.value}")

    def reset(self):
        """
        Mengatur ulang nilai kalkulator ke 0.
        """
        self.value = 0
        print("Nilai telah direset ke 0.")

    def show_value(self):
        """
        Menampilkan nilai saat ini dari kalkulator.
        """
        print(f"Nilai saat ini adalah: {self.value}")

# Contoh penggunaan untuk memahami peran 'self'
def main():
    # Membuat objek Calculator dengan nilai awal 10
    calc1 = Calculator(initial_value=10)

    # Menggunakan metode dari objek calc1
    calc1.add(5)          # Menambah 5 ke nilai calc1
    calc1.subtract(3)     # Mengurangi 3 dari nilai calc1
    calc1.show_value()    # Menampilkan nilai calc1

    # Membuat objek Calculator lainnya dengan nilai awal default (0)
    calc2 = Calculator()
    calc2.add(20)         # Menambah 20 ke nilai calc2
    calc2.show_value()    # Menampilkan nilai calc2

    # Penjelasan peran self:
    # 'self' memungkinkan setiap instance (calc1, calc2) memiliki atribut 'value' masing-masing.
    # Perubahan yang dilakukan pada calc1 tidak akan mempengaruhi calc2, 
    # karena masing-masing mengacu pada self yang berbeda (instance yang berbeda).

if __name__ == "__main__":
    main()
    