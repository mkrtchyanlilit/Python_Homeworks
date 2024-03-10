# while True:
#     filename = input("Enter the name of the text file you want to open: ")
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             print("File content:\n", content)
#             break
#     except FileNotFoundError:
#         print("Invalid filename. Please enter a valid filename.")

try:
    filename = input("Enter the name of the text file you want to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Invalid filename. Please enter a valid filename.")
else:
    choice = input("Do you want to write to this file? (yes/no): ").lower()
    if choice == 'yes':
        with open(filename, 'w') as file:
            new_content = input("Enter the new content you want to write: ")
            file.write(new_content)
    else:
        new_filename = input("Enter the name of the new text file: ")
        new_content = input("Enter the content you want to write: ")
        with open(new_filename, 'w') as file:
            file.write(new_content)
    print("Success")
finally:
    print("End of operation.")
    file.close()