user=input("input: ")

print("output:",end="")

for alphabet in user:
#using .lower() so that if the input is in upper case it is converted to lower case...
    if not alphabet.lower() in ['a','e','i','o','u' ]:
#looping for vowels and removing them...
        print(alphabet,end="")