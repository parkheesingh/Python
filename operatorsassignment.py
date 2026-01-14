#input student details 
name = input("Enter student name: ")
student_class = input("Enter student class:  ")
section = input("Enter section: ")

m1= float(input("Enter marks for subject 1: "))
m2= float(input("Enter marks for subject 2: "))
m3= float(input("Enter marks for subject 3: "))
m4= float(input("Enter marks for subject 4: "))
m5= float(input("Enter marks for subject 5: "))

total= m1+ m2+ m3+ m4+ m5
percentage = (total/500) * 100 

print("Name:", name)
print("Class:", student_class)
print("Section:", section)
print("Percentage:", percentage , "%" )
 
#sum of three numbers 
a= int(input("Enter value_1: "))
b= int(input("Enter value_2: "))
c= int(input("Enter value_3: "))
total= a + b + c 
print("Sum: ", total)

#square of a number 
n= int(input("Enter a number: "))
print( n**2 )

#calculate quotient and remainder 
p= int(input("Enter dividend: "))
q= int(input("Enter divisor: "))
quotient= p//q
remainder= p%q
print("Quotient: ", quotient)
print("Remainder: ", remainder)

#simple interest 
P= float(input("Enter Principal: "))
R= float(input("Enter Rate of interest: "))
T= float(input("Enter Time: "))

SI= (P* R* T)/ 100
print("Simple Interst= ", SI)