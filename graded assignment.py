'''word=input()
flag=False
if word.count('(')==word.count(')'):
     if word.count('[')==word.count(']'):
         if word.count('{')==word.count('}'):
             flag=True                               #if you take any alphabet or number it wiil show perfect
if flag:
    print('PARFECT')
else:
    print('IMPEFRFECT')
'''
######################
'''n=int(input())
if n>10:
    print('hey kid!')
elif n<0:
    pass
else:
    print('wrong input')'''

'''i=1
if 10<i<20:
    print('10-20')
elif 20<i<30:
    print('20-30')
else:
    print('ffff')'''


#################
'''
word = input()
valid = False
# both 'a' and 'z' are in lower case
if 'a' <= word[0] <= 'z':
    if word[0] == word[-1]:
        valid = True
if valid:
    print('true')
else:
    print('false')

'''
word = input()
match = False
if word.count('(') == word.count(')'):
    if word.count('[') == word.count(']'):
        if word.count('{') == word.count('}'):
            match = True
if match:
    print('PERFECT!')
else:
    print('IMPERFECT!')






