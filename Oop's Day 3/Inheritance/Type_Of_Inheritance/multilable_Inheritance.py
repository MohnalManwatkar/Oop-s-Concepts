
                            # Multilable Inheritance

class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print('this will show you account open status')

    def deposit(self):
        print('this will show you deposited amount')
b=bank()
b.transaction()
b.account_opening()
b.deposit()


class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print('this will shows you all the transaction happens to icici through hdfc')

h=HDFC_bank()
h.transaction()
h.account_opening()
h.deposit()
h.hdfc_to_icici()

class icici(HDFC_bank):
    pass

i=icici()
i.transaction()
i.account_opening()
i.deposit()
i.hdfc_to_icici()

