from abc import ABC, abstractmethod

'''
   Abstraction 
'''

class Vehicle(ABC):

    @abstractmethod
    def colour(self):
        pass
    
    '''
        abstract class can have concrete methods
    '''
    def fuel_type(slef):
        print("petrol")


class Car(Vehicle):

    def colour(self):
        print ('White car.')

    def wheel(self):
        print('4 Wheels')

print('----vehicle abstraction----')
ref_car = Car()
ref_car.colour()
ref_car.wheel()
ref_car.fuel_type()

'''
    Interface
'''

class Army(ABC):

    @abstractmethod
    def gun(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Navy(Army):

    def gun(self):
        print("Ak 47")

    def area(self):
        print("ocean")

print('----Army Interface----')
ref_navy = Navy()
ref_navy.gun()
ref_navy.area()