# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:31:07 2026

@author: muham
"""

'''
Exercise 2.4 - Include the weight categories in
the bmi_cal function

'''

def bmi_cal(name, weight, height):
    bmi = weight / (height * height)
    if(bmi < 18.5):
        return ('%d is Underweight' %name);
    elif(bmi >= 18.5 or bmi <=24.5):
        return '%name is healthy';
    elif(bmi >= 25.0 or bmi <=29.9):
        return '%name is overweight';
    else: 
        return '%name is obese';

print(bmi_cal('Muhammad', 52, 12));