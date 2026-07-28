'''#sum of squares from 1-5
sum=0
for i in range(1,6):
    square=(i)**2
    sum+=square
print(f"sum of squares from 1 to 5 is:{sum}")

#countdown
count=5
while count<6:
   print(count)
   if count==1:
      break
   count-=1
   
#sum of even numbers using for loop
sum=0
for i in range(0,11):
   if i%2==0:
      sum+=i
print(f"sum of even numbers from 0 to 1o is:{sum}")









#sum of all numbers from 1 to given number:
sum=0
num_1=int(input("Enter the number : "))
for i in range(1,num_1+1):
    sum+=i
print(f"sum of all numbers from 1 to {num_1} is: {sum}")

#display numbers from list using loop
sample_list=[1,2,3,4,5,6,7,8]
for i in sample_list:
    print(i)






#display numbers from -10 to -1 using for loop:
for i in range(-10,0):
    print(i)
#cube of numbers from 1 to given number
num_2=int(input("Enter the number:"))
for i in range(1,num_2+1):
    cube=i**3
    print(cube)'''






#multiplication table for user specified number using nested for loop:

table=int(input("which table you need to display?"))

for i in range(table,table+1):
    for j in range(1,11):
     print(f"{i}X{j}={i*j}")