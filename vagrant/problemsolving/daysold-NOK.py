# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    #if (year is not exactly divisible by 4) then (it is a common year)
    if year % 4 != 0:
        return False
    # else if (year is not exactly divisible by 100) then (it is a leap year)
    elif year % 100 != 0:
        return True
    # else if (year is not exactly divisible by 400) then (it is a common year)
    elif year % 400 !=0:
        return False
    # else (it is a leap year)
    else:
        return True
def yearstodays(y1,y2):
    yearstodays=0
    for year in range(y1,y2):
        if isLeapYear(year):
            yearstodays += 366
        else:
            yearstodays += 365
    return yearstodays

def dayoftheyear(y,m,d):
    day = 0
    if m>2 and isLeapYear(y):
        day +=1
    for i in range(0,m):
        day += daysOfMonths[m-1]
    return day+d
        
def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    days += yearstodays(y1,y2)
    days += dayoftheyear(y2,m2,d2) -dayoftheyear(y1,m1,d1)
    return days
    
    
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()