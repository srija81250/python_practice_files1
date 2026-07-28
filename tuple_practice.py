tuple1=()
print(tuple1)
print(type(tuple1))

tuple2=(1,2,2.5,"pytonlife",True)
print(tuple2)
print(type(tuple2))

tuple3=tuple()
print(tuple3)
print(type(tuple3))

a=b=c=d=1
print(a)
print(b)
print(c)
print(d)

a=1,23,5,4.5,"python"
print(a)

a,b,c,d=1,2,4,5
print(a)
print(b)
print(c)
print(d)

#swapping of two variables
a=5
b=10
a,b=b,a
print(a)
print(b)

person_info=('john',25,'Male')
print(len(person_info))

tuple1=(1,2,3)
tuple2=('a','b','c')
print(tuple1+tuple2)

tuple1=(1,2,3)
print(tuple1*3)

tuple1=(1,2,3,4,5)
print(tuple1[2])
print(tuple1[-2])

tuple1=(1,2,3,4,5)
print(tuple1[1:3])
print(tuple1[::-1])

fruits=('apple','mango','banana')
print('apple' in fruits)

tuple1=(1,2,3,"pythonlife")
print(tuple1.index("pythonlife"))

sample=()
print(all(sample))