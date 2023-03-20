month = [
    "-",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if len(date.split("/")) > 2:
        mm, dd, yyyy = date.split("/")
        if int(mm) <=12 and int(dd) <=31:
            if int(mm) < 10 and int(dd) < 10:
                dd = f"0{dd}"
                mm = f"0{mm}"
                print(f"{yyyy}-{mm}-{dd}")
                break
            elif int(mm) < 10:
                mm = f"0{mm}"
                print(f"{yyyy}-{mm}-{dd}")
                break
            elif int(dd) < 10:
                dd = f"0{dd}"
                print(f"{yyyy}-{mm}-{dd}")
                break
            else:
                print(f"{yyyy}-{mm}-{dd}")
                break
        else:
            continue

    elif len(date.split(", ")) > 1:
        md, yyyy = date.split(", ")
        mm, dd = md.split(" ")
        mm = month.index(mm)
        if int(dd) <= 31:
            if int(dd) <10:
                dd = f"0{dd}"
                print(f"{yyyy}-{mm:02}-{dd}")
                break
            else:
                print(f"{yyyy}-{mm:02}-{dd}")

    else:
        continue