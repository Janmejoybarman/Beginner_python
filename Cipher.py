'''alpha='abcdefghijklmnopqrstuvwxyz'
i=23
print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])
print(alpha[(i+3)%26])
print(alpha[(i+4)%26])'''

'''x='india'
print(x[3])            #prints (i)3rd alphabet in the string
print(x.index('d'))'''    #prints (2) index of d in word india


alpha="abcdefghijklmnopqrstuvwxyz"
#malda to be print as nbmeb

x='abcde'
i=0
t=''
k=2
t=t+(alpha[(((alpha.index(x[i]))+k)%26)])
t=t+(alpha[(((alpha.index(x[i+1]))+k)%26)])
#t=t+alpha[((alpha.index(x[2]))+1)]              #POPULARLY CALLED AS CAESAR CIPHER IN CRYPTOGRAPHY
t=t+(alpha[(((alpha.index(x[i+2]))+k)%26)])
t=t+(alpha[(((alpha.index(x[i+3]))+k)%26)])
t=t+(alpha[(((alpha.index(x[i+4]))+k)%26)])
print(t)