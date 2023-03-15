start = int(50)
print("Amount Due:", start)


while start > 0:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        if coin == 25:
            start = start - coin
            if start == 0:
                print("change Owed", start)
            else:
                print("Amount Due:", start)
        elif coin == 10:
            start = start - coin
            if start == 0:
                print("change Owed", start)
            else:
                print("Amount Due:", start)
        elif coin == 5:
            start = start - coin
            if start == 0:
                print("change Owed", start)
            else:
                print("Amount Due:", start)
    else:
        print("Enter 50, 25 or 5 cents")