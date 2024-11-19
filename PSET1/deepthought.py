user_input = input("The answer to the Great Question of Life, the Universe and Everything is ?  ")
#convertin the user input to lower letter to make it easy...
user_input2 = user_input.lower().replace("-"," ")
# i'm taking two different conditions with two different variables.
if user_input == "42" or user_input2=="forty two":
    print("Yes")
else :
    print("No")