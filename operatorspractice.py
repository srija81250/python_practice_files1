
'''#addition
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1+num_2
print(f"addition of two numbers is:{result}")
#subraction
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1-num_2
print(f"subraction of two numbers is:{result}")
#multiplication
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1*num_2
print(f"multiplication of two numbers is:{result}")
#division
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1/num_2
print(f"division of two numbers is:{result}"



#modulus
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1%num_2
print(f"remainder of two numbers is:{result}")
#exponentation
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1**num_2
print(f"division of two numbers is:{result}")
#floor division
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the second number:"))
result=num_1//num_2
print(f"division of two numbers is:{result}")




#compound assignment operator:it is a shorthand notation which combines arithmetic operation with assignment
num_1=20
num_1+=5
print(num_1)
num_1-=10
print(num_1)
num_1*=10
print(num_1)
num_1/=10
print(num_1)
'''


#comparision operators and logical operators
username=input("Enter the username:")
password=input("Enter the password:")
print(username=="SRIJA" and password=="srija@123")
#identity operators
a=[1,2,3,4]
b=[1,2,3,4]
print(id(a))
print(a is b)
print(id(b))
a=[1,2.5,"srija"]
b=a
print(id(a))
print(a is b)
print(id(b))
#membership operators:to check whether a value is a member of a sequence
sample_set={1,2.5,"srija",(1,3,5)}
print(1 in sample_set)