variable = input("variable in camel case: ")
print("variable in snake case:", end="")

for alphabet in variable:
    if alphabet.isupper():
        print("_"+alphabet.lower(),end="")
    else:
        print(alphabet,end="")