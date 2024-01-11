units=float(input("Enter the units consumed:"))

if(units<=100):

    print("No charge up to 100 units..")

elif(units>100 and units<=200):

    amount=((units-100)*(5))
    print("Total electricity-bill amount is:Rs.",amount)

elif(units>200):
    
    amount=((100*0)+(100*5)+(units-200)*(10))
    print("Total electricity-bill amount is:Rs.",amount)

else:
    print("Enter correct units consumed.")
