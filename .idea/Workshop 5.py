numbers = [3,1,4,1,5,9,2]

print(numbers[0])
print(numbers[-1])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6,5,3])

numbers[0] = "ten"
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])

print(numbers.__contains__(9))

# incomes = []
# months = int(input("How many months? "))
#
# for month in range(1, months + 1):
#     income = float(input("Enter income for month {0}:".format(month)))
#     incomes.append(income)
#
# print("\nIncome Report\n-------------")
#
# total = 0
# for month in range(1, months + 1):
#     income = incomes[month - 1]
#     total += income
#     print("Month {:2d} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

#
# numbers = []
# for i in range(5):
#     number = int(input("Number:"))
#     numbers.append(number)
# print("The first number is", numbers[0])
# print("The last number is", numbers[-1])
# print("The smallest number is", min(numbers))
# print("The Largest number is", max(numbers))
# print("The average of the numbers is", sum(numbers)/len(numbers))

# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
# 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
# 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# username = input("Enter username:")
# if username in usernames:
#     print("Access granted")
# else:
#     print("Access denied")


# import random
#
# line = int(input("how many quick picks"))
# for i in range (line):
#     lottoNums = random.sample(range(48),6)
#
#     list(set(lottoNums))
#
#     while lottoNums.__sizeof__() < 6:
#         collectioncollection.append(random.randint(range(48)))
#         list(set(lottoNums))
#
#     lottoNums.sort()
#     list_str = str(lottoNums)
#     print(list_str.strip('[]'))
