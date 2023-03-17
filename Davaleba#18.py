while True:
    try:
        text = input("Fraction: ")
        x , y = text.split("/")
        x = int(x)
        y = int(y)
        answer = int(x/y*100)
        if x > y:
            continue
    except ValueError:
        print("both numbers must be INT")
    except ZeroDivisionError:
        print("Cant divide on 0")
    else:
        break


if answer >= 99:
    print("F")
elif answer <= 1:
    print("E")
else:
    print(str(answer) + "%")