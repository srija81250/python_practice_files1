#Declare two variables, one storing an integer and the other a string. Print their values
employee_id=123456
employee_name="SRIJA"
print(employee_id)
print(employee_name)

#Concatenate two strings and print the result.
first_name="SRIJA"
last_name="THALLA"
full_name=first_name+" "+last_name
print(full_name)

"""Create a program that takes user age = “35”, converts it to an integer,and 
then prints the result type."""
employee_age="35"
employee_age=int(employee_age)
print(employee_age)
print(type(employee_age))



"""Display the memory addresses
The memory addresses of x and y 
employee_id = 10
person_age = 10"""
employee_id=10
person_age=10
print(id(employee_id))
print(id(person_age))

#Create variables of different data types(int,float,str) and print their values.
employee_age=32
employee_salary=82000.50
employee_name="SRIJA"
print(employee_id)
print(employee_name)
print(employee_age)













"""Determine the data type of a variable.
 Expected Output:
The data type of variable discount is <class 'int'>."""
discount=10
print("the data type of a variable discount is",type(discount))


#Write a program that prints a pattern using multiple print statements.
print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")



#Create a Python script for a simple task and add comments to explain each step.

'''
first line indicates marks secured in subject mathematics
second line indicates marks secured in subject physics
third line indicates marks secured in subject chemistry
in fourth line by using + operator addition of all the 3 subjects has done to get
 the total marks
 last line is written to print total marks on the screen
 '''
mathematics=98
physics=99
chemistry=99
total_marks=mathematics+physics+chemistry
print(total_marks)









#variable:variable is a container used to store a value.
student_id=1234
"""in the above line 1234 value is assigned to student_id which is of type integer 
by using assignment operator '='"""
student_name="srija" #srija is assigned to the variable student_name which is of type string
student_age=30   # 30 is a value assigned to student_age


#data_types:
employee_age=21 #this is an int data type which doesnot have any floating point number
employee_name="SRIJA"
'''above line is a string data type which have sequence of characters enclosed 
within double quotes'''
employee_salary=82500.50 #it is a float data type which has a decimal value

#type():
print(type(employee_age))
print(type(employee_name))
print(type(employee_salary))

#type conversion:
print(int(employee_salary))
print(type(employee_salary))



age=int(input("enter your age")) #explicit type conversion
print(type(age))

