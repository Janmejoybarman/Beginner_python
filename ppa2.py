'''word=input()
present=False
if ('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
    if (word.index('a')< word.index('e') < word.index('i') <word.index('o') <word.index('u')):
        if(word.count('a')>= word.count('e') >= word.count('i') >=word.count('o') >=word.count('u')):
            present=True
if(present):
            print('It is a perfect word')
else:
    print('It is not a perfect word')'''
'''

alpha='abcdefghi'
n=input()
m=input()                                                 ###problem on chess (bishop move)
#first coordinare
x=int(alpha.index(n[0])+1)
y=int(n[1])
#2nd cooordinate
x1=int(alpha.index(m[0])+1)
y1=int(m[1])
#slope
if ((abs(y-y1)/(x-x1))==1):
    print('yes')
else:
   print('no')
'''
'''a,b,c,d=input()
#print('\n',a,'\n',b,'\n',c,'\n',d)
print(a,b,c,d)
'''
print('\\hello\\')










