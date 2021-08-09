'''
Comparison operators are the same as in regular math but in python and most programming launguages they may look a little different

Operator |   Meaning
--------------------------
==       | Equal to                           [=] is not the same as [==],[=] is for assignment and [==] means equal to
!=       | Not equal to
<        | Less than
>        | Greater than
<=       | Less than or equal to
>=       | Greater than or equal to
'''
#-------------------------------------------------------------------------------------------------------------------
num1 = 1
num2 = 2
num3 = 1
num4 = 2.0
string1 = 'dog'
string2 = 'cat'
string3 = 'dog'
Bool1 = True
Bool2 = False
Bool3 = True

# NOTE: You can not do the same with booleans because in python, Booleans can only be True and False #NOTE: remember bools are case sensitive !
#-------------------------------------------------------------------------------------------------------------------
print('\nOperation Python is a go !\n') #\n means newline meaning that adding this will add a blank line where the \n is
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/Integers_and_Floats\________________________________')
#-------------------------------------------------------------------------------------------------------------------
# NOTE: Try and guess what each one will be before running it !

print('\n---------num1 == num2---------\n')
print('\t   ',num1 == num2) #\t is to denote adding a tab in the output.
print('\n---------num1 == num3---------\n')
print('\t   ',num1 == num3)
print('\n---------num2 == num4---------\n') # NOTE: num4 is 2.0 which means it is a float, but 2.0 is still 2 
print('\t   ',num2 == num4)
print('\n---------num1 != num2---------\n') # Remeber this means is not equal to which in this case is True
print('\t   ',num1 != num2)
print('\n---------num1 < num2----------\n')
print('\t   ',num1 < num2)
print('\n---------num1 > num2---------\n')
print('\t   ',num1 > num2)
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/Strings\____________________________________________')
#-------------------------------------------------------------------------------------------------------------------
print('\n-----string1 == string2------\n') # NOTE: You can do strings as well but <,>,<=,>= do not apply to strings.
print('\t   ',string1 == string2)
print('\n-----string1 == string3------\n')
print('\t   ',string1 == string3)
print('\n-----string1 != string2------\n')
print('\t   ',string1 != string2)
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/Booleans\___________________________________________')
#-------------------------------------------------------------------------------------------------------------------
print('\n-------bool1 == bool2--------\n') # NOTE:  Even booleans too ! It is the same as with strings, <,>,<=,>= do not apply.
print('\t   ',Bool1 == Bool2)
print('\n-------bool1 == bool3--------\n')
print('\t   ',Bool1 == Bool3)
print('\n-------bool1 != bool2--------\n')
print('\t   ',Bool1 != Bool2)
