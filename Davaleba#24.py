import inflect

p = inflect.engine()
names = []

while True:
    try:
        text = input("Name: ")
        names.append(text)
    except EOFError:
        print("Adiu, adiu, to " + p.join(names))
        break
