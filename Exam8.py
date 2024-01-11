cost=float(input("Enter the cost price of bike:"))

if(cost>100000):

    tax=cost*(15/100)
    print("Road tax is:",tax)

elif(cost>50000 and cost<=100000):

    tax=cost*(10/100)
    print("Road-tax is:",tax)

elif(cost<=50000):
    
    tax=cost*(5/100)
    print("Road tax is:",tax)

else:
    print("Please enter price of bike.")