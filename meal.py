def convert(time):
    hours, minutes = map(int, time.split(":"))  # Convert time to integers
    return hours + minutes / 60  # Convert to decimal hours

def main():
    time = input("Time: ").strip()
    hour = convert(time)

    # Check and print the correct meal time
    if 7 <= hour <= 8:
        print("breakfast time")  # Fixed case to match expected output
    elif 12 <= hour <= 13:
        print("lunch time")  # Fixed case
    elif 18 <= hour <= 19:
        print("dinner time")  # Fixed case

# Test convert function (for debugging)
if __name__ == "__main__":
    main()
