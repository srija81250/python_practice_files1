#1
my_list=[10,20,30,40,50,11]
print(my_list[::-1])

#2
list_sample=[]
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
for i in list1:
    for j in list2:
        if i==j:
           list_sample.append(i)
print(list_sample)

#3.
original_list=[1,2,2,3,4,4,5]
sample_list=[]
for i in original_list:
    if i not in sample_list:
        sample_list.append(i)
print(sample_list)

#4.
duplicated_list=[1,2,2,3,4,4,5]
list1=[]
for i in duplicated_list:
    if i not in list1:
        list1.append(i)
print(list1)

#list concatenation:
my_list=[10,20,30,40,50,11]
original_list=[1,2,2,3,4,4,5]
list1=my_list+original_list
print(list1)

#list repetition
original_list=[1,2,2,3,4,4,5]
sample_list=[original_list*3]
print(sample_list)
#list removal
original_list=[1,2,3,4,5,6]
list1=[]
for i in range(len(original_list)):
    if i%2!=0:
     list1.append(original_list[i])
print(list1)
#list insertion
original_list=[1,2,3,4,5]
original_list.insert(0,12)
original_list.insert(0,11)
original_list.insert(0,10)
print(original_list)
#list comprehensions
#square numbers
result=[i**2 for i in range(1,11)]
print(result)
#even numbers
result=[i for i in range(1,21) if i%2==0]
print(result)
#word lengths
words=["apple","banana","cherry","date"]
result=[len(i) for i in words]
print(result)

    





