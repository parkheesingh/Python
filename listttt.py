#question1 
friends= ["hiya" , "riya", "siya", "priya" , "jiya"]
new_friend= input("enter the friend's name to add: ")
friends.append(new_friend)
print("\nfriend list: ", friends)
important_friend= input("\enter your most imporatant friend's name: ")
position= int(input("enter the position where you want to add this friend: "))
friends.insert(position, important_friend )
print("\nfinal friend list: ")
print(friends)

#question2 
l= ['hello', 'hiiii', 'heyyy', 'hola', 'graciasss']
print(l)

#question3 
l =[1,10,100,3,6,8]
l.insert(2,59)
l.append(5)
print("list:", l)
print ("length:",  len(l))

#question 4
l= ['hey', 'hellloo', 'jelly', 'bed']
short_words=[]
for word in l:
    if len(word)<4 :
        short_words.append(word)
print(short_words)

#question 5
numbers= range(20)
result=[]
for n in numbers:
    if n% 2==0:
        result.append("even")
    else:
        result.append("odd")
print(result)

#question5 
numbers_div_by_7 =[]
for n in range (1, 1001):
    if n % 7== 0:
        numbers_div_by_7.append(n)
print(numbers_div_by_7)

#question 6
s=("helloo guyss kaisee ho")
space_count= (" ")
print(space_count)
 
#question7 
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common = []

for i in list_a:
    for j in list_b:
        if i == j and i not in common:
            common.append(i)

print(common)
