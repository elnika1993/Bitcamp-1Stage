text = input("Enter The Text: ")
snake = ""

for char in text:
    if char.isupper():
          snake += "_" + char.lower()
    else:
        snake += char
print(snake)