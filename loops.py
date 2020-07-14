# Author: @whydoesitmatter
# Date: 7/13/2020
# Description: loops

def main():
  # Loops are pieces of code that repeat.

  print("\n_______WHILE LOOPS_______")

  # This is a while loop.
  # It will repeat while the statement given is true.

  x = 0             # Create variable x at 0
  while(x < 7):     # Loop while x < 7
    print(x)        # Print x on every iteration
    x += 1          # Add 1 to x every iteration

  print("\n________FOR LOOPS________")

  # There are also for loops.
  # For loops are used when you know the number of times it should repeat.
  # Here we are using the range function.

  for y in range(0, 7):   # Create variable y at 0
    print(y)              # Print y every iteration

  # For loops automatically increment every iteration.
  # This will repeat 7 times. (0-6)

  print("\n_____FOR LOOPS CONT._____")

  # For loops are commonly used to loop through lists.

  nums = [0, 10, 20, 30, 40, 50, 60]  # Create list
  for val in nums:                    # Start at beginning of list
    print(val)                        # Print value at every iteration

  # This for loop also automatically increments at the end of each iteration.
  # However, it increments val by one index in the list.

  print("")

  # Another way to increment through a list is using the range function.

  for z in range(0, len(nums)):   # Create variable z at index 0
    print(nums[z])                # Print value at index at every iteration

  # It will repeat as many times as there are values in nums. (len = length)

  print("\n__________ELSE___________")

  # The while loop can include an "else" block.
  # The "else" will execute when the statement becomes false.

  x = 0
  while (x < 7):
    print(x)
    x += 1
  else:
    print("x is now equal to 7 \n")
  
  # The for loop can also include an "else" block.
  # The "else" will execute when it is done iterating.

  names = ["salty", "kuma", "witchy"]
  for i in names:
    print(i)
  else:
    print("There are no more names. \n")

  # There can also be a break statement.
  # This executes the else ONLY IF the break is not run.
  
  name1 = "ciceroll"          # Create a sample name
  for j in names:             # Loop through list
    if (j == name1):          # If a name in list equals sample name
      print("This name exists in the database. \n")
      break
  else:                       # If no name in list equals sample name
    print("No such name exists in the database. \n")

  print("\n________CONTINUE_________")

  # When a "continue" statement is hit, you will return to the top of the loop.
  # Here is an example of a "continue" statement in a while loop, comparable to a do while loop.
  # Do while loops execute once before checking the statement.
  # Here, we increment once before checking if y is divisible by 2.

  y = -1                # The increment exists at the beginning
  while (y < 7):
    y += 1              # This has to come before the "if" or it will loop forever
    if (y % 2 != 0):    # If y is not divisible by 2, the below statement will be executed
      continue        # This statement will skip anything AFTER it
    print(y)
  
  print("")

  # Here is an example of a "continue" statement in a for loop.

  for letter in "Pythons":
    if letter == "s":       # Skip the letter "s"
      continue
    print(letter)

  print("\n______NESTED LOOPS_______")

  # You can also nest a loop inside another loop.

  list = [("salty", "d.va", "mercy"), ("kuma", "torbjorn", "reinhardt"), ("witchy", "moira", "junkrat")]

  for r in range(0, 3):       # For row, there are 3 values per row (0-2)
    for c in range(0, 3):     # For column, there are 3 values per column (0-2)
      print(list[r][c])       # Print data at every loop
    print("")                 # Create a break between rows

  # This should follow the pattern:
  # [0][0], [0][1], [0][2]
  # [1][0], [1][1], [1][2]
  # [2][0], [2][1], [2][2]

main()
