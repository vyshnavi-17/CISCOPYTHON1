# Step 1: Accept a sequence of numbers from the user
numbers_input = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_input.split()]

# Step 2: Find maximum and minimum values
max_value = max(numbers_list)
min_value = min(numbers_list)

# Step 3: Store the results in a file
with open('minmax_data.txt', 'w') as file:
    file.write(f"Numbers List: {numbers_list}\n")
    file.write(f"Maximum Value: {max_value}\n")
    file.write(f"Minimum Value: {min_value}\n")

# Step 4: Read and print the saved data
print("\nReading from minmax_data.txt:")
with open('minmax_data.txt', 'r') as file:
    data = file.read()
    print(data)