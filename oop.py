class CreditCard(object):
    """A consumer  CreditCard"""

    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.

        The Intial balance is zero

        customer the name of the customer
        bank 	 the name of the bank
        acnt     the name of the account
        limit    the credit limit(Measured in dollars)

         """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """ Return name of the customer """
        return self._customer

    def get_bank(self):
        """ Return the bank name """
        return self._bank

    def get_account(self):
        """ Return card identifying number as a String """
        return self._account

    def get_limit(self):
        """ Return current credit limit"""
        return self._limit

    def get_balance(self):
        """ Return current balance"""
        return self._balance

    def charge(self, price):
        """ 
                Charge given price  to the card, assuming sufficient credit limit
                Return True if the charge was processed ;False if charge was denied

        """
        if price + self._balance > self._limit:
            return False

        else:
            self._balance += price
            return True

    def make_payments(self, amount):
        """ 
                Process customer payment that reduces balance
        """
        self._balance -= amount



class PredatoryCreditCard(CreditCard):
    """
    An extension to Credit card that compounds interest and fees 
    

    """
    def __init__(self, customer, bank,acnt,limit,apr):
        """
            Create a new predatory credit card instance.

            The intial balance is Zero

            customer the name of the customer
            bank     the name of the bank
            acnt     the account identifier
            limit    credit limit (Measured in dollars)
            apr      annual percentage rate (e.g 0.00825 )

        """
        OVERTIME_FEE = 5
        super().__init__(customer,bank, acnt, limit) #call the super constructor
        self._apr = apr


    def charge(self, price):
        """
            Charge given price to the card, assuming  sufficient credit limit

            return true if charge was processed
            Return False and assess $5 fee if charge is denied.

        """

        success = super().charge(price)
        if not success:
            self._balance+=PredatoryCreditCard.OVERTIME_FEE
        return success


    def process_month(self):
        """
        Assess Monthly interest on outstanding balance
        """

        if self._balance > 0:
            #if positive balance, convert APR to monthly multiplicative Factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
            
        


if __name__ == '__main__':
	wallet=[]
	wallet.append(CreditCard('John Doe', ' California Savings', '5391 0375 9387 5309', 2000))
	wallet.append(CreditCard('Bozics Chucky', ' California Federal', '5691 0375 3087 5309', 2500))
	wallet.append(CreditCard('Dude Yoo', ' Kampala Savings', '6000 0375 9387 5309', 3500))

	for val in range(1,7):
		wallet[0].charge(val)
		wallet[1].charge(2*val)
		wallet[2].charge(3*val)

	for c in range(3):
		print('customer=',wallet[c].get_customer)
		print('Bank=',wallet[c].get_bank)
		print('Account=',wallet[c].get_account)
		print('Limit=',wallet[c].get_limit)
		print('Balance=',wallet[c].get_balance)

		while wallet[c].get_balance() > 100:
			wallet[c].make_payments(100)
			print("New balance =", wallet[c].get_balance())
			print()


'''
cc = CreditCard('chucky', "bank x", " 5678 0567 9567 5309 ", 1000)
print(cc.get_bank())
print(cc.get_balance())
print(cc.make_payments(200))
'''