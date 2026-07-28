<<<<<<< HEAD
first_string='hello,world'
string_2="python strings kiran's 8"
string_3="""triple quotes is allowed to write a 
sentence in multiple lines"""
print(first_string)
print(string_2)
print(string_3)
string_4=" "
print(string_4)
print(type(string_4))

sentence="python"
print(sentence)
print(len(sentence))

#indexing:to access an individual character 
sentence="python"
print(sentence[2]) #t
print(sentence[4]) #o
print(sentence[5]) #n

#slicing:used to extract portion of elements
print(sentence[2:])#thon
print(sentence[1:4])#yth
print(sentence[-4:])#thon
print(sentence[4:1:-1])#oht
print(sentence[-1:-5:-1])#noht

#methods
#upper() and lower() methods
sentence="python life"
uppercase_sentence=sentence.upper()
lowercase_sentence=sentence.lower()
print(uppercase_sentence)
print(lowercase_sentence)

#len()
sentence="python is a programming language"
length_1=len(sentence)
print(length_1)
#strip()
sentence=" this is a white space program   "
print(len(sentence))
sen_1=sentence.strip()
print(sen_1)
print(len(sen_1))
#count()
sentence="this is a programming language"
count_i=sentence.count(" is")
print(count_i)

count_i=sentence.count("is")
print(count_i)
#split()
data="pythonlife,kiran,123456"
data_1=data.split(',')
print(data_1)
#replace
original_string="python is fun"
modified_string=original_string.replace("fun","pythonlife")
print(modified_string)
#title()
sentence="python is a programming language"
sen_1=sentence.title()
print(sen_1)
#startswith() and endswith()
filename="example.txt"
starts_with=filename.startswith("ex")
ends_with=filename.endswith("txt")
print(starts_with)
print(ends_with)

email_list=["srija@gmail.com","srija@hotmail.com","srija@yahoo.com","python@gmail.com"]
empty_list=[]
for i in email_list:
    if i.endswith("@gmail.com"):
        empty_list.append(i)
print(empty_list)
#using list comprehension:
result=[i for i in email_list if i.endswith("@gmail.com")]
print(result)
#find() and index():
position="this is a sentence"
position_a=position.find('a')
position_i=position.index('i')
print(position_a)
print(position_i)
#capitalize:
text="python programming"
cap=text.capitalize()
print(cap)
#isalpha() and isdigit()
numeric_string="12345678"
alpha_string="python"
is_numeric=numeric_string.isdigit()
is_alpha=alpha_string.isalpha()
print(is_numeric)
print(is_alpha)
#
word_list=["hello","world"]
word_1=' '.join(word_list)
print(word_1)
sentence="python programming is fun"
sen_1=sentence.split()
result=" "
for word in sen_1:
    result+=word.capitalize() + " "
res1=result.strip()
=======
first_string='hello,world'
string_2="python strings kiran's 8"
string_3="""triple quotes is allowed to write a 
sentence in multiple lines"""
print(first_string)
print(string_2)
print(string_3)
string_4=" "
print(string_4)
print(type(string_4))

sentence="python"
print(sentence)
print(len(sentence))

#indexing:to access an individual character 
sentence="python"
print(sentence[2]) #t
print(sentence[4]) #o
print(sentence[5]) #n

#slicing:used to extract portion of elements
print(sentence[2:])#thon
print(sentence[1:4])#yth
print(sentence[-4:])#thon
print(sentence[4:1:-1])#oht
print(sentence[-1:-5:-1])#noht

#methods
#upper() and lower() methods
sentence="python life"
uppercase_sentence=sentence.upper()
lowercase_sentence=sentence.lower()
print(uppercase_sentence)
print(lowercase_sentence)

#len()
sentence="python is a programming language"
length_1=len(sentence)
print(length_1)
#strip()
sentence=" this is a white space program   "
print(len(sentence))
sen_1=sentence.strip()
print(sen_1)
print(len(sen_1))
#count()
sentence="this is a programming language"
count_i=sentence.count(" is")
print(count_i)

count_i=sentence.count("is")
print(count_i)
#split()
data="pythonlife,kiran,123456"
data_1=data.split(',')
print(data_1)
#replace
original_string="python is fun"
modified_string=original_string.replace("fun","pythonlife")
print(modified_string)
#title()
sentence="python is a programming language"
sen_1=sentence.title()
print(sen_1)
#startswith() and endswith()
filename="example.txt"
starts_with=filename.startswith("ex")
ends_with=filename.endswith("txt")
print(starts_with)
print(ends_with)

email_list=["srija@gmail.com","srija@hotmail.com","srija@yahoo.com","python@gmail.com"]
empty_list=[]
for i in email_list:
    if i.endswith("@gmail.com"):
        empty_list.append(i)
print(empty_list)
#using list comprehension:
result=[i for i in email_list if i.endswith("@gmail.com")]
print(result)
#find() and index():
position="this is a sentence"
position_a=position.find('a')
position_i=position.index('i')
print(position_a)
print(position_i)
#capitalize:
text="python programming"
cap=text.capitalize()
print(cap)
#isalpha() and isdigit()
numeric_string="12345678"
alpha_string="python"
is_numeric=numeric_string.isdigit()
is_alpha=alpha_string.isalpha()
print(is_numeric)
print(is_alpha)
#
word_list=["hello","world"]
word_1=' '.join(word_list)
print(word_1)
sentence="python programming is fun"
sen_1=sentence.split()
result=" "
for word in sen_1:
    result+=word.capitalize() + " "
res1=result.strip()
>>>>>>> db76ca4f307bdc8ebb9759e7e6725c52392f6028
print(res1)