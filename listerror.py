def list_pgm(list1,index):

    try:
        print("The element is:",list1[index])

    except IndexError as e:

        raise Exception("Index is out of range",e)
        

     

limit=int(input("Enter the limit:"))

list1=[]

for i in range(limit):
    number=int(input("Enter numbers:"))
    list1.append(number)

print("List elements are:",list1)

index=int(input("Enter the index of element you want:"))

list_pgm(list1,index)