import sys


class Vehicle(object):
    vehicle_id = 0
    vehicles_sold = []

    def __init__(self,year,mileage,purchase_price,serial_number):
        try:
            self._year = int(year)
            self._mileage = int(mileage)
            self._purchase_price = int(purchase_price)
        except ValueError as e:
            print('Error: You didn\'t enter a number for the {:s} variable.'.format(str(e).split(' ')[-1]))  # Say which
            # variable generates the error, that's just good manners.
        self._serial_number = serial_number
        self._vehicle_id = Vehicle.generate_vehicle_id(self)
        Vehicle.vehicle_id += 1

    def __str__(self):
        return str(self.get_id())

    def get_id(self):
        return self._vehicle_id

    @staticmethod
    def generate_vehicle_id(self):
        return Vehicle.vehicle_id + 100000

class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,doors):
        super().__init__(year, mileage, purchase_price, serial_number)
        self._doors = doors
        self._wheels = 4


class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,wheels,doors=2):
        super().__init__(year, mileage, purchase_price, serial_number)
        self._doors = doors
        self._wheels = wheels

        
class Motorcycle(Vehicle):

    classic_count = 0

    def __init__(self,year,mileage,purchase_price,serial_number,classic=False):
        super().__init__(year, mileage, purchase_price, serial_number)
        self._classic = classic
        if classic:
            Motorcycle.classic_count += 1
    

### test cases ###

# initialising vehicle instances

Veh1 = Vehicle(2008,65000,7500,"34567851g4")
Veh2 = Car(2007,125000,5500,"e44653ftu1",4)
Veh3 = Car(2012,45000,8900,"gf5622iguz",doors=2)
Veh4 = Lorry(2005,180000,16000,"hbh997123f",6)
Veh5 = Lorry(2013,30000,35000,"hjbf17jbkh",8,4)
Veh6 = Motorcycle(1975,75500,40000,"bh545664rh",True)

print(Veh1,Veh2,Veh3,Veh4,Veh5,Veh6)
#prints 	100000 	100001 	100002 	100003 	100004 	100005

Veh7 = Motorcycle("year",10000,25000,"bjhgss4rdh",False)
# instance Veh7 generates an exception (ValueError) (uncomment to test)
