def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    # if gauge(percentage) == None:
    #     pass
    # else:
    print(gauge(percentage))


def convert(fraction):
    try:        
        x , y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y and y != 0:
            print("Error")
            return ValueError
        
        fraction = round(x/y*100)
        return fraction
    
    except ValueError:
        print("both numbers must be INT")
        return ValueError
    
    except ZeroDivisionError:
        print("Cant divide on 0")
        return ZeroDivisionError
        


def gauge(percentage):
    try:
        if percentage <= 1:
            return("E")
        elif percentage >= 99:
            return("F")
        else:
            return(f"{percentage}%")
    except TypeError:
        pass


if __name__ == "__main__":
    main()