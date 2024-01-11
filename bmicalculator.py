def bmi_calc(height,weight):

    bmi=(weight)/(height*0.01)**2

    print("Body mass index is:",bmi)

    value=check(bmi)

    return bmi,value

def check(bmi):

    if bmi <=18.5:

        value="The person is underweight"
        print(value)

    elif bmi>=24.9 and bmi <=18.5:

        value="The person is in normal weight"
        print(value)

    elif bmi <=25 and bmi>=29.9:
        value="The person is in over weight"
        print(value)

    elif bmi>=30:

        value="The person has obesity"
        print(value)

    else:
        print("Input not correct")
    return value



number=int(input("Enter no.of peoples:"))

result=[]

print("Enter details.......")

for i in range(number):
    
    name=input("Enter name of the person:")
    height=float(input("Enter height in cm:"))
    weight=float(input("Enter weight in kg:"))

    bmi,value=bmi_calc(height,weight)

    data={"name":name,"weight":weight,"height":height,"bmi":bmi,"bmi-check":value}
    result.append(data)

print("............................")

print("Displaying details...")

for persons in result:
    print("Name:",persons["name"])
    print("Weight in kg:",persons["weight"])
    print("Height in cm:",persons["height"])
    print("BMI:",persons["bmi"])
    print("BMI Category:",persons["bmi-check"])
    print(".................")
