def sum_of_elements(numbers, exclude_negative = False):
    sum = 0
    for num in numbers:
        if exclude_negative and int(num) < 0:
            continue  # Skip negative numbers
        sum += int(num)
    return sum    

numbers = input("Enter a list of numbers separated by spaces: ").split()
choice = input("Do you want to exclude negative numbers? (yes/no): ")

if choice == 'yes':
    result = sum_of_elements(numbers, True)
else:
    result = sum_of_elements(numbers)
print("Sum of elements:", result)