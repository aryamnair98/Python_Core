a=int(input("Enter number:"))
b=int(input("Enter number:"))
try:
    c=a/b
except Exception as e:
    c=a/(b+2)
    print("Division by zero not permitted")
    print(c)