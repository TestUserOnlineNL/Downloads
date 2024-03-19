from pathlib import Path

file_path = Path('import.txt')

if file_path.is_file():
    print('The file exists!')
else:
    print('The file does not exist.')

# Output:
# 'The file exists!' if the file exists, 'The file does not exist.' otherwise.
    
try:
    with open('import.txt'):
        print('The file exists!')
except FileNotFoundError:
    print('The file does not exist.')

# Output:
# 'The file exists!' if the file exists, 'The file does not exist.' otherwise.
    
#from pathlib import Path

# Create a Path object
p = Path('.')

# Print the absolute path
print(p.absolute())

# Output:
# '/path/to/current/directory'

################################################################################################
import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
    
################################################################################################
print()

import re

ln = 0

with open(r"./data-collection/series_data.txt", 'r') as fp:
    for line in fp:

            if re.search("^\n", line):
                continue
            else:
                ln = ln + 1
                print(ln, line.strip())
        
print('Total Lines', ln)

