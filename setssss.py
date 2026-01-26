# question1 
friday = {"Alice", "Bob", "Charlie"}
saturday = {"Charlie", "David", "Eve"}
all_guests = friday.union(saturday)
both_nights = friday.intersection(saturday)
print("All guests:", all_guests)
print("Guest attending both nights:", both_nights)
 
#question2 
data = [1, 2, 2, 3, 4, 4, 4, 5]
clean_set = set(data)
clean_set.add(6)
print(clean_set)

#question3 
library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}
available_books = library_books.difference(checked_out)
print("Available books on the shelf:", available_books)
new_book = "Don Quixote"
if new_book not in library_books:
    library_books.add(new_book)
    print("Book donated and added to the library.")
else:
    print("Book already exists in the library.")

print("Updated library books:", library_books)

# #question4 
user_permissions = {"read", "write"}
admin_reqs = {"read", "write", "execute"}
has_admin_access = admin_reqs.issubset(user_permissions)

print("User has admin access:", has_admin_access)
missing_permissions = admin_reqs.difference(user_permissions)

print("Missing permissions:", missing_permissions)

#question5
logs = {
    "404": [10, 12, 15, 20],
    "500": [12, 20, 22, 25],
    "403": [10, 20, 30]
}

error_404 = set(logs["404"])
error_500 = set(logs["500"])
error_403 = set(logs["403"])
all_errors_servers = {
    server
    for server in error_404
    if server in error_500 and server in error_403
}

print("Servers with all error types:", all_errors_servers)
critical_servers = {
    server
    for server in error_500
    if server not in error_404
}

print("Critical servers:", critical_servers)
