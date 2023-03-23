import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            level = int(input("Enter Level: "))
            if 0 < level < 3:
                print(f"level: {level}")    
                return level
        except ValueError:
            continue


def generate_integer(level):
    score = 0
    for i in range(10):
        mistake = 0
        if level == 1:
            x = random.randint(1,9)
            y =random.randint(1,9)
        elif level == 2:
            x = random.randint(11,99)
            y =random.randint(11,99)
        else:
            x = random.randint(111,999)
            y =random.randint(111,999)
        
        while True:
            print(f"{x} + {y} = ", end="")
            answer = input()
            if answer ==  str(x + y):
                score += 1
                break
            elif answer != str(x + y) and mistake != 3:
                print("EEE")
                mistake += 1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
                break
    print(score)


if __name__ == "__main__":
    main()