'''#vowel checker
char=input("Enter a character:")
vowel='aeiouAEIOU'
if char in vowel:
    print(f"The character {char} is a vowel")
else:
    print(f"The character {char} is not a vowel")
#using shorthand if-else:
char=input("Enter a character:")
vowel='aeiouAEIOU'
result="vowel" if char in vowel else "not a vowel"
print(f"the character {char} is {result}")
#number classifier:
num_1=int(input("Enter the number:"))
if num_1>0:
  print(f"The number is positive")
elif num_1<0:
 print(f"The number is negative")
else:
 print(f"The number is zero")

#shorthand if:
x=8
result="even" if x%2==0 else "odd"
print(result)
#calculator:
num_1=int(input("enter the first number"))
num_2=int(input("enter the second number"))
operator=input("enter the operator ('+','-','*','/')")
if operator=='+':
    print("result:",num_1+num_2)
elif operator=='-':
    print("result:", num_1-num_2)
elif operator=='*':
    print("result:", num_1*num_2)
elif operator=='/':
    print("result:", num_1/num_2)
else:
    print("invalid operator")



#discount calculator:
original_price=float(input("enter the price:"))
discount=int(input("Enter the discount:"))
final_price=original_price-(original_price*discount)/100
print(f"original price is {original_price},discount is {discount},final price after discount is {final_price}")
#BMI check:
weight=int(input("Enter the weight:"))
height=int(input("Enter the height:"))
BMI=weight/(height)**2
print(BMI)
#check leap year:
year=int(input("Enter the year:"))
if year%4==0:
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
 print("not a leap year")
'''

#age group classification:
age=int(input("Enter the age:"))
if age<0:
    print("please enter a valid age above 0")
elif age<=12:
    print("given age comes under child")
elif age<=17:
    print("given age comes under teenager")
elif age<=64:
    print("given age comes under adult")
else:
    print("given age comes under senior")