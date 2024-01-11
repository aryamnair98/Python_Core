number=int(input("Enter the number:"))

last_digit=number%10

if(last_digit%3==0):
    print("The last digit of the number",number,"is divisible by 3")
else:
    print("The last digit of the number",number,"is not divisible by 3")