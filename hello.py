# print("Hello World!")
# print("My name is Yao.")

# # ctrl+/ is how we make a comment
# # this is a string example
# learner = "optimus Prima"
# print(learner)

# # this is a number/integer example
# ideal_number_of_pets = 2
# print(ideal_number_of_pets)

# # This a float/decimal example
# how_much_is_a_banana = 9.99
# print(how_much_is_a_banana)

# # This is an example of a Boolean True/False
# is_our_pets_vaccinated = True
# print(is_our_pets_vaccinated)

# print(type(ideal_number_of_pets))
# print(type(how_much_is_a_banana))
# print(type(learner))
# print(type(is_our_pets_vaccinated))

# is_it_a_number = 333
# is_this_a_number = "333"

# print(type(is_it_a_number))
# print(type(is_this_a_number))

# statement = "The number of pets I want is 2 dogs."

# puppy_name = "Buddy"
# what_is_buddy_age = 3
# how_old_is_colton = 21.5
# is_line_36_true = True
# zipcode = '100001'

# # print(statement)
# print(statement)
# print(statement)

# print(5+3)
# print(5*3)
# print(5-3)
# print(5/3)

# print(10/5)
# print(7/3)
# print(12/4)
# print(99/8)

# Example of modulo
# print(10%3)
# print(10/3)
# print(10%5)

# # show an example of an exponent "power to the 5th"
# print(2**5)
# print(2**2)
# print(32**12)

# find the area of a ectangle
# length = int(input("What is the length?"))
# width = int(input("What is the width"))
# area = length * width
# print(f"The area of rectangle is {area}.")

# # find the tax amount
# price = 9
# tax = price * 0.08
# print(tax)

# # find the average
# avg = (10+10 +10)/3
# print(avg)

# # Ask the user their favorite color
# fav_color = input("What is your favorite color?")

# print(f"Your favorite color is {fav_color}")

# This is a comment to test multiple input
# print('This', 'is', 'a', 'sample.')
# print(12, 24, -2, sep=':')
# print('but', 'not', 'including', sep='**')
# print('but', 'not', 'including', sep='')

# create a receipt
# customerName = input("Enter customer's name: ")
# itemPrice = float(input("What is the price of the item?"))
# quantity = int(input("Enter quantity:"))
# totalCost = itemPrice*quantity
# roundedCost = round(totalCost,2)

# print("Receipt")
# print("-------------------")
# # customer name
# print(f"Customer: {customerName}")
# # the price of what they purchased
# print(f"Item price: ${itemPrice}")
# # the quantity of the product they purchase
# print(f"Quantity: {quantity}")
# # the total cost
# print(f"Total Cost: ${roundedCost}")

# # This is my additional code 
# print("This is an additional line.")

# str practice
# s = 'Hello World!'
# print(s[0])
# print(s[2:5])
# print(s[3:])
# print(s*2)
# print(s+'Everyone!')
# print(s.lower())
# print(s.replace('l','s'))
# print(len(s))
# print(s.strip())
# print(s.split(' '))

# MyInteger= 10
# print(type(MyInteger))
# # Converting integer to String
# integerToStr = str(MyInteger)
# print("Integer into String: ", integerToStr)
# print(type(integerToStr))

#initializing and declaring variable and value
# floatNumberOne=11.10
# floatNumberTwo = 2/5
# print(floatNumberOne)
# print(floatNumberTwo)
# # checking data type
# print(type(floatNumberOne))
# print(type(floatNumberTwo))
# # # Converting float to String
# MyStringOne = str(floatNumberOne)
# MyStringTwo = str(floatNumberTwo)
# print("Floating point into String: ", MyStringOne)
# print("Floating point into String: ", MyStringTwo)
# # # checking data type
# print(type(MyStringOne))
# print(type(MyStringTwo))

# mylist=[] # create a empty list
# print(mylist)
# # Create a list of strings.
# string_list = ["Hello", "Python", "World"]
# print(string_list[2])
# # Create a list of numbers.
# number_list = [3, 4, 5, 6, 8, 10]
# print(number_list)
# # Create a list of boolean values.
# boolean_list = [True, False, False, True]
# print(boolean_list)
# # Create a mixed list or list with heterogeneous data
# mixed_list = [3, 4, "Python", True]
# print(mixed_list)

# Create a string.
# my_string = "Hello World"
# # Create a list of characters from my_string.
# character_list = list(my_string)
# # Create a list of substrings from my_string.
# substring_list = my_string.split()
# # Print the results.
# print(my_string) # Output: "Hello World"
# print(character_list) # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# print(substring_list)

# my_list = [1, "Hello Python", 7.98]
# # Output: 'Hello Python'
# print("before: ", my_list[1])
# # Output: 'Hello JavaScript'
# my_list[1] = "Hello JavaScript"
# print("after: ", my_list[1])

# append vs 
# my_list1 = []
# # Add elements to the list using append().
# my_list1.append(1)
# my_list1.append(2)
# my_list1.append(3)
# print(my_list1)

# # Create an empty list.
# #my_list2 = []
# # Add elements to the list using extend().
# my_list1.extend([1, 2, 3])
# # Print the new list.
# # Note that my_list *is* modified.
# print(my_list1)

# insert
# my_list = [1, 2, 4, 5]
# # Insert elements using insert().
# my_list.insert(2, 3)
# # Print the new list.
# # Note that my_list *is* modified.
# print(my_list) # output: [1, 2, 3, 4, 5]

# Concatenating two Lists
# Create two lists.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# # Add elements to the list using append().
# new_list = list1 + list2
# # Print the new list.
# print(new_list) # output: [1, 2, 3, 4, 5, 6]

# print(9+4)
# print('My ' + 'Apple')

# Create a list.
# my_list = [1, 2, 3, 4, 5]
# # # Traverse the list with a for loop.
# # for element in my_list:
# #     print(element)
# # Traverse the list by accessing the
# # indexes with the range() and len() functions.
# for i in range(len(my_list)):
#     print(f"Index {i} contains: {my_list[i]}")


# Create a two-dimensional list with three sublists.
# Each sublist contains three elements.
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Print the middle element of the 2D list.
# # Remember that list indexes start at 0.
# # print(my_list[1][1])

# # Iterate through each sublist.
# for sublist in my_list:
# # Iterate through each sublist element.
#     for element in sublist:
#         print(element)

# Define a nested list called 'nums' that contains various data types.
nums = [1, 2, 3, [4, 5, 6, [7, 8, [9]]], 10]
# Access and print individual elements in the 'nums' list:
print(nums[0]) # Output: 1
print(nums[1]) # Output: 2
print(nums[3]) # Output: [4, 5, 6, [7, 8, [9]]]
print(nums[4]) # Output: 10
# Accessing and printing the element at index 0 of the nested list at index 3.
print(nums[3][0]) # Output: 4
# Accessing and printing the entire nested list at index 3.
print(nums[3][3]) # Output: [7, 8, [9]]
# Accessing and printing the element at index 0 of the deeply nested list at index 3 of the main list.
print(nums[3][3][0]) # Output: 7
# Accessing and printing the entire deeply nested list at index 2 of the nested list at index 3.
print(nums[3][3][2]) # Output: [9]

