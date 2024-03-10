numbers = input("Enter a list of numbers separated by spaces: ").split()
even_nums = []
odd_nums = []
for num in numbers:
    if int(num)%2==0:
        even_nums.append(int(num))
    else:
        odd_nums.append(int(num))

print("Even nums: ", even_nums, "\nOdd nums: ", odd_nums)