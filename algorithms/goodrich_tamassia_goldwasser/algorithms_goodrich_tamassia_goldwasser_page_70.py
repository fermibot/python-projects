class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance"""
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._bank

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


cc = CreditCard('John Doe', 'First Bank', '3568 5634 9856 5865', '1000')

if __name__ == '__main__':
    wallet = [CreditCard('John Doe', 'First Bank', '3568 5634 9856 5865', 1000),
              CreditCard('John Doe', 'Second Bank', '3568 5634 9856 5866', 1000),
              CreditCard('John Doe', 'Nth Bank', '3568 5634 9856 5867', 1000)]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Balance =', wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance =', wallet[c].get_balance())
        print()
