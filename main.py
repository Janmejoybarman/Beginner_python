'''n=10
print(type(n))
m=n/2
print(m,type(m))'''

'''a=5                        #declearing variable
b1='idfj             '
#1y=999    variable cannot start with number
_1aaa=8288 '''

'''rool=111                   #variable name are case sensitive
   ROLL=123
   ROLL=7171
   print(roll,ROLL,Roll'''

'''x,y =22,33                 #mulltiple variable in single line
print(x,y)
x=y=z=100
print(x,y,z)

x,y=2,3
print(x,y)
x,y=y,x                       #swapping value
print(x,y)'''

'''x=10
print(x)
del x                         #deleting variable
print(x)'''

'''count=2
count **=2                    #short hand operator(*,/,-.//,
count=count**2                #regular
print(count)'''

'''print('joy' in 'my name is joy')    #finding joy in the string
print('joy' in 'my name is tom')'''    #in OUTPUT IS ALWAYS BOOLEAN

'''x=2
print(1<x<5)
print(10>=x<20)                        #chaning operator
print(9<x<1)'''
                         #ESCAPE CHARACTER AND TYPE OF QUOTES
'''print('It\'s a beautifull day')                    #\=backslash
print("Hello \"IIT\" students")

print("My name is joy.\nI am from malda.")            #\n=newline
print("My name is joy. I am from malda.")
print("My name is joy.\t\t\t\tI am from malda.")'''   #more gap between two senteces


#print("It's a beautifull day")

'''x='hello'
y="world"'''
z='''\thello             #multiline string using ''''''
     jkgjkjk             
     jiuuig'''
'''print(x,y,z)'''

'''comment1
comment2
comment3'''

                       #STRING METHOD

'''x='PyThOn STriNg MeThodS'         #Converts a string into lower case
print(x.lower())

print(x.upper())                  #into upper case

print(x.capitalize())             #First caracter into upper case

print(x.title())                  #first character of each word to upper case

print(x.swapcase())               #upper cas ebecome lower and lower4 case become upper


y='I am joy'

print(y.islower())               #returns true if all the chracter
                                 #in the string are upper case either false
z='am'
print(z.isupper())               #same thing happening

s='I Am Joy'
print(s.istitle())'''              #Return true if the string follows the rule of a title
#return true

x=('101')
print(x.isdigit())                #returns true if all character in the string are digit/alphabets/alpha-numeric
x=('1khk')
print(x.isdigit())                 #False

x=('jhfdkj')
print(x.isalpha())
x=('11gggg')
print(x.isalpha())

x=('WwW111')
print(x.isalnum())              #true
x='@!#%'
print(x.isalnum())
                               #STRIP METHODE
#x='aaaapythonaaaaa'
#print(x.strip(a))  #name error

'''x='000kjjk000'
print(x.strip(0))'''              #TypeError: strip arg must be None or str

x='____JOY____'
print(x.strip('_'))
x="   JOY   "
print(x.strip())              #remove specific character from left or right side
x='----Py-thon----'
print(x.strip('-'))
print(x.lstrip('-'))
print(x.rstrip('-'))


