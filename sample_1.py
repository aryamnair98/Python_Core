try:
    num=int(input("enter the number:"))
   
    if num==0:
        print("factorial of zero is 1")
        i=1
        fact=1
        
    while(i<=num):
        fact=fact*i
        i+=1
    print("factorial of",num,"=",fact)
except Exception as e:
    if num<0:
        raise Exception("there is no factorial in negative  number")



    


