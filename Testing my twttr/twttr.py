def main():
    text = input("Enter the text: ")
    print(shorten(text))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_text = ""
    for i in range(len(word)):
        if word[i].lower() not in vowels:
            new_text += word[i]
    return new_text
            

if __name__ == "__main__":
    main()