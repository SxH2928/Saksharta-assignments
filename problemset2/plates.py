def main():
    plate = input("Plate: ") 
     # user for plate number input
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # If plate number is not within the range of 2 and 6, it returns false
    if not (2 <= len(s) <= 6):
        return False
     # If plate number is within the range
    for i in range(len(s)):
        # Checks if plate number has digits
        if s[i].isdigit():
            # If the first digit that occured is 0
            if i == len(s) - 2 and s[i] == '0':
                return False
            # If digit occurs in a postion outside the last two characters
            elif not (i == len(s) - 1 or i == len(s) - 2):
                return False
    return True


main()