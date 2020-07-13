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

  # Another way to increment through a list is using the range function.
  for z in range(0, len(nums)):   # Create variable z at index 0
    print(nums[z])                # Print value at index at every iteration
  # It will repeat as many times as there are values in nums. (len = length)

  print("\n_______FOR... ELSE_______")
  # The for loop can include an "else" block.
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

main()