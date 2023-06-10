import os

def file_list_generator():
    file_list = []
    for file in os.listdir():  # Iterate over the files in the current directory
        if os.path.isfile(file):  # Check if the item is a file
            file_info = {
                "file_name": file,  # Store the file name
                "file_path": os.path.abspath(file),  # Store the absolute file path
                "file_size": os.path.getsize(file)  # Store the file size
            }
            file_list.append(file_info)  # Add the file information dictionary to the file list
    
    return file_list

if __name__ == "__main__":
    files = file_list_generator()  # Generate the file list
    for file in files:
        print(file)  # Print each file information dictionary
