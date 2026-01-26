# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 14:24:02 2026

@author: muham
"""
a = 9
b= 8
c = 12
d = 33
e = 5

totalVariableValue = a + b + c + d + e
meanValue = totalVariableValue / 5 
totalSquareDevisionVlaue = ((a - meanValue) ** 2) + ((b - meanValue) ** 2) + ((c - meanValue) ** 2) + ((d - meanValue) ** 2) + ((e - meanValue) ** 2) 
totalSquareDevisionVlaueSum = totalSquareDevisionVlaue / 5

standardDeviationVlaue = totalSquareDevisionVlaueSum ** (1 / 2.0)
print(standardDeviationVlaue)