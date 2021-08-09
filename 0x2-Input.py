'''
This is a simple program that uses the variable assignments from Data_Types.py it also
introduces input methods and converting Data_Types
'''
#------------------------------------------------------------------------------------------------------------------
myName = ''
myAge = 0
#------------------------------------------------------------------------------------------------------------------
print('Hello, I am Computer')
print('What is your name ?: ') #Having a print lines seperated like this means each thing will get printed to a new line
myName = input() # There are two ways to do input first is this way, where you print and then ask for input but the second method compounds the two lines.
print('Hello there, ', myName)
print('Your name is ', len(myName), ' characters long.') # 'len' will return the legnth of string in front of it.
#------------------------------------------------------------------------------------------------------------------
print('I was invented around 1940') #Look up the Z1 Computer if you're interested !
myAge = int(input('How old are you ? ')) # Because ,in python 3, input returns a string we must convert it to an integer to operate with it*
print('Wow the difference in our ages is', 79 - myAge, 'years !') #NOTE: Entering a number greater than 79 will cause the difference to be negative.
print('Its good to get to know you !')
print('Bye !') # See ya in a while, crocodile !
#------------------------------------------------------------------------------------------------------------------

'''
* To convert between each data type you put that data type in front of the one to be converted. ie.

string -> integer = int('21')
integer -> string = str(21)
integer -> float = float(21)
float -> integer = int(21.0) <##### Be careful with this one, when converting to int you are losing precision, so it may lead to errors.

NOTE: I think you can figure out float to string and vice versa.
'''
