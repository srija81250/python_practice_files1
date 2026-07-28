'''
#area of rectangle?
length=int(input("Enter the length of the rectangle:"))
width=int(input("Enter the width of the rectangle:"))
area=length*width
print(f"length of the rectangle:{length}, width of the rectangle:{width},area of the rectangle:{area}")

#incrementing and decrementing a variable:
num_1=15
num_1+=10
print(f"num_1:{num_1}")

num_2=20
num_2-=10
print(f"num_2:{num_2}")

#to convert temp from celcius to fahrenheit:
temp_1=int(input("Enter the temperature:"))
F=(temp_1*9/5)+32
print(F)
'''

#convert kilometers to miles:
distance=int(input("enter the distance:"))
mile=distance*0.621
print(f"distance in miles:{mile}")

#concatenate two strings:
first_name=input("enter the first name:")
last_name=input("enter the second name:")
full_name=first_name+" "+last_name
print(f"full_name is {full_name}")

#calculate simple interest:
p=int(input("enter principal amount:"))
t=int(input("enter time in years:"))
r=float(input("enter rate of interest:"))
SI=(p*t*r)/100
print(f"simple interest:{SI}")