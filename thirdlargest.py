list1=[]
limit=int(input("enter limit:"))

i=0
while(i<=limit):
    num=int(input("Enter numbers:"))
    list1.append(num)
    i=i+1
print(list1)

if(len(list1<3)):
    print("Please enter atleast 3 elements for list")
else:
    i=0
    big=list1[0]
    sec_big=list1[0]
    third_big=list1[0]

    while(i<len(list1)):
        if list1[i]>big:
            third_big=sec_big
            sec_big=big
            big=list1[i]
        elif list1[i]>sec_big:
            third_big=sec_big
            sec_big=list1[i]
        
        elif list1[i]>third_big:
            third_big=list1[i]
        i=i+1
  
print("Third biggest element:",third_big)
