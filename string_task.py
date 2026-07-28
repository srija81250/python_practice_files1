#1
sentence="python is amazing"
for i in range(len(sentence)):
    if i%2==0:
        print(sentence[i],end=" ")
print("\n")

#2
s="python is fun and powerful"
print(s.replace(" ","_"))

#3
s="12345"
print(s.isnumeric())

#4
s="python is amazing"
print(s[::-1])


#5
s="python programming is fun"
result=s.title()
print(result)