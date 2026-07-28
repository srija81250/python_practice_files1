'''#square of a number
result=lambda x:x**2
print(result(5))

#square using input from user
result=lambda x:x**2
x=int(input("Enter a number:"))
print(result(x))

#even or odd
result=lambda x:"even" if x%2==0 else "odd"
print(result(4))
print(result(3))

#even or odd
result=lambda x:"even" if x%2==0 else "odd"
x=int(input("Enter a number"))
print(result(x))

#bigger
result=lambda a,b:"a is bigger" if a>b else "a is smaller"
print(result(3,5))

#bigger taking input from user
result=lambda a,b:"a is bigger" if a>b else "b is bigger"
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(result(a,b))

#add
result=lambda a,b:a+b
print(result(5,6))

#add taking user input
result=lambda a,b:a+b
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(result(a,b))

#multiply 
result=lambda a,b:a*b
print(result)



#smallest
result=lambda a,b:"a is smaller" if a<b else "b is smaller"
print(result(5,3))

#smallest taking user input
resul=lambda a,b:"a is smaller" if a<b else "b is smaller"
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(result(a,b))

#multiply taking user input
result=lambda a,b:a*b
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(result(a,b))
'''
'''#map:square of all
list1=[1,2,3,4,5]
def square(a):
    return a**2
result=map(square,list1)
print(list(result))

list1=[1,2,3,4,5,6,7,8,9]
result=map(lambda a:a**2,list1)
print(list(result))

#list1=[1,2,3,4,5,6,7,8,9]
result=lambda a:a.upper()
print(str(result('r')))

list1=['srija','sai']
result=map(lambda a:a.upper(),list1)
print(list(result))

def upper(a):
    return a.upper()
result1=map(upper,list1)
print(list(result1))

list1=[1,2,3,4,5,6,7,8,9]
result=map(lambda a:a+10,list1)
print(list(result))

def add(a):
    return a+10
list1=[1,2,3,4,5,6,7,8,9]
result=map(add,list1)
print(list(result))

#celsius to fahrenheit
result=lambda a:(9*a)/5+32
print(result(5))

def fah(a):
    return (9*a)/5+32
list1=[1,2,3,4,5,6,7,8,9]
result=map(fah,list1)
print(list(result))

#length of a word in a list
list1=['srija','apple','pomegranate']
result=map(lambda a:len(a),list1)
print(list(result))

def length(a):
    return len(a)
result=map(length,list1)
print(list(result))
#reverse each word
list1=['apple','banana','orange']
result=map(lambda a:a[::-1],list1)
print(list(result))

#find first letter of each word:
result=map(lambda a:a[0],list1)
print(list(result))


list1=['apple','banana','orange']
def fw(a):
    return a[0]
result=map(fw,list1)
print(list(result))

#filter even numbers
list1=[1,2,3,4,5,6,7,8,9,10]
def even(a):
    return a%2==0
result=filter(even,list1)
print(list(result))
list1=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda a:a%2==0,list1)
print(list(result))

#odd numbers
list1=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda a:a%2!=0,list1)
print(list(result))

#filter positive numbers
list1=[1,-2,3,-4,5,-6,7,-8,-9,-10]
result=filter(lambda a:a>0,list1)
print(list(result))

#filter names starting with A
list1=['Apple','Banana','Avacado']
result=filter(lambda a:a.startswith('A'),list1)
print(list(result))

list1=['madam','python','level','code']
result=filter(lambda a:a==a[::-1],list1)
print(list(result))

list1=['python','srija','orange']
result=filter(lambda a:len(a)>5,list1)
print(list(result))

from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10]
result=reduce(lambda a,b:a+b,list1)
print(result)


from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10]
result=reduce(lambda a,b:a*b,list1)
print(result)

list1=[1,2,3,4,5,6,7,8,9,10,11]
result=reduce(lambda a,b:max(a,b),list1)
print(result)

list1=[1,2,3,4,5,6,7,8,9,10]
result=reduce(lambda a,b:min(a,b),list1)
print(result)
#filter even and squares of even
list1=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda a:a%2==0,list1)
result=map(lambda a:a**2,even)
print(list(result))


#sum of squares of even
list1=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda a:a%2==0,list1)
squares=map(lambda a:a**2,even)
result=reduce(lambda a,b:a+b,squares)
print(result)
'''
from functools import reduce
from math import *
list1=[1,2,3,4,5,6,7,8,9,10]
result=map(lambda x:reduce(lambda a,b:a*b,range(1,x+1)),list1)
print(list(result))


list1=['srija','python']
result=map(lambda a:a.upper(),list1)
print(list(result))

string='srija'
result=filter(lambda a:a=='a' or a=='e' or a=='i' or a=='o' or a=='u',string)
print(list(result))

list1=[1,2,3,4,5,6,7,8,9]
result=list(map(lambda x:list(filter(lambda a:x%a!=0,range(2,x+1))),list1))
print((result))










































