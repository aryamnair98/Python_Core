class Student:
    def __init__(self,name,address,mobile):
        self.name=name
        self.address=address
        self.mobile=mobile
    def display(self):
        print("Student Name:",self.name)
        print("Address:",self.address)
        print("Mobile Number:",self.mobile)



while(True):
    print("Student details")
    print("1.Enter student details","\n","2.Exit")
    choice=int(input("Enter your choice:"))

    if(choice==1):
        n1=input("Enter the name:")
        a1=input("Enter the address:")
        m1=int(input("Enter the mobile number:"))
        st=Student(n1,a1,m1)
        st.display()
    elif(choice==2):
        break
    else:
        print("No choices")
    
    

