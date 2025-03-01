def calculate_tip(amount, percentage):
    tip = amount * (percentage / 100)
    return f"leave ${tip:.2f}"

amount = float(input("Enter amount (e.g. $50.00): ").strip("$"))
percentage = float(input("Enter tip percentage (e.g. 15%): ").strip("%"))

print(calculate_tip(amount, percentage))
