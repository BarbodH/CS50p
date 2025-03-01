expression = input("Expression: ").strip().split()

num1 = float(expression[0])
operator = expression[1]
num2 = float(expression[2])

if operator == "+":
    print(float(num1 + num2))
elif operator == "-":
    print(float(num1 - num2))
elif operator == "*":
    print(float(num1 * num2))
elif operator == "/":
    print(float(num1 / num2))
else:
    print("Invalid operator")
