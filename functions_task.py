from math import *
#add
def add(a,b):
    return sum([a,b])
print(add(5,6))
#square root
def square(a):
    return sqrt(a)
print(square(25))

#factorial
def fact1(a):
   b=factorial(a)
   return b
n=int(input("Enter a number to find factorial:"))
fact2=fact1(n)
print(fact2)

#maximum function
def maximum(l):
    b=max(l)
    return b
list_1=[]
while True:
 list2=int(input("Enter numbers"))
 if list2<=20:
   list_1.append(list2)
 else:
  break
print(list_1)
a=maximum(list_1)
print(f"The maximum value in the list is: {a}")

#reverse function
def reverse(a1):
   b=a1[::-1]
   return b
string1=input("Enter a string")
a=reverse(string1)
print(a)

#check prime function
def prime(a):
   if a<=1:
      return False
   for i in range(2,a):
      if a%i==0:
         return False
      else:
         return True
num1=int(input("Enter a number:"))
c=prime(num1)   
print(c)

#average
def average(a):
   sum=0
   count=0
   for j in a:
    sum+=j
    count+=1
    c=float((sum)/(count))
   return c
list3=[]
while True:
 num2=int(input("Enter the number:"))
 if num2<=20:
  list3.append(num2)
 else:
    break
d=average(list3)
print(f"{d:.2f}")

#sum of squares function
def sumofsquares(a):
  sum=0
  for i in a:
   sq=i**2
   sum+=sq
  return sum
list4=[]
n=int(input("Enter up to how many numbers you want sum of squares:"))
while True:
 num3=int(input("Enter the number:"))
 if num3<=n:
   list4.append(num3)
 else:
   break
c=sumofsquares(list4)
print(f"sum of squares of given numbers is:{c}")


#fibonacci
def fibonacci(n1):
    list1=[]
    a=0
    b=1
    for i in range(0,n):
     list1.append(a)
     c=a+b
     a=b
     b=c
    return list1
    
n=int(input("Enter a number for fibonacci sequence"))
print(fibonacci(n))



#palindrome
def palindrome(a):
    original=a
    reverse=0
    while a>0:
     digit=a%10
     reverse=reverse*10+digit
     a//=10
    if original==reverse:
         b=True
    else:
         b=False
    return b
n=int(input("Enter a number:"))
c=palindrome(n)
print(c)