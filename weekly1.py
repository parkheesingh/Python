#question1 
for i in range (1, 51):
    if i%3== 0 and i%5==0 :
        print("Fizzbuzz")
    elif i%3== 0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)

#question2 
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#question3
score= int(input("enter score(0-100): "))
if 90<= score<= 100:
    print("Grade A")
elif 80<= score<=89:
    print("Grade B")
elif 70<= score<=79:
    print("Grade C")
elif 60<=score<=69:
    print("Grade D")
elif 0<= score< 60:
    print("Grade F")
else:
    print("invalid score")

#question4 
num= int(input("enter the number: "))
for i in range (1,11):
    print(num, "x", i, "=", num * i)

#question 5 
squares= []
for i in range(1, 21):
    if i % 2 ==0:
        squares.append(i*i)
print(squares)

#question 6 
year= int(input("enter the year: "))
if (year % 4 ==0 and year % 100 != 0) or (year % 400== 0) :
    print(year, "is a leap year")
else:
    print (year ," is not a leap year")

#question 7 
a= float(input("enter the side1: "))
b= float(input("enter the side2: "))
c= float(input("enter the side3: "))
if a==b==c: 
    print("the triangle is equilateral")
elif a== b or b==c or a==c:
    print("isoceles triangle ")
elif (a*a + b*b== c*c) or (b*b+ c*c== a*a) or (a*a + c*c == b*b) :
    print("right angled triangle")
else:
    print("scalene triangle")

#question 8 
num = int(input("Enter an integer: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


#question 9
weight= float(input("enter your weight: "))
height= float(input("enter your height: "))
bmi= weight / (height * height) 
print("BMI: ", bmi)
if bmi< 18.5:
    print("underweight")
elif 18.5<= bmi<= 24.9:
    print("normal weight")
elif 25<= bmi <=29.9:
    print("overweight")
else:
    print("obesity")

#question 10
num= int(input("enter the day number(1-7): "))
day= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
if 1<= num <= 7:
    print(day[num-1] )
else:
    print("invalid number")

#question 11
price= float(input("enter the price of the product: $ "))
if price> 1000:
    discount= 0.10* price
elif 500<=price<=1000:
    discount= 0.5 *price
else:
    discount= 0
final_price= price - discount
print("original price: $ ", price)
print("discount= $ ", discount)
print("Final price= ", final_price)

# #question12 
n= int(input("enter the integer: "))
sum_n= n * (n+1)//2
print("the sum of first", n, "natural numbers is :", sum_n)

# question13
s= input("enter the string: ")
vowels= "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count +=1
print("Number of vowels:", count)

#question14
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum of digits:", sum_digits)

#question 15
n= int(input("enter the no. of rows: "))
for i in range (1, 1+n):
    print('*' * i)

#question16
num= int(input("enter a number: "))
for i in range (1, num+1):
    if i %2 == 0:
        print(i)

# #question17
num=[5,10,15,20,25,30,35,40,45,50]
   #check if 25 exists
if 25 in num:
    print("25 exists")
else:
    print("25 does not exist")
   #total length of list
print("total length of list is ", len(num))
  #total occurence of 25 
print("total occurence of 25 ", num.count(25))
  #traverse element 
print("traversing elements")
for element in num:
    print(element)
  #show all even numbers
print("even numbers in list: ")
for element in num:
    if element %2 ==0:
        print(element)


#question18 
text = input("Enter a string (minimum 10 words and maximum 19 words): ")

words = text.split()
if len(words) < 10 or len(words) > 19:
    print("Invalid input! Please enter between 10 and 19 words.")
# else:
#     # 1. Print full string and length of string
    print("\nFull String:")
    print(text)
    print("Length of string:", len(text))

#     # 2. Check if string is palindrome (ignoring spaces and case)
    cleaned_text = text.replace(" ", "").lower()
    if cleaned_text == cleaned_text[::-1]:
        print("The string is a Palindrome")
    else:
        print("The string is NOT a Palindrome")

    # 3. Print middle word
    middle_index = len(words) // 2
    print("Middle word:", words[middle_index])

#     # 4. Print second last word
    print("Second last word:", words[-2])

#questio19
print("Welcome to Calci:")
print("1. Power")
print("2. Sum")
print("3. Sub")
print("4. Multiple")

choice = int(input("Enter your choice (1-4): "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == 1:
    print("Result:", a ** b)
elif choice == 2:
    print("Result:", a + b)
elif choice == 3:
    print("Result:", a - b)
elif choice == 4:
    print("Result:", a * b)
else:
    print("Invalid choice")

#question20 
strings = ['arshita', 'daman', 'akshima', '121', 'hiya', 'nitya']

count = 0

for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of valid strings:", count)

