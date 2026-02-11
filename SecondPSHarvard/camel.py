name = input("Enter a name of a variable in camel case: ")
snake = ""

for char in name:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char
print(snake)
