a, b, c = input("Enter the maths expression:  ").split()
num_1=int(a)
num_2=int(c)
match(b):
    case"+":
     print(num_1+num_2)
    case"-":
      print(num_1-num_2)
    case"/":
      print(num_1/num_2)
    case"*":
      print(num_1*num_2)
 