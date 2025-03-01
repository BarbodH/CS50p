def camel_to_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()  # Add an underscore before uppercase letters
        else:
            snake_case += char
    return snake_case.lstrip("_")  # Remove leading underscore if present

camel_case = input("camelCase: ")
snake_case = camel_to_snake(camel_case)
print("snake_case:", snake_case)
