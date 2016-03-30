import math
# sales = float(input("Enter sales: $"))
# while sales > 0:
#     if sales < 1000:
#         bonus = sales * 0.1
#     else:
#         bonus = sales * 0.15
#     print("Bonus is $", bonus, sep='')
#     sales = float(input("Enter sales: $"))
# print("No Bonus for you then!")
#
# name = input("Name: ")
# while name != "":
#     print("hello", name,", my good chum!")
#     name = input("Name: ")
# print("Goodbye")
#
# for i in range(1,21,2):
#     print(i, end=' ')
# print()
#
# for i in range(0,110,10):
#     print(i, end=' ')
# print()
#
# for i in range(20,0,-1):
#     print(i, end=' ')
# print()
#
# score = float(input("Enter score:"))
# if 0 < score < 100:
#     if score > 90:
#         print ("Excellent")
#     elif score > 50:
#         print("Passable")
#     else:
#         print("Bad")
# else:
#     print("Invalid score")
#
# name = input("Enter Name")
# menu = input("(H)ello (G)oodbye (Q)uit")
# while menu != "Q":
#     if menu == "H":
#         print("hello", name)
#         menu = input("(H)ello (G)oodbye (Q)uit")
#     elif menu == "G":
#         print ("goodbye", name)
#         menu = input("(H)ello (G)oodbye (Q)uit")
#     else:
#         print("Invalid choice")
#         menu = input("(H)ello (G)oodbye (Q)uit")
# print("Finished")


# itemNumber = int(input("Enter number of items"))
# while itemNumber <0:
#     print("Invalid item number")
#     itemNumber = int(input("Enter number of items"))
# CostPerItem = int(input("Enter cost per item"))
# ShippingCost = itemNumber * CostPerItem
# print("Shipping Cost is $",ShippingCost)

#
# print ("Number sequence generator")
# menu = input("1:Even numbers 2:Odd numbers 3:Squares 4:Exit")
# while menu != "4":
#     if menu == "1":
#         x = int(input("Enter first number"))
#         y = int(input("Enter second number"))
#         for i in range (x, y, 2):
#             print(i, end=' ')
#         print()
#         menu = input("1:Even numbers 2:Odd numbers 3:Squares 4:Exit")
#     elif menu == "2":
#         x= int(input("Enter first number"))
#         y = int(input("Enter second number"))
#         for i in range (x, y ,3):
#             print(i, end=' ')
#         print()
#         menu = input("1:Even numbers 2:Odd numbers 3:Squares 4:Exit")
#     elif menu == "3":
#         x= int(input("Enter first number"))
#         y = int(input("Enter second number"))
#         for i in range (x, y, 1):
#             if(float(math.sqrt(i)) % 1 == 0):
#                 print(i, end=' ')
#         print()
#         menu = input("1:Even numbers 2:Odd numbers 3:Squares 4:Exit")
# print("Goodbye!")






#Week 4

# import random
#
# __author__ = 'Lindsay Ward'
# MAX_INCREASE = 0.1  # 10%
# MAX_DECREASE = 0.05  # 5%
# MIN_PRICE = 1.00
# MAX_PRICE = 100.00
# INITIAL_PRICE = 10.0
#
#
# day = 0
# price = INITIAL_PRICE
# print("Starting price: ${:,.2f}".format(price))
#
# while price >= MIN_PRICE and price <= MAX_PRICE:
#     priceChange = 0
#     # generate a random integer of 1 or 2
#     # if it's 1, the price increases, otherwise it decreases
#     if random.randint(1, 2) == 1:
#         # generate a random floating-point number
#         # between 0 and MAX_INCREASE
#         priceChange = random.uniform(0, MAX_INCREASE)
#     else:
#         # generate a random floating-point number
#         # between negative MAX_INCREASE and 0
#         priceChange = random.uniform(-MAX_DECREASE, 0)
#
#
#     price *= (1 + priceChange)
#     day = (1+ day)
#     print("on day ", day ," price is: ${:,.2f}".format(price))

# try:
#     numerator = int(input("Enter the numerator:"))
#     denominator = int(input("Enter the denominator:"))
#     fraction = numerator/denominator
#     print (fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished")

#
# lower = input("lower = ").strip(' ')
# upper = input("upper = ").strip(' ')
# print("Enter a number:({}-{})".format(lower,upper))
#
# for i in range(int(lower), int(upper), 1):
#     print("{0} {1:>5}".format(i,chr(i)))


# finished = False
#
# result=0
# while not finished:
#     try:
#         result = int(input("Enter an integer"))
#     except ValueError:
#         print("Please enter a valid integer")
#
# print("valid result is",result)


# outFile = open("name.txt","w")
# name = input("What is your name?")
# print(name, file=outFile)
# outFile.close()
#
# in_file = open("name.txt","r")
# name = in_file.read().strip()
# print("Your name is", name)
# in_file.close()
#
# in_file = open("numbers.txt", "r")
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# print(number1 + number2)
# in_file.close()
#
# in_file = open("numbers.txt", "r")
# total = 0
# for line in in_file:
#     number = int(line)
#     total += number
# print(total)
# in_file.close()


MINIMUM_LENGTH = 5
MAXIMUM_LENGTH = 15

print("Please enter a valid password")
passwordChecker = input("Your password must be between 5 and 15 characters, and contain: 1 or more upperchase characters 1 or more lowercase characters 1 or more numbers and 1 or more special characters:!@#$%^&*()_-=+`~,./o'[]\<>?0{}")

