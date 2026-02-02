# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:31:07 2026

@author: muham
"""

'''
Exercise 2.4 - Include the weight categories in
the bmi_cal function

'''

"""
def bmi_cal(name, weight, height):
    bmi = weight / (height * height)
    if(bmi < 18.5):
        return f'{name} is Underweight' ;
    elif(bmi >= 18.5 or bmi <=24.5):
        return f'{name} is healthy';
    elif(bmi >= 25.0 or bmi <=29.9):
        return f'{name} is overweight';
    else: 
        return f'{name} is obese';

print(bmi_cal('Muhammad', 52, 12));

"""

'''
1.2 Converting numbers as strings into integers and floats
print(int('10'))
'''

"""
value = input('Enter the value of number:')
print(float(value))

"""

"""
# Converting single number value in without decimals value
stringNumberValue = '10';
print(int(stringNumberValue));

"""

"""
1.3 Converting between floats and ints

"""
"""
floatNumberValue = 9.6
print(int(floatNumberValue))
print(float(8))
print(8*1.0) # Use of the float() function is preferred, because then the source code expresses more clearly what the programmer intended.
"""

"""
1.4 Converting numbers into string format
There are 2 approaches, direct conversion, or interpolation of numbers into strings. We can
use the str() function to convert a number into string directly.
"""
print(str(8.5))
print(str(3))

#We can also interpolate numbers into strings. Python uses %d and %f for ints and floats.
s = "an int %d number" % 10.5
print(s)

# We can also interpolate numbers into strings. Python uses %d and %f for ints and floats
s = "a float %f number" % 3.3
print(s)

"""
%f gives 6 decimal places. We can choose how many decimals we want. Formatting money
amounts in a report we will typically want 2 decimal places.
"""

s = "a float %.1f number" % 3.3
print(s)

d = "a float %15.2f" % 123456789.01
print(d)

"""
If we want to interpolate more than one number into a string, we can use a tuple, which is a
comma separated set of values in round brackets, to supply the data.
"""
a=10
b=3.6
print("a float %f and an int %d" % (b, a))

"""
2. Definition of simple Python functions with input and output

"""
def square(x):
    return x * x

# print(square(10))

"""
2.1 A function with 2 statements
"""
def sqrt(x):
    y = x ** 0.5;
    return y

print('number %.2f should be 2 decimal number' %sqrt(2))





