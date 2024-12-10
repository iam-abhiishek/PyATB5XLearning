import os

print(os.getcwd())  # Returns the current working directory

# List files in the current directory

files = os.listdir("/Users/abhishek/PycharmProjects/PyATB5XLearning")
print("files in current directory",files, type(files))

# Create a new directory
# os.mkdir('Test2')

# Check if a file exists
file_exist = os.path.exists("pramod.txt")
print(file_exist)

print(os.name) # posix == mac, nt - windows