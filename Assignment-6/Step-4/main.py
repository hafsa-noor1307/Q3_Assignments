class Bank:
    bank_name = "Meezan_Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


bank1 = Bank()
print(bank1.bank_name)
Bank.change_bank_name("Habib_Bank")
print(bank1.bank_name)
