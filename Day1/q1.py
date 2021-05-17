# Note to self: Dictionary is just JS objects
Dictionary = {
    "Apple": "A red fruit",
    "Ball": "A round play thing",
    "Cat": "A house pet",
    "Dank": "Memes",
    "Spain": "City but the 'S' is silent"
}

print("The dictionary contains the following words:")
tempStr = ""

# looping through the key value pair in the dictionary
for key, value in Dictionary.items():
    tempStr += key + " "

print(tempStr)

userInput = input("Enter the word you wanna look up in the dictionary: ")
print("The meaning of " + userInput + " is " + Dictionary.get(userInput))
