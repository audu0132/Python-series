import os

# Specify the directory you want to list (use '.' for the current directory)
directory = '/xampp/htdocs'

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: Directory '{directory}' not found.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory}'.")
