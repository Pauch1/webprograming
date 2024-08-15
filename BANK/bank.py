class Bank ():
    def __init__(self, name):
        self.name = name
        self.balance = ''
    
    def withdraw(self, amount):
        if self.balance_checker() < 100:
            print('minimun of 100')
            return False
        elif self.balance_checker()> self.balance:
            print('you withdraw more than you can')
            return False
        else:
            self.balance = self.balance - amount
            return True
        
    def balance_checker(self, amount):
         return self.balance - self.withdraw
         
        