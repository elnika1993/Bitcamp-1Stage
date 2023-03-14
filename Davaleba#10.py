def main():
    time = input("what time is it? ")
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if hours == 7 and 0 <= minutes <= 60 or hours == 8 and minutes == 0: 
        print("Breakfest Time")
    elif hours == 12 and 0 <= minutes <= 60 or hours == 13 and minutes == 0:
        print("Lunch Time")
    elif hours == 18 and 0 <= minutes <= 60 or hours == 19 and minutes == 0:
        print("Dinner Time")
    
if __name__ == "__main__":
    main()



## Another way
# def main():
#     time = input("input time: ")
#     time = convert(time)

#     if 18 <= time <=19:
#         print("It's dinner time")
#     elif 12 <= time <= 13:
#         print("It's lunch time")
#     elif 7 <= time <= 8:
#         print("It's breakfast time")
#     else:
#         print("It's not time to eat!")
                
   
# def convert(time):
#     pm = False
#     if "pm" in time:
#         pm = True
#     # print(pm)
#     time = time.replace("pm", "").replace("am","")
#     # print(time)
#     hours, minutes = time.split(":")
#     # print(hours, minutes)
#     if pm:
#         hours = float(hours) + 12
#     time = float(hours) + float(minutes)/60
#     # print(time)
#     return time

# if __name__ == "__main__":
#     main()