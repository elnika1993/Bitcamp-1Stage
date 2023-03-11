answer = input("Greeting: ")

if answer.lower().startswith("hello"):
    print("$0")
elif answer.lower().startswith("h"):
    print("$20")
else:
    print("$100")