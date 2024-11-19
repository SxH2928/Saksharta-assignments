greeting = input("Greetings user! ")
greeting_def = greeting.lower().replace(" ","")
if greeting_def == "hello":
    print("0$")
elif greeting_def[0]=="h":
    print("20$")
else :
    print("100$")
