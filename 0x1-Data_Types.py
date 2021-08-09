
"""
In this file you will learn about variables and types of data that can be stored
in those variables

Variables are a way for you to store data and then reference it later

The syntax of which is: name_of_variable = data

There are a few data types that can be stored in a variable
    1. Integers - Integers are whole numbers without a decimal point. They are
       also called int or ints
    2. Floating point - Floating point numbers are numbers that have a decimal
       point. They are also called float numbers or floats
    3. Strings - Strings are a sequence or string of characters. It is often used to print
       text to the screen like was done in Hello_World.py. These are simply
       called strings
    4. Boolean - Variables that are boolean can either be 'True' or 'False'. Often shortened to bool or bools Less common than the other three types.
"""

#----------------------------------------------------------------------------------------------------
# A small example of assigning different varable types.

integer = 7 # Integers can be as big as you want as long as there are no decimal points
floating_point = 6.9 # As with integers any amount of numbers can be added before and after the decimal points
string = 'Spam is delicious' # When assigning a string quotes are used. Either single quotes or double. NOTE:With double it is easier to add apostrophes.
boolean = True #In python it is required for a boolean to be either True or False to be capitilized because python is case sensitive
a, b, c, d = 1, 2.3, 'Bacon is also good', False  # It is possible to assign multiple variables at a time NOTE: Try to name the variable in a way that lets you remeber what it is for

print('This is a integer: ', integer) #When printing more than one thing, be sure to seperate each with a comma
print('This is a float: ', floating_point)
print('This is a string: ', string)
print('This is a Boolean: ', boolean)
print('All the variables: ', a, ' ', b, ' ', c, ' ', d) # Adding spaces can make the output more readable.

'''
Try changing the values and see the output ! NOTE: Boolean can only be True or False

Python is usually read by the computer line by line, top to bottom. If you want to change a variable after assigning it earlier in the program
then make sure it is the same type. There are ways to convert between the data types but thats for another file

'''
