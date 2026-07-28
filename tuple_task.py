#1.Creating tuple
tuple_1=("SRIJA",23,"pink")
print(tuple_1)

#2.Access tuple elements
sample_tuple=("sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(sample_tuple[2])

#3.Tuple concatenation
tup1=(1,3,5)
tup2=(2,4,6)
print(tup1+tup2)

#4.Tuple Unpacking
rect_1=(10,5)
length,width=rect_1
print(f"length of rectangle: {length}")
print(f"Width of rectangle:  {width}")
area=length*width
print(f"area of rectangle: {area}")

#5.check if an element exists:
tuple1=(1,2,3,4,5,6)
print(3 in tuple1)
print(10 in tuple1)
print(10 not in tuple1)
#6
items=[("Apple",99),("Banana",99),("Milk",49)]
print(f"Item",f" "*8,f"Price")
print("-"*22)
price=0
for i,j in items:
    print(f"{i}",f"\t\t",f"{j:.2f}")
    price+=j
print("-"*22)
print(f"Total\t\t{price:.2f}")