class BankAccount:
    def __init__(self, owner, balance):
        # Atribut dengan double underscore (__) dianggap "private" di Python
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        """Method untuk menambahkan saldo."""
        if amount > 0:
            self.__balance += amount
            print(f"{amount} telah ditambahkan ke akun {self.__owner}.")
        else:
            print("Jumlah deposit harus lebih dari 0.")

    def withdraw(self, amount):
        """Method untuk menarik saldo."""
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} telah ditarik dari akun {self.__owner}.")
        else:
            print("Saldo tidak mencukupi.")

    def get_balance(self):
        """Method untuk mendapatkan informasi saldo terkini."""
        return self.__balance

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek BankAccount dengan owner="Alice" dan balance awal 1000
    alice_account = BankAccount(owner="Alice", balance=1000)

    # Deposit uang
    alice_account.deposit(500)       # Berhasil
    alice_account.deposit(-100)      # Gagal (validasi)

    # Withdraw uang
    alice_account.withdraw(300)      # Berhasil
    alice_account.withdraw(2000)     # Gagal (saldo tidak cukup)

    # Mendapatkan saldo
    current_balance = alice_account.get_balance()
    # Akses owner menggunakan name mangling karena owner bersifat private
    print(f"Saldo terakhir di akun {alice_account._BankAccount__owner}: {current_balance}")

    # Mencoba mengakses atribut 'private' langsung (tidak direkomendasikan)
    # alice_account.__balance  # Akan error
    # Karena Python "mangling" nama atribut __balance menjadi _BankAccount__balance
    # Ini adalah salah satu mekanisme enkapsulasi sederhana di Python.