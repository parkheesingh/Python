# question 1
a= int(input("Enter month number(1-12): "))
months= ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
if 1<= a <= 12:
 print("Month: ", months[a - 1])
else :
 print("Invalid number")

#question 2 
a= int(input("enter first number: "))
b= int(input("enter second number: "))
 
# # check if equal
if a==b :
 print("a equals b ")
else: 
 print("not equals")
 
# #which is bigger
if a<b:
 print("b is greater")
elif a>b:
 print("a is greater")
else:
 print("both are same")

# #first no. is smaller or equals to second 
if a<=b:
 print("a is smaller or equalsto b")
else:
 print("a is greater than b")

#print name according to condition
if a >b:
 for i in range (5):
  print ("Enter your firstname: ")
elif a<b:
 for i in range(3):
  print("Enter surname: ")
  

#question 3
str1 =input("enter first string: ")
str2 =input("enter second string: ")
#using==
if str1==str2:
    print("Using == : Both strings are equal")
else:
    print("Using==  : Both the strings are NOT equal") 
#using is
if str1 is str2:
    print("Using is : Both are equal ")
else:
    print("Using is : Both are NOT equal")

#question 4 
str1 =input("enter string_1: ")
str2 =input("enter string_2: ")

num1= int(str1)
num2= int(str2)

if num1 is num2:
    print("Both numbers are equal")
else:
    print("Both numbers are NOT equal")

#question 5 
n= int(input("Enter a number: "))
total= 0 
for i in range (1, n + 1 ):
   total += i
print("Sum from 1 to", n, "is: ", total)

#question 6
num= int(input("Enter a number: "))
for i in range(2, num + 1, 2):
    print(i, end=" ")

#question 7
num= int(input("Enter a number: "))
op= input("Enter an operator (+ or -): ")
if op== "+":
    for i in range(num):
        print (i, end=" ")
elif op== "-":
    for i in range(num, 0, -1):
        print(i, end= " ")
else:
    print("invalid operator")