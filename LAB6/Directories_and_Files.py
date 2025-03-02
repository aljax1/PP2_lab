#1
import os

location = input("Enter the directory path: ")

if os.path.exists(location):
    print("All items:", os.listdir(location))
    print("Directories:", [name for name in os.listdir(location) if os.path.isdir(os.path.join(location, name))])
    print("Files:", [name for name in os.listdir(location) if os.path.isfile(os.path.join(location, name))])
else:
    print("The specified path does not exist.")
#2
import os

path = input("Enter the file or directory path: ")

print('Path exists:', os.access(path, os.F_OK))
print('Path readable:', os.access(path, os.R_OK))
print('Path writable:', os.access(path, os.W_OK))
print('Path executable:', os.access(path, os.X_OK))

#3
import os

path = input("Insert path: \n")

if not os.path.exists(path):
    print("Path does not exist")
else:
    directories = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    files = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    
    print("Directories:", ', '.join(directories) if directories else "No directories")
    print("Files:", ', '.join(files) if files else "No files")
#4
with open(r'C:\Users\Admin2\Desktop\lab3\1.py', 'r') as file:
    x = len(file.readlines())
    print("Number of lines:", x)
#5
mylist = ['A', 'B', 'C', 'D']
with open(r'C:\Users\Admin2\Desktop\lab3\1.py', 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()
#6
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is the file {letter}.txt")

generate_text_files()
#7
with open('file.txt', 'r') as file1, open('filee.txt', 'a') as file2:
    for line in file1:
        file2.write(line)
#8
import os

file_path = r'C:\Users\Admin2\Desktop\lab3\classes.py'
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File not found.")
