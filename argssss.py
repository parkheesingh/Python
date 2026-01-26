#question1 
def average_marks(*args):
    total = 0
    count = 0
    for mark in args:
        if mark >= 0:    
            total += mark
            count += 1
    if count == 0:
        return None     
    return total / count
result = average_marks(75, 80, -5, 90, 60)
if result is None:
    print("No valid marks provided.")
else:
    print("Average of valid marks:", result)
 
#question2 
def filter_details(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, str):   
            print(f"{key} = {value}")

filter_details(
    name="Parkhee",
    age=20,
    city="Delhi",
    cgpa=8.5,
    course="B.Tech CSE"
)
