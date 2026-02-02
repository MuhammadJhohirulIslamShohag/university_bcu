# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:56:43 2026

@author: muham
"""
"""
Exercise 2.1 – Implementation of BMI
calculation

"""


"""
Exercise 2.2- BMI calculation function 
bmi = int(weight / (height * height))
"""

def bmi_cal(width, height):
    bmi = width / (height * height)
    return bmi

name = str(input("Enter your name: "))
height = int(input('Input your height in meters: '))
weight = int(input('Input your weight in kilograms: '))
print(bmi_cal(weight, height))