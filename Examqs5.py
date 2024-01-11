percent=int(input("Enter your mark:"))

if(percent>90):
    print("Grade:A")
elif(percent>80 and percent<=90):
    print("Grade:B")
elif(percent>=60 and percent<=80):
    print("Grade:C")
elif(percent<60):
    print("Grade:D")
else:
    print("Please enter percentage")


