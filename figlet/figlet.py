import sys
from pyfiglet import Figlet

figlet = Figlet()

# Get the list of available fonts
fonts = figlet.getFonts()

# Check command-line arguments
if len(sys.argv) == 1:
    # No font specified, use default
    pass
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font = sys.argv[2]
    if font in fonts:
        figlet.setFont(font=font)
    else:
        print("Invalid font")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

# Get user input
text = input("Enter text: ")

# Print ASCII text using the selected font
print(figlet.renderText(text))
