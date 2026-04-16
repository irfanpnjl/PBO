class SimpleExample:
    def __init__(self, name):
        """
        Konstruktor: Dipanggil saat objek dibuat.
        Menyimpan nilai 'name' dan mencetak pesan pembuatan objek.
        """
        self.name = name
        print(f"Konstruktor: Objek '{self.name}' telah dibuat.")

    def __del__(self):
        """
        Destruktor: Dipanggil saat objek dihapus.
        Mencetak pesan bahwa objek sedang dihapus.
        """
        print(f"Destruktor: Objek '{self.name}' sedang dihapus.")

def main():
    print("Program dimulai.\n")

    # Membuat objek SimpleExample
    obj = SimpleExample("Demo")
    print("Program sedang berjalan...\n")

    # Menghapus objek secara eksplisit
    del obj
    print("Objek telah dihapus secara eksplisit.\n")

    print("Program selesai.")

if __name__ == "__main__":
    main()