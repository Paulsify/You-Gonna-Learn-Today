
"""
In this file you will learn about variables and types of data that can be stored
in those variables
#-------------------------------------------------------------------------------
Variables are a way for you to store data and then reference it later

The syntax of which is: name_of_variable = data

There are a few data types that can be stored in a variable
    1. Integers - Integers are whole numbers without a decimal point. They are
       also called int or ints
    2. Floating point - Floating point numbers are numbers that have a decimal
       point. They are also called float numbers or floats
    3. Strings - Strings are a sequence of characters. It is often used to print
       text to the screen like was done in Hello_World.py. These are simple
       called strings
    4. Boolean - Variables that are boolean can either be 'True' or 'False'
"""

# A small example of assigning different varable types.

integer = 7 #An integer value has no decimal points, it can be as big as you want as long as there are no decimal points
floating_point = 6.9 # A floating point number contains a decimal point, as with integers any number of numbers can be added after the decimal points
string = "This is a string" # When assigning a string double quotes are used to let python know that the sequence of characters in the quotes are the ones to be assigned
boolean = True #A boolean variable is either True or False; In python it is required for either of them to be capitilized because python is case sensitive

print("These are my data types: " , integer, floating_point, string, boolean) #When printing more than one variable be sure to seperate each with a comma
