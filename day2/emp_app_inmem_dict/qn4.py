# Step 1: Read names from the user
names_input = input("Enter names separated by spaces: ")
names_list = names_input.split()

# Step 2: Sort the names alphabetically
sorted_list = sorted(names_list)

# Step 3: Convert the list into a tuple
sorted_tuple = tuple(sorted_list)

# Step 4: Save the sorted list and tuple into a file
with open('names_data.txt', 'w') as file:
    file.write("Sorted List:\n")
    file.write(str(sorted_list) + "\n")
    file.write("Sorted Tuple:\n")
    file.write(str(sorted_tuple) + "\n")

# Step 5: Read and print the saved data
print("\nReading from names_data.txt:")
with open('names_data.txt', 'r') as file:
    data = file.read()
    print(data)