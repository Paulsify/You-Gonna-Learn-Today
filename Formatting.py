'''
This File is all about formatting the output of string and numbers plus a few tips
'''
#-------------------------------------------------------------------------------------------------------------------
name = 'Jimothy'
integer = 23
data = ('Jimothy', 'McDonald', 22.15)
formatString = "Hello %s %s, The total cost of your meal is $%s"
float = 54.164378
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/Formatting with modulo (%) operator\__________________________')
#-------------------------------------------------------------------------------------------------------------------
print('My name is %s' % name) # %s means string and will fill in with whatever string is on the end
print('I am %d years old' % integer) # %d actually stands for decimal, not integer as other bases can be use ie. hexadecimal or octal
print('This is an octal number: %o'%(23)) # alternatively the variable can be added in the same print line after the quotes.(In this case it is written in octal or base 8 hence the o for octal).
print('Perhaps you like hexadecimal? %x'%(255)) # x for heXadecimal
print ('My name is %s and I am %d years old' % (name, integer)) # Combining operators is also possible
print(formatString % data) #This is another form of combination. It inserts the variables from 'data' into 'formatString'
print ('I am floating %.2f meters above the ground' % float) # %.Xf will shorten the float to X digits after the decimal
print('The sailboat is floating %3d centimeters from the dock' % (6))# the 3 in front of the d is for the width or how many spaces to use for the print, if the amount of digits is less it will be filled with blanks.
print('The rowboat is floating %4d centimeters from the dock' % (253))# this allows for you to line up things, 1 is added to the decimal width as sailboat has an extra letter.
print('The floats on the airplane are %5.2f milimeters out of alignment' % (5.334))# Works with floats too

'''
%d – integer
%f – float
%s – string
%x – hexadecimal
%o – octal
'''

print('________________________________________________________/Formatting with the format method\__________________________')

#NOTE: Formatting with the format method is very similar to the modulo operator

print('My favorite movies are {} and {}'.format('The Terminator','Wall-E'))# The data in the .format() method is used in place of the brackets when printing
print('{0} and {1} went to the store'.format('Jack','Jill'))# Adding a position argument to a format method,if you remeber from lists, things start at 0.
print('{1} and {0} went to the store'.format('Jack','Jill'))# You can use this to switch positions of variables
print('My name is {1} and my favorite ice creams are {0} and {ice_cream}'.format('Chocolate', 'Jeremy', ice_cream = 'Strawberry'))# Variables can be assigned in the format method !
print('The box is {0:3d} inches by {1:3.2f} inches'.format(12, 6.546))# works with float and decimal width flags.
print('{s} and {f} climbed mount doom'.format(s = 'Sam', f = 'Frodo'))# alternatively variables work as well

print('________________________________________________________/Formatting with the string method\__________________________')

mystr = 'String cheese is my favorite snack.'

print('Center aligned with fill character')
print(mystr.center(40, '-'),'\n')
print('Left aligned with fill character')
print(mystr.ljust(40, '-'), '\n')
print('Right aligned with fill character')
print(mystr.rjust(40, '-'), '\n')
