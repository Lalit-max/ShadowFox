# List of friends' names
friends = ["Aditya", "Sneha", "Ravi", "Pranav", "Tanisha"]

# Creating a list of tuples with name and name length
name_length_tuples = [(name, len(name)) for name in friends]

# Printing the result
print("List of tuples (Name, Length):")
for item in name_length_tuples:
    print(item)
