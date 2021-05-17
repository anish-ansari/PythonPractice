import random
import time  # to use a delay in the program I imported time
import os  # to clear my console I imported os


# a function that clears the console window
def clear(): os.system('cls')


# list is just arrays
list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tempStr = " "
print("This is a list of numbers: " + tempStr.join(list))
time.sleep(2)
print("Computer is guessing a random number...")
time.sleep(2)
# .choice chooses a random value from the provided list
randomValue = random.choice(list)
print("Done")
time.sleep(1)
clear()
userInput = input("What do you think the computer guessed?: ")
if userInput == randomValue:
    print("You guessed correct!")
    print("The correct answer was " + userInput + " after all")
else:
    print("Wrong guess!")
    print("The correct answer was: " + randomValue)
