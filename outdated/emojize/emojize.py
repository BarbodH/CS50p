import emoji

user_input = input("Input: ")
emoji = (emoji.emojize(user_input , language = "alias"))
print("Output: " , emoji)
