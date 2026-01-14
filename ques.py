# to check whether the no. is prime or not
# n= int(input("Enter the no. : "))
# if n<=1:
#     print("not prime")
# else:
#     prime= True
#     for i in range (2, int(n**0.5)+1 ):
#         if n%i==0:
#             prime= False
# print(prime)
#2 check whether the no. is palindrome 
n=int(input("enter the no. "))
original= n
reverse_num= 0
while n>0:
    reverse_num= reverse_num * 10 + n%10 
    n= n//10 
if original== reverse_num:
    print("it is palindrome")
else:
    print("it is not a palindrome")

#question 3
# for i in range (1, 101):
#     if i%3== 0 and i%5==0 :
#         print("Fizzbuzz")
#     elif i%3== 0:
#         print("Fizz")
#     elif i%5 ==0:
#         print("Buzz")
#     else:
#         print(i)


