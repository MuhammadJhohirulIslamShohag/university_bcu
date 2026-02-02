"""
c. Copy and paste your successful areacirc() and rectarea() functions into a new window,
and save this file as Z:\ CMP7244\Lab2\funcs.py. To be able to import this, you are likely
to need to add the folder where you saved your funcs.py module to the Python module
search path.

"""
import sys;
a = sys.path.append('D:\BCU\Software_Development\lab\CMP7244_S_D_Lab_W-02')
print(a);

import funcs

funcs.areacirc(10.0)
funcs.rectarea(3,4)

"""
a. We have used a single = to assign a value to a variable, e.g. x=2 and we change or
overwrite the value in x (if it had a value) by doing this. But in the above isleap function
definition we use a double == to compare or test 2 values of a pair of variables, literals or
expressions to see whether or not these are the same. Here we are interested in whether or
not the remainder on dividing y (the year) by 4 is equal to 0. We are not going to
overwrite the value of the variable or expression on the left hand side of the == operator.

"""
def isleap(y):
    if y % 4 == 0:
        return True
    else:
        return False;
    
isleap(2000)




