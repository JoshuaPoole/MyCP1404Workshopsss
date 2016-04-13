
# STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC":"Victoria", "TAS":"Tasmania"}
#
# state = input("Enter short state: ").upper()
# while state != "":
#     if state in STATE_NAMES:
#         print(state, "is", STATE_NAMES[state])
#     else:
#         print("Invalid short state")
#     state = input("Enter short state: ").upper()

# COLOR_NUMBERS = {"RED": "#ff0000", "YELLOW": "#FFFF00", "PINK": "#FFC0CB", "GREEN": "#008000", "PURPLE": "#800080", "ORANGE": "#FFA500", "BLUE": "#0000FF",}
#
# colors = input("Enter a color name from the Sing a Rainbow Song to see it's hexadecimal code").upper()
# while colors != "":
#     if colors in COLOR_NUMBERS:
#         print(colors, "'s hexadecimal colour code is", COLOR_NUMBERS[colors])
#     else:
#         print("That colour is not in the list")
#     colors = input("Enter color name (no spaces)").upper()

dictionary = {}

string = input("Enter a string")
word = string.split(" ")

for key in word:
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

for key in dictionary:
    print(key,':',dictionary[key])



