name = input("Input: ")

letters = ["a" , "e" , "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U"]

for letter in letters:
    if letter in name:
        name = name.replace(letter , "")

print("Output: " , name)
