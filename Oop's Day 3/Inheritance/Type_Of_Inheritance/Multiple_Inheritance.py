
                                    # Multiple Inheritance

class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print('this will show you account open status')

    def deposit(self):
        print('this will show you deposited amount')

class HDFC_bank:
    def hdfc_to_icici(self):
        print('this will shows you all the transaction happens to icici through hdfc')

class icici(bank, HDFC_bank):
    pass
i=icici()
i.transaction()
i.account_opening()
i.deposit()
i.hdfc_to_icici()

#######################################################################################################################
# ---------------------------------------------------------------------------------------------------------------------
#######################################################################################################################


                                    # Multiple Inheritance

        '''this class is different'''
class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print('this will show you account open status')

    def deposit(self):
        print('this will show you deposited amount')

    def test(self):
        print("this test from bank")

        '''this class is different'''
class HDFC_bank:
    def hdfc_to_icici(self):
        print('this will shows you all the transaction happens to icici through hdfc')

    def test(self):
        print("this test from HDFC_bank")

      """   '''multiple inheritance by calling bank and HDFC''' | '''we can use 1,2,2+++ classes as multiple inheritance'''"""
class icici(bank, HDFC_bank): #jiska bhi argument first rahenga uska test function accept/print karenga
    pass
i=icici()
i.transaction()
i.account_opening()
i.deposit()
i.hdfc_to_icici()
