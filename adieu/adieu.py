import inflect
import sys

# Create an inflect engine
p = inflect.engine()

# List to store names
names = []

# Try to collect names until EOF is encountered (Ctrl+D)
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:  # Handle EOFError when Ctrl+D is pressed
    pass

# Format the farewell message
if names:
    # Use the join method from inflect to handle proper punctuation
    farewell_message = f"Adieu, adieu, to {p.join(names)}"
    print(farewell_message)

# Exit with code 0, ensuring clean exit
sys.exit(0)
