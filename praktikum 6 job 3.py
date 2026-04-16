class Person:
    def __init__(self, name, age):
        """
        Konstruktor untuk menginisialisasi objek Person dengan nama dan umur.
        Atribut privat (dengan double underscore) menyimpan data internal.
        """
        self.__name = name
        self.__age = age

    @property
    def name(self):
        """
        Getter untuk atribut name.
        Mengembalikan nilai dari __name.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Setter untuk atribut name.
        Memeriksa apakah nilai tidak kosong sebelum mengubah nilai name.
        """
        if not value:
            print("Nama tidak boleh kosong.")
        else:
            self.__name = value

    @property
    def age(self):
        """
        Getter untuk atribut age.
        Mengembalikan nilai dari __age.
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Setter untuk atribut age.
        Memeriksa apakah nilai umur tidak negatif sebelum mengubah nilai age.
        """
        if value < 0:
            print("Umur tidak boleh negatif!")
        else:
            self.__age = value

# Contoh penggunaan
def main():
    # Membuat objek Person dengan nama "Alice" dan umur 30
    person = Person("Alice", 30)
    print(f"Nama: {person.name}, Umur: {person.age}")

    # Mengubah nama dan umur melalui setter
    person.name = "Bob"
    person.age = 35
    print(f"Nama baru: {person.name}, Umur baru: {person.age}")

    # Mencoba menetapkan nilai yang tidak valid untuk umur
    person.age = -5  # Akan memunculkan pesan error karena validasi umur negatif

if __name__ == "__main__":
    main()