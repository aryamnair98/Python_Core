try:
    number=int(input("Enter a number"))

    if(type(number) is int):

        print(number,"is an integer")
        
except Exception as e:
    
    raise Exception("please enter integer number")


