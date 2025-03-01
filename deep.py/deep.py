something = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

answers = [42, "forty-two", "forty two", "Forty Two"]

if something.isdigit():
    something = int(something)

if something in answers:
    print("Yes")
else:
    print("No")
