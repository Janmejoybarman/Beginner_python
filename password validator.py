'''
password=input()
first_el=password[0]
len_pass=len(password)

if (8<=len_pass<=32):
    if (first_el.isalpha()):
        if (' ' in password == False):
               if ("=" in password ==False):
                     if ("'" in password ==False):
                          if ('"' in password ==False):
                               if ("\\" in password ==False):
                                   if ("/" in password == True):
                                       print('True')

                                   else:
                                       print('spa')

                               else:
                                 print('backslash')
                          else:
                             print('dq')
                     else:
                        print('False')
               else:
                 print('equal')
        else:
          print('spACE')
    else:
       print('not 1st latter is alphabet')
else:
  print('not 8word')

'''
'''
password=input()
first_el=password[0]
len_pass=len(password)

if (8<=len_pass<=32):
    if (first_el.isalpha()):
        if ('/' in password):
            print('False')
        if ('=' in password):
            print('equal')
        if ("'" in password):
            print('quote')
        if ('"' in password):
            print('dq')
        if ("\\" in password ):
            print('backslash')
        if (' ' in password):
            print('space')
        elif :
            print('False')
    else:
        print('False')
else:
    print('False')
'''
'''
if (' ' in password ==False):
    if ("/" in password == False):
'''
        
password=input()
first_el=password[0]
len_pass=len(password)

if (8<=len_pass<=32):
    if (first_el.isalpha()):
        if ("/" in password):
            print('forward-slash')
        elif ('=' in password):
            print('equal')
        elif ("'" in password):
            print('quote')
        elif ('"' in password):
            print('dq')
        elif ("\\" in password ):
            print('backslash')
        elif (' ' in password):
            print('space')
        else:
            print('True')
    else:
        print('False')
else:
  print('Wrong passsword')