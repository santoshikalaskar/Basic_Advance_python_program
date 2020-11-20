"""
@property decorator is used to change a method into a class property or variable. so we can excess any method 
directly as we access any variables ie without ()
"""

# class Employee:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name  = last_name
#         self.email      = first_name + last_name +'@email.com'

#     def full_name(self):
#         return self.first_name +" "+self.last_name


# emp = Employee('Deep','Sarkar')

# emp.first_name = "Raj"
# emp.last_name  = "kumar"

# print(emp.first_name)
# print(emp.last_name)
# print(emp.email)
# print(emp.full_name())

"""
    Output :
    Raj
    kumar
    DeepSarkar@email.com
    Raj kumar
    
    but expected output :
    Raj
    kumar
    RajKumar@email.com
    Raj kumar
"""
"""
to overcome this problem without changing our code we can declaire our email as property
"""
class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name
    
    @property
    def email(self):
        return self.first_name + self.last_name +'@email.com'

    @property
    def full_name(self):
        return self.first_name +" "+self.last_name


emp = Employee('Deep','Sarkar')

emp.first_name = "Raj"
emp.last_name  = "kumar"

print(emp.first_name)
print(emp.last_name)
print(emp.email)
print(emp.full_name)