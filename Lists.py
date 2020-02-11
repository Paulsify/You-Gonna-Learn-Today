'''
This file extends upon the variable assingment learned from
data_types.py.
In this file you will learn about lists, a list is basically exactly
what it sounds like it is; it is a list of variables that can be
treated as a variables individually.
It is possible to pull a variable from the list and add to the list any time that you need.
NOTE: Lists start at zero meaning that the first item in the list is indexed as 0.
The index keeps track of where things are in the list.
List :  [24, 52, 63, 91]
Index:  [0, 1, 2, 3]
24 is in the 0th position on the list; 52 is in the 1st etc..
'''

#---------------------------------------------------------------------------------------------------------------------

my_list = [] # This is the assigning a list to a name. The my_list is initally empty until we add or 'append' it.
another_list = [4, 5, 6] # With another_list we will assign something to it right off the bat.
guess_what_another_list = ['seven', 'eight', 'nine'] # Lists can store all of the different data types.
yet_another_list = [9.1, 9.2, 9.3] # Floating point too.
list_number_five = [True, False, True] # Even boolean values.
edit_this_list = [10, 'eleven', 13] #This list we will edit

#---------------------------------------------------------------------------------------------------------------------
print('\nSanta has a list, you should too\n')

print('\n--------Empty my_list--------\n')
print(my_list) # NOTE: This prints just the brackets because we havent added anything my_list yet.

my_list.append(1) # This adds or 'appends' 1,2,3 to the list.
my_list.append(2)
my_list.append(3)

#---------------------------------------------------------------------------------------------------------------------

print('\n--------my_list--------\n') # NOTE: Just for seperation when viewing output.
print(my_list[0]) # This will print the first thing in a list.
print(my_list[1])
print(my_list[2])

print('\n--------another_list--------\n')
print(another_list[0])
print(another_list[1])
print(another_list[2])

print('\n--------guess_what_another_list--------\n')
print(guess_what_another_list[0:]) # This will print everything; It prints everything from the 0th position to the end. (NOTE: It will all be on the same line and include brackets).

print('\n--------yet_another_list--------\n')
print(*yet_another_list) # This will also print everything. * means a wildcard or everything in programming.

print('\n--------list_number_five--------\n')
print(*list_number_five, sep = '\n') # Adding the 'sep = \n' mean to seperate the elements of the list by a new line.

'''
'\n' is whats called an escape sequence or escape character its a special set of characters that python interpets in a special way
in the case of \n it creates a new line wherever it is placed.
The other very commonly used one is \t which creates a tab, or four spaces, equal to pressing the tab button.
'''

#---------------------------------------------------------------------------------------------------------------------
print('\n--------edit_this_list--------\n')
print(*edit_this_list) # Printing the original list for reference.

edit_this_list[1] = 11 # This will change the 2nd element in the list to 11 instead of 'eleven'.

print(*edit_this_list) # Prints the edited list.

spam = 12 #Variable to change NOTE: Try changing this.

edit_this_list[2] = spam # This will change the 3rd element of the list to whatever spam is.

print(*edit_this_list) # Prints the edited list.

#---------------------------------------------------------------------------------------------------------------------
print('\n--------CO-CO-CO-COMBO-BREAKER!!!!--------\n')
print(*my_list, *another_list, *guess_what_another_list, *yet_another_list, *list_number_five, *edit_this_list) #You should be able to figure out this one ;)
