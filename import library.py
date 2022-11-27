'''import math                                            #math is a library function
print(math.log(10))
print(math.sin(45))
print(math.cos(30))
print(math.sqrt(100))
print(math.factorial(10))

print(math.pow(10,3))'''

import random             #random number between 0 and 1
'''a=random.random()
if (a>.5):
    print('head')                                      #HEAD AND TAIL USING RANDOM NUMBER GENARATOR
else:
    print('tail')'''
#let us simulater a six face dice

'''dice1=(random.randrange(1,7))
dice2=random.randrange(1,7)                            #DICE SUM USING RANDOM NUMBER LIBRARY
total=dice1+dice2

print("your pair of dice is:",total)'''
###########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
import calendar
print(calendar.month(2022,9))                        #CALENDER IMPORT
print(calendar.calendar(2022))
'''
'''
from calendar import*#month,calendar                 #2ND WAY OF IMPORTING CALENDER
print(month(2022,10))
print(calendar(2022))
'''
'''
import calendar as c
print(c.month(2022,9))                               #importing and accessing it using as variable by as keyword
print(c.calendar(2022))
'''
'''
from calendar import month as c
print(c(2022,1))
'''