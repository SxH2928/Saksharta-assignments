# Comments Pset 0 Part 2

Your code works nicely. Good job!

Helpful suggestion: An alternative way to approach the `faces.py` program where you ask the user if they want to continue again and based on that you either call the main function or say 'Thank you!'.

```python
# while True is used to create an infinite while loop. Unless break is used, 
# this program will keep running because True will always return True

while True:
    user_input = input('Do you want to continue the program?').lower()
    if user_input == 'yes':
        main()
    else:
        break
```

This program will keep asking the user if they want to run the program again and again until they enter no, at which point it will break out of the infinite while loop.
