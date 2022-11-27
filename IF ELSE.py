'''print('enter:')
n=int(input())
m=2022
age=m-n
if (age<13):
	print('not allow')

else:
	print('wellcome')'''
#########################
'''n=int(input('enter'))
if(n%2==0):                             #accepting input and telling wheather it is even or odd
	print('even')
else:
	print('odd')'''
################################
#input 20 25 last element 0,5
#input 21,12,23 etc output other

'''x=input()
if (int(x[-1])==0 or int(x[-1])==5):
	print('0')
else:
	print("other")'''

'''num=int(input())
if (num % 5==0):
	if (num % 10==0):                     #Find the given number ends with 0 or 5 or any other number
		print('0')
	else:                                 # 10,15,12,11,100,55
		print('5')
else:
	print('other')'''

#################################
'''marks=int(input("Enter marks: "))
if (marks >= 90):
	print("A")
if (marks >=80 and marks < 90):
	print('B')
if (marks >=70 and marks < 80):
	print('C')
if (marks >=60 and marks < 70):
	print('D')
if (marks >=100 and marks < 0):
	print('Invalid input')
else:
	print('E')'''

########################
'''marks=int(input("Enter marks: "))
if (marks >= 0 and marks <= 100):
    if (marks >= 90):
	     print("A")
    if (marks >=80 and marks < 90):
	     print('B')                          #grade of students based on marks 0 to 100
    if (marks >=70 and marks < 80):
	     print('C')
    if (marks >=60 and marks < 70):
	     print('D')
    if(marks <60):
	     print("E")
else:
	print('Invalid input')'''


################################

marks=int(input("Enter marks: "))
if (marks >= 0 and marks <= 100):
    if (marks >= 90):
	     print("A")
    elif (marks >=80):                       #else-if  in short elif
	     print('B')                          #grade of students based on marks 0 to 100
    elif (marks >=70):
	     print('C')
    elif (marks >=60):
	     print('D')
    elif(marks <60):
	     print("E")
else:
	print('Invalid input')