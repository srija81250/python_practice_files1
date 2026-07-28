#print numbers from 1 to 100 but stop at 50
for i in range(1,100):
    if i>50:
        break
    print(i)
#using while loop
i=1
while i<=100:
 if i==51:
   break
 print(i)
 i+=1
   
#ask users to enter numbers continuously and stop when they enter -1
while True:
    num=int(input("Enter a number:"))
    if num==-1:
     print("program stopped")
     break
    print(num)
#print only positive numbers from list:
num=[1,-2,3,-4,-5,-6,7]
for i in num:
    if i<0:
        continue
    print(i)
#using while loop
number=[1,2,-3,4,-5,-6,-7]
i=0
while i<len(number):
    if number[i]<0:
        i+=1
        continue
    print(number[i])
    i+=1


#skip spaces in a sentence
var_1="thalla srija"
for i in var_1:
    if i==" ":
        continue
    print(i,end="")

#print numbers from 1 to 50 except even numbers
for i in range(1,51):
    if i%2==0:
        continue
    print(i)

#skip usernames shorter than 5 characters in a list
username=["srija","leo","vineeth"]
i=0
while i<len(username):
 if len(username[i])<5:
  i+=1
  continue
 print(username[i])
 i+=1
  

#stop printing at a specific number
for i in range(1,11):
    if i==6:
        break
    print(i)


#stop when user enters 0
while True:
 num=int(input("Enter the number"))
 if num==0:
  break
 print(num)


#skip a specific number
for i in range(1,11):
    if i==7:
        continue
    print(i)
#using while loop
i=0
num=int(input("upto how many numbers do you want to print:"))
while i<=num:
    if i==9:
        i+=1
        continue
    print(i)
    i+=1

#print only odd numbers
num=int(input("Enter upto how many numbers you want to print:"))
i=1
while i<=num:
      if i%2==0:
            i+=1
            continue
      print(i)
      i+=1
#skip vowels in a string:(using for loop)
name="thallasrija"
vowels="aeiouAEIOU"
for i in name:
 if i in vowels:
  continue
 print(i,end="")











#using while loop
name="thallasrija"
vowels="aeiouAEIOU"
i=0
while i<len(name):
    if name[i] in vowels:
        i+=1
        continue
    print(name[i])
    i+=1

#search a number in a list and stop once found
sample=[1,2,3,4,5,6,7,8,9]
i=0
for num in sample:
    if sample[i]==7:
        print(num)
        break
    i+=1
#search a number in a list by taking input from the user
number=[10,20,30,40,50,60,70,80]
search=int(input("Enter a number"))
for i in number:
    if i==search:
        print("number found")
        print(search)
        break
else:
    print("number not found")  
#print multiplication tables but stop completely when table reaches 5
for i in range(1,11):
    if i>5:
            break
    for j in range(1,11):
        print(f" {i}X{j}={i*j}")
        