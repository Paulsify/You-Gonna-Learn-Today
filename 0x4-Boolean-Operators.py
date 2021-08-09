'''
This file is all about boolean/logic operators which is another way to compare booleans

There are three operators that you can use; AND, NOT, and OR. These are often capitilized to distinguish them from regular words

AND Operators evaluate to be True when both inputs are True. Versus OR Operators that evaluate to be True if one or the other inputs is True
and NOT Operators simply evaluate to the opposite value

AND, OR and NOT operators have whats called a truth table; a truth table shows every possible result of said operators

##############################################################################################################################################

                AND operator                                     OR Operator                                    NOT Operator
----------------------------------------            --------------------------------------          --------------------------------------
Expression          |   Evaluation                  Expression        |   Evaluation                Expression     |    Evaluation
----------------------------------------            --------------------------------------          --------------------------------------
True and True       |   True                        True or True      |   True                      not True       |    False
True and False      |   False                       True or False     |   True                      not False      |    True
False and True      |   False                       False or True     |   True
False and False     |   False                       False or False    |   False

###############################################################################################################################################
'''
#-------------------------------------------------------------------------------------------------------------------
Bool1 = True
Bool2 = True
Bool3 = False
Bool4 = False
#-------------------------------------------------------------------------------------------------------------------
print('\nThe best thing about a Boolean is even if you are wrong, you are only off by a bit.\n')
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/AND_Operators\______________________________________')
#-------------------------------------------------------------------------------------------------------------------
print('\n---------Bool1 and Bool2---------\n')
print('\t     ',Bool1 and Bool2)
print('\n---------Bool1 and Bool3---------\n')
print('\t     ',Bool1 and Bool3)
print('\n---------Bool3 and Bool2---------\n')
print('\t     ',Bool3 and Bool2)
print('\n---------Bool3 and Bool4---------\n')
print('\t     ',Bool3 and Bool4)
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/OR_Operators\_______________________________________')
#-------------------------------------------------------------------------------------------------------------------
print('\n---------Bool1 or Bool2---------\n')
print('\t     ',Bool1 or Bool2)
print('\n---------Bool1 or Bool3---------\n')
print('\t     ',Bool1 or Bool3)
print('\n---------Bool3 or Bool2---------\n')
print('\t     ',Bool3 or Bool2)
print('\n---------Bool3 or Bool4---------\n')
print('\t     ',Bool3 or Bool4)
#-------------------------------------------------------------------------------------------------------------------
print('________________________________________________________/NOT_Operators\______________________________________')
#-------------------------------------------------------------------------------------------------------------------
print('\n------------NOT Bool1-----------\n')
print('\t     ', not Bool1)
print('\n------------NOT Bool2-----------\n')
print('\t     ', not Bool2)
print('\n------------NOT Bool3-----------\n')
print('\t     ', not Bool3)
print('\n------------NOT Bool4-----------\n')
print('\t     ', not Bool4)
