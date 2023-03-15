def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if 2 <= len(s) < 7:
        if s.isalnum():
             if s[0].isdigit() and s[1].isdigit():
                 return False
             else:
                  if s[2:length].isdigit():
                        if int(s[2]) != 0:
                            return True
                        else:
                            return False
                  
                  elif s[3:length].isdigit():
                        if int(s[3]) != 0:
                            return True
                        else:
                            return False
                  
                  elif s[4:length].isnumeric(): 
                        if int(s[4]) != 0:
                            return True
                        else:
                            return False
                        
                  elif s[5:length].isnumeric(): 
                        if int(s[5]) != 0:  
                            return True
                        else:
                            return False

                  elif s[2:length].isalpha():
                        return True          
        else:
            return False
    else:
        return False

main()