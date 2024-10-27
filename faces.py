def main():
#asking user input 
    user_input=input("Enter the text: ")
    print(user_input.replace(":)","🙂").replace(":(","🙁"))

    repeat = input("Do you want to try again? yes/no?").lower()
    if repeat ==  "yes":
        main()
    else:
        print("Thankyou for using this program!")
    
main()