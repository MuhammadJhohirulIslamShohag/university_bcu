"""
5.1 Student exercise
Extend leap.py by adding a function daysinmonth() to which a month and year are passed as
integer parameters. The function must branch based on month and return an integer, being the
number 28, 29, 30 or 31. The month will be passed as a number between 1 and 12. If the
month number is 2, the function isleap() must be called to work out whether the year
parameter is a leap year or not. Months with 31 days should be detected using an else: block.
The number of days in the 12 months is known from this statement: "30 days has September,
April, June and November. All the rest have 31, except February which has 28, and 29 for a
leap year"

"""
def isleap(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False;
    elif y % 400 == 0:
        return True
    else:
        return False;
    
def daysinmonth(month, year):
    if(month == 2):
        if isleap(year):
            return 'February Month is 29 days.';
        else:
            return 'February Month is 28 days.'
    else:
       if(month == 4):
           return '30 days has April'
       elif(month == 9):
           return '30 days has September'
       elif(month == 11):
           return '30 days has November'
       elif(month == 6):
           return '30 days has June'
       else:
           return 'All the rest have 31, except February which has 28, and 29 for a leap year'
   
print(daysinmonth(2, 2026))
   
    