'''#check age eligibility to vote:
age=int(input("Enter your age:"))
if age>=18:
    print(f"you are eligible to vote age is:{age}")
    user=input("Enter username:")
    print(f"welcome {user}")
#check age eligibility for voting:
age=int(input("Enter your age:"))
voting_age=18
if age>=18:
    print(f"you are eligible to vote and age is: {age}")
else:
    years_until_eligible=voting_age-age
    print(f"you are not eligible to vote and you can vote after {years_until_eligible} years")
#check username and password:
username=input("Enter the username:")
password=input("Enter the password:")
if username=="thalla srija" and password=="srija@123":
    print("successfully logged in")
    print(f"welcome {username}")
else:
    print("invalid credentials")



#if-elif-else:
#Grading system:
marks=int(input("Enter your marks:"))
if marks>100 or marks<0:
    print("enter marks in between 0 to 100")
elif marks>=90:
    print(f"You got grade A and obtained marks: {marks}")
elif marks>=80:
    print(f"You got grade B and obtained marks: {marks}")
elif marks>=70:
    print(f"You got grade C and obtained marks: {marks}")
elif marks>=60:
    print(f"You got grade D and obtained marks: {marks}")
elif marks>=35:
    print(f"You got grade E and obtained marks: {marks}")
else:
    print(f"you got failed")




#nested if-else:
#username and password check:
username=input("Enter the username:")
password=input("enter the password:")
if username=="thallasrija":
    if password=="srija@123":
        print(f"you have successfully logged in {username}")
    else:
        print(f"invalid password")
else:
    print("invalid username")'''



#shorthand if-else:
num_1=int(input("Enter the number:"))
result="even" if num_1%2==0 else "odd"
print(f"the number is {result}")




