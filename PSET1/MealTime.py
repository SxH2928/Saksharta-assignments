def main():
    time=input("Enter the time: ")
#creating a variable to recall the function for 24 hr meal time
    meal=convert(time)
    print(meal)
    if meal>=7 and meal <= 8 :
        print("It's time for breakfast")
    elif meal >= 12 and meal <= 13 :
        print("it's time for lunch")
    elif meal >= 18 and meal <= 19 :
        print("It's dinner time")
    else: print("it's no time to eat")
def convert(time):
#defining the function for the 24 hr meal time
    hour,min = time.split(":")
    hour = float(hour) + (float(min)/60)
    return hour
if __name__=="__main__":
    main()
