import os

def list_directory_contents(path='.'):
    """Print the contents of a directory using os.listdir()."""
    try:
        contents = os.listdir(path)
        print(f"Contents of directory: {os.path.abspath(path)}")
        print(f"Total items: {len(contents)}\n")

        for item in contents:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")

    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")

# List current directory
list_directory_contents("C:\Python\Chapter1 test")

# Or specify a custom path:
# list_directory_contents('/your/custom/path')