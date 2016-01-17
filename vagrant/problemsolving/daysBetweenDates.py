# Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325398

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True
        
def daysInMonth(year, month):
    if isLeapYear(year):
        daysOfMonths[1]=29
    else:
        daysOfMonths[1]=28
    return daysOfMonths[month-1]

def nextDay(year, month, day):
    if day<daysInMonth(year,month):
        return (year,month,day+1)
    elif day == daysInMonth(year,month):
        if month < 12:
            return (year,month+1,1)
        elif month == 12:
            return (year+1,1,1)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1==year2 and month1< month2:
        return True
    elif year1==year2 and month1==month2 and day1<day2:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    assert dateIsBefore(year1, month1, day1, year2, month2, day2) 
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
        year1,month1,day1 = nextDay(year1, month1, day1)
    return days

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

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