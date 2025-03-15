def main():
    name = input("Input: ")
    print("Output:", shorten(name))

def shorten(word):
    vowels = "aeiouAEIOU"
    for letter in vowels:
        word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()
