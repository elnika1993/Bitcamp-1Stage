def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    return text
    

def main():
    text = input("enter the text: ")
    text = convert(text)
    print(text)

main()