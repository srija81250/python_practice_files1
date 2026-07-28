
  
#for loop:
#syntax:
#for variable in sequence:
emp_data=["akhil","nikhil","sai","suraj","deeraj"]
for i in emp_data:
    print(i)
#fruits tuple:
fruits=("apples","mangoes","banana","orange")
for i in fruits:
    if i=="mangoes":
     print(f"{i} have been received")
    print(i)


for i in range(10):
    print(i)
for i in range(1,11):
    print(i)
for i in range(10):
    user=input("Enter username")
    print(user)

for i in range(1,101):
    print(i)
for i in range(1,10,2):
    print(i)
    for i in range(1,21):
        print(f"2X{i}={2*i}")


for i in range(1,11):
    print(f"17X{i}={17*i}")




table=int(input("which table do you want to print?"))
for i in range(1,11):
 print(f"{table}X{i}={table*i}")


for i in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print('-'*25)

#while
age=35
while age>=18:
    print("you are eligible to vote")
    break




while True:
    username=input("Enter the username:")
    password=input("Enter the password:")
    if username=="srija" and password=="srija@123":
        print("you have successfully logged in")
        break
    else:
        print(f"invalid credentials")



for i in range(1,2):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")

'''#factorial using while loop
fact=1
fact_num=int(input("Enter a factorial number:"))
fact_1=fact_num
while fact_num>=1:
    fact=fact*fact_num
    fact_num-=1
print(f"{fact_1}! is: {fact}")

#factorial using for loop:
fact_num=int(input("Enter the number:"))
fact=1
for i in range(1,fact_num+1):
    fact*=i
print(f"{fact_num}! is: {fact}")'''

word=["srija","break","skip","break","sai","eating"]
for i in word:
    if i=="break" or i=="continue":
        continue
print(i)