import os

path = os.getcwd()
print(path)

full_path = path + "/example.txt"
print(full_path)

try:
# Read the file
    file = open(full_path)  # FileNotFoundError: [Errno 2] No such file or directory
except Exception as e:
    print(e)
finally:
    print("This code will be executed anyhow")