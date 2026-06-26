# If statements 
# is used to compare things

# variable = input("This is an input:")
# print(variable)
# height = int(input("How tall are you?"))
# # height >= 48
# if height >= 48:
#     print("You many ride")
# else:
#     print("Sorry kid, get lost. Come back next year.")

# create a password checker
# username = HotWater
# password = blue

# password = "bluepen"

# userLoginInput = input("Enter Password: ")

# if userLoginInput == password:
#     print("Open")
# else:
#     print("Wrong password")

# check if number is even of odd
# number = int(input("What's your number?"))

# if number%2 == 0:
#     print("Your number is an even number.")
# else:
#     print("Your number is an odd number.")

# for number in range(1, 152):
#     print(number)

# for number in range(10, 0, -1):
#     print(number)

# numberOfEgg = int(input("How many eggs do you have?"))

# for i in range(numberOfEgg, 1, -1):
#     print(f"{i} eggs in the box.")

# What is the sum of 1 to 427

# total = 0

# for number in range(1,428):
#     total += number

# print(f"The sum of 1 - 427 is: {total}")

# password = "bluepen"

# userLoginInput = input("Enter Password: ")

# while userLoginInput != password:
#     print("Wrong password - please try again.")
#     userLoginInput = input("Enter Password: ")
# else:
#     print("Open!")
    
# find the largest number
# numberList = [7, 42, 8, 946, -1, 4235, 6, 730]
# LargestNumber = numberList[0]

# for number in numberList:
#     if number > LargestNumber:
#         LargestNumber = number

# print(f"Lasgest Number is {LargestNumber}")

secretnumber = 7

guess = int(input("Guess a number: "))

while guess != secretnumber:
    print("Wrong number.")
    uess = int(input("Guess again: "))

print(f"You got it! Secret number is {secretnumber}")