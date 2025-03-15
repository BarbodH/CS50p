import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        for attempt in range(3):
            try:
                user_answer = int(input(f"What is {x} + {y} = ? "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            if attempt == 2:
                print(f"The correct answer is {correct_answer}")

    print(score)

def get_level():
    while True:
        try:
            level = int(input("Enter level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
