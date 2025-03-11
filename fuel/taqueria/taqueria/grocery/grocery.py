# Create an empty list to store the grocery items
items = []

# Read input until EOF (Ctrl + D)
while True:
    try:
        grocery = input()  # Take input
        items.append(grocery)  # Append to the list
    except EOFError:
        break

# Create an empty dictionary to count occurrences of each item
item_count = {}

# Count the occurrences of each item
for item in items:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1


for item in sorted(item_count):
    print(f"{item_count[item]} {item.upper()}")
