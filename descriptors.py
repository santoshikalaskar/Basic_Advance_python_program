"""
-These are special type of protocols used to set, get or delete any instance from a class.
-This is simillar to getter and setter method used in other programming language like java in encapsulation
-There are 3 predefined descriptors in python. Three different methods that are __getters__(),
     __setters__(), and __delete__(). If any of these 3 defined for an object then called as descriptor.
-In the case of descriptor all the methods are made public and variables will be private
"""
class Employee(object):

     def __init__(self, name=''):
          self.__name = name

     """
     name(self) property will use to get the value of private variable __name. since we cant access private variable
          outside the class se we go for descriptor methods ie, getter,setter and delete
     """
     @property
     def name(self):
          return "Getting name :" + self.__name
     
     """
     Since our __name variable is private so we cant access it outside the class by object reference.
          To set or change value we can use setter method.
     """
     @name.setter
     def name(self, name):
          print('Setting name :', name)
          self.__name = name
     

     """
     To delete private variable we have to go for descriptor method deleter. 
     """
     @name.deleter
     def name(self):
          print("Deleting name :",self.__name)
          del self.__name
     

emp1 = Employee("Deep")
print(emp1.name)
emp1.name = "Rajnikant"
print(emp1.name)
print("Accessing private variable by class : ",emp1._Employee__name)
del emp1.name
