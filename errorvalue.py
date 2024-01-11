
try:
    number=int(input("Enter a number"))

    print(number,"is an integer")
except ValueError:
    raise Exception("please enter integer number")