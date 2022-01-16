class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100
    
    # name of the shared method . getter or setter
    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100
    
    
bank_account = Currency(50000)
print(bank_account.dollars) # 50000.0

bank_account.dollars = 100000
print(bank_account.dollars) # 100000.0

bank_account.dollars = -20000
print(bank_account.dollars) # 100000.0