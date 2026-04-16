class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
            self._update_grade()
        else:
            print("Nilai harus berada di antara 0 hingga 100.")

    def _update_grade(self):
        if 90 <= self.__score <= 100:
            self.__grade = "A"
        elif 80 <= self.__score <= 89:
            self.__grade = "B"
        elif 70 <= self.__score <= 79:
            self.__grade = "C"
        elif 60 <= self.__score <= 69:
            self.__grade = "D"
        else:
            self.__grade = "E"

    def show_info(self):
        print(f"Nama Mahasiswa: {self.name}")
        print(f"Nilai: {self.score}")
        print(f"Grade: {self.__grade}")

    def __del__(self):
        print(f"Data mahasiswa {self.name} telah dihapus dari sistem.")


student1 = Student("Siti", 87)
student1.show_info()

print("\nNilai diubah...")
student1.score = 93
student1.show_info()
print()

del student1