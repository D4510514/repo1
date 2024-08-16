#Greeting and date of 100yrs old.

'''
from datetime import date
name = input("Enter your name: ")
print("Good Morning, " + name + ".")
age = input("Enter your age: ")
date = date.today()
year = date.year
age100 = year + 100 - int(age)
print("In " + str(age100) + " you will tern 100 years old.")
'''
#checking module importation.

import module1

num = input("Enter a number: ")
print(module1.check_even(num))

name = input("Enter a string: ")
print(module1.reverse(name))