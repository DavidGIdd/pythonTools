import os

# Specify the folder path
folder_path = [
    'C:\\Users\\DipoleServer\\pdv-logs',
    'C:\\Users\\DipoleServer\\pdv-logs',
    'C:\\Users\\DipoleServer\\pdv-logs'
]

# Delete all files in the folder
for path in folder_path:
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            try:
                os.remove(file_path)
                print(f"{file_path} has been deleted.")
            except PermissionError as e:
                print(f"PermissionError: {e}")
            except Exception as e:
                print(f"Error: {e}")
        elif os.path.isdir(file_path):
            print(f"{file_path} is a directory, skipping.")
