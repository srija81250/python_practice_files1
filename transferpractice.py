for i in range(11):
    if i==3:
        break
    print(i)
print(f"last iteration {i}")

emp_id=[12,21,526,544,63,78,546]
for i in emp_id:
    if i==544:
        print(f"employee id found {i}")
        break
print(f"last iteration {i}")


for i in range(11):
    if i==2:
        continue
    print(i)
print(f"last iteration: {i}")

products=["ok","ok","ok","defect","defect","defect","defect","ok","ok","ok","ok","ok","ok",]
for i in products:
    if i=="defect":
        print(i)
print(i)

products=["ok","ok","ok","defect","defect","defect","defect","ok","ok","ok","ok","ok","ok",]
for i in products:
    if i=="defect":
        continue
    print(i)
print(f"last iteration: {i}")



#pass
for i in range(11):
    if i>=5:
        pass
    else:
        print(f"not required")

for i in range(10):
    pass
print(f"last iteration {i}")

#python list
list_1=[]
print(list_1)
print(type(list_1))

list_2=[2,3.2,"pythonlife",{1,2},(1,2,3.5),[9,8.32],{1:"user_1"}]
print(list_2)

list_3=list()
print(list_3)
print(type(list_3))

#indexing:positive indexing:
list_1=[10,20,30,40,50,60]
print(list_1[0])
print(list_1[1])
print(list_1[2])

#negative indexing:
print(list_1[-4])
print(list_1[-2])
print(list_1[-2])

#slicing:
my_list=[10,20,30,40,50,60,70,80]
print(my_list[0:8:1])
print(my_list[0:8])
print(my_list[::])
print(my_list[::2])
print(my_list[::3])

#forward slicing and positive indexing
my_list=[10,20,30,40,50,60,70,80]
print(my_list[1:4])
print(my_list[5:8])
print(my_list[2:5])

#forward slicing and negative indexing
my_list=[10,20,30,40,50,60,70,80]
print(my_list[-7:-4])
print(my_list[-5:-3])
print(my_list[-4:-1])

#backward slicing and positive indexing
my_list=[10,20,30,40,50,60,70,80]
print(my_list[6:3:-1])
print(my_list[2::-1])
print(my_list[3:0:-1])

#backward slicing and negative indexing
my_list=[10,20,30,40,50,60,70,80]
print(my_list[-2:-5:-1])
print(my_list[-6::-1])
print(my_list[-3:-6:-1])
#nesting list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2]) #to access element 3
print(matrix[1][2]) #to access element 6
print(matrix[2][0]) #to access element 7
print(matrix[2][2]) #to access element 9




