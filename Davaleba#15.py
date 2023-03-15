text = input("Input: ")

for char in text:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        text = text.replace(char, "")
print(text)