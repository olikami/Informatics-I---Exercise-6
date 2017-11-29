from vehicle import *


class Customer(object):
    
    def __init__(self,name):
        self._name = name
        self._score = self.credit_score()

    def __str__(self):
        return 'Customer: {:s}'.format(self._name)

    def credit_score(self):
        from random import randint
        return randint(0, 100) > 60

    def get_score(self):
        return self._score


class VIP_Customer(Customer):

    def credit_score(self):
        return True


### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

print(Wendy) # expected output: Customer: Wendy
print(Heidi) # expected output: Customer: Heidi

print(Wendy.get_score()) # expected output: True or False
print(Heidi.get_score()) # expected output: True
