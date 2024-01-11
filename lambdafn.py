def square(x):
    return x**2
print("output using normal fn:",square(2))

s=lambda x:x**2
print("using lambda:",s(5))

numbers=[1,2,3,4]
squared_no=map(lambda x:x**2,numbers)
print(list(numbers))