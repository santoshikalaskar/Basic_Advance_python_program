"""
    Check divide by 0 decorator
"""
def check(func):
    def inside(a,b):
        if b == 0:
            print('cant devide by zero')
            return
        return func(a,b)
    return inside

@check
def div(a , b):
    return a / b

print('case 1:',div(2,2))
print('case 2:', div(10,5))
print('case 3:',div(10,0))

"""
    Upper case decorator
"""
def upper_case_decorator(function):
    def wrapper():
        func = function()
        message = func.upper()
        return message
    return wrapper

def split_decorator(function):
    def wrapper():
        func = function()
        return func.split()
    return wrapper

@upper_case_decorator
def say_hello():
    return "hello"

@split_decorator
@upper_case_decorator
def say_hello_world():
    return "hello world"


print('upper case decorator :',say_hello())
print('upper case decorator & split decorator :',say_hello_world())