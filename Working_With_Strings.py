'''
This file is all about what you can do with strings

Remember strings can either use single quotes [''] or double quotes [""] double quotes are better for
when you want to use apostrohes.

Think outside the box for uses of this !
'''
#-------------------------------------------------------------------------------------------------------------------
aString = 'Hello, World!'
#-------------------------------------------------------------------------------------------------------------------
print('\nString cheese is my favorite\n')
#-------------------------------------------------------------------------------------------------------------------
print('aString = "Hello, World!"\n')
#-------------------------------------------------------------------------------------------------------------------
print('\n______________________________________________________/Indexing_a_string\__________________________________\n')
#-------------------------------------------------------------------------------------------------------------------
print(len(aString), '<- This is the length of aString (including spaces)\n') # Remember we used len in Input.py; it tells the legth of a string in this case 13 characters.

print(aString.find('o'), '<- Shows index of the first time the letter [o] appears.\n') # NOTE: .find() only works with strings use .index() for lists.

print(aString.find('o',6), '<- Same as above but starts at index #6\n') # For strings you can include a sequence of characters too !

print(aString.find('o',2, -3), '<- It is also possible to define a end parameter\n') # NOTE: Think of negative numbers as reverse order.

print(aString.count('l'), '<- This counts the number of times the letter [l] appears.\n') # That is a lowercase l not a 1 or an i if you could not tell.
#-------------------------------------------------------------------------------------------------------------------
print('\n______________________________________________________/Slices\_____________________________________________\n')
#-------------------------------------------------------------------------------------------------------------------
print(aString[2:10], '<- This is a slice of the string from the index of 2 upto but not including 10\n') # It does not count the 10th index because it makes math easier.

print(aString[2:10:2], '<- This is an extended slice, 2 means it skips every other character\n') # The third number means how many characters to skip to also called a step.

'''
[X:Y] means use X up to and not including Y NOTE: using negative characters will start at the end of the string and go backwards
[X:Y:Z] Means X upto and not including Y and it will step to every Zth character
[X:Y:1] Does not step any characters
[X:Y:2] Steps every 2nd character
[X:Y:3] Steps every 3rd character (more than 2 is called a stride [get it ? because your taking steps])

                  x - x  <-Step
                0 2 3 4
Hello[0:5:3] -> H X X l -> Hl

'''
#-------------------------------------------------------------------------------------------------------------------
print('\n______________________________________________________/[X:Y:Z]_Examples\___________________________________\n')
#-------------------------------------------------------------------------------------------------------------------
print(aString[1:], "<- Leaving off a number on the 'Y' side will print everything after but not including 'X'\n")

print(aString[:5], "<- Leaving off a number on the 'X' side will print everything upto 'Y' but not include it\n")

print(aString[-5:-1], "<- Negative numbers start from 'Y' and go to 'X' number, It does not include either idex\n")

print(aString[::-1], "<- Omitting both 'X' and 'Y' and including a negative 'Z' reverses the string\n") # Remember negative start at the end and go backwards.

print(aString[::-2], "<- Works with steps too !\n")
