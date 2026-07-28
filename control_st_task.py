#1.
num=[25,30,20,40,50]
sum=0
for i in num:
    sum+=i
    if sum>100:
        break
print(sum)

#2.
for i in range(1,601):
    if i%2==0:
        continue
    print(i)
     

#3.
num=int(input("Enter a number"))
for i in range(num,num+1):
    if i%2==0:
        print("even")
    else:
        pass
        

#4.
sample=["srija","sai","break","skip","sindhu","anshu"]
for i in sample:
    if i=="skip":
        continue
    if i=="break":
        continue
    print(i)
    