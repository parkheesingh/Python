#question 1
s= input("enter a string : ")
if len(s)<2 :
    print("not a valid string ")
else:
    print(s[:2] + s[-2:])

#question 2 
s1= input("enter the first string  : ")
s2= input("enter the second string: ")
if len(s1)>0 and len(s2)>0:
    print(s2[:1]+ s1[1:] + " " + s1[:1]+ s2[1:])
else:
    print("invalid")

#question3 
s=input("enter a string: ")
if len (s)<3:
    print(s)
elif s.endswith("ing"):
    print (s + "ly" )
else:
    print (s + "ing" )

#question4 
s = input("enter a string: ")
n= int(input("enter the index to remove: "))
if 0 <=n <= len(s):
     result= s[:n] + s[n+1:] 
     print(result)
else:
     print("invalid index ")