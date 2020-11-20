print("----- lambda -----")
"""
LAMBDA/ANANOMOUS Functions :
  Generally it is 1 line function used to perform small operations.
"""

a = lambda a:2*a   #example a : Takes 'a' as an argument and returns a*2
print('a :',a(6))

""""""

b = lambda b,c: b%c #example b : Takes 'b' and 'c' as an argument and returns b%c
print('b :',b(7,2))

""""""

def myfunc(n):        #example c : myfunc(n) takes a number as an argument and returns lambda function. 
  return lambda a : a * n # ie by this we can create one more 1 line function.

twice = myfunc(2)  #created a function twice which will return n*2 when a int argument is passed an argument
print('c :',twice(20)) #passed 20 in twice() will return 40

multiply = myfunc(3)
print('d :',multiply(3))






print("----- map() -----")
"""
map(func, *iterables) : it is used to perform some small operations to all the elements in iterable ie. sequence like list.
 commonly we can use lambda function as a function argument.
"""
#example 1
marks = [40, 49, 31, 45, 43 , 41, 21, 33]

add_5_in_all_marks = list(map(lambda a:a+5,marks))
print('adding 5 to all the numbers in list using map :',add_5_in_all_marks)

#example 2
subjects = ['math', 'english','science']

subj_in_upper_case = list(map(str.upper, subjects))
print('subjects in upper case :',subj_in_upper_case)







print("----- zip() -----")
"""
zip(iterable1, iterable2) : used to create list of touples of elements of 2 list
"""

even = [2, 4, 6, 8]
odd  = [1, 3, 5, 7]

my_touple = list(zip(odd, even))
print('touple of odd even :',my_touple)







print("----- filter() -----")
"""
filter(func, *iterable) : filter is used to filter specific results or element from list
"""
my_list = [1,2,3,4,5,6,7,8,9]

filter_even = list(filter(lambda a: a%2 == 0, my_list))
print('all even filtered numbers :',filter_even)







print("----- reduce() -----")
"""
reduce(func , *iterable) : it is used to perform arithmatic operation in a single list and output will be 
  string type or int type
- we have to import it from functools
"""

from functools import reduce

reduce_list = [1,2,3,4,5]

sum_by_reduce = reduce(lambda a , b : a + b, reduce_list)
print('sum by reduce :',sum_by_reduce)