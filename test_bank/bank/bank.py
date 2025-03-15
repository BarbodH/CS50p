def main():
    answer = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    answer.strip().lower()
    if answer[0] == "h" and answer != "hello":
        return "$20"
    elif answer == "hello":
        return "$0"
    else:
        return "$100"

if __name__ == "__main__":
    main()
