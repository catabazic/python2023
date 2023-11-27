
#--------------------------------- Exercitiul 1

import os
import sys

def read_files(directory, extension):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # Iterate over files in the directory with the specified extension
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                file_path = os.path.join(directory, filename)

                try:
                    # Read and print the contents of each file
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"Contents of {filename}:\n{content}\n{'='*30}")

                except Exception as e:
                    print(f"Error reading file '{filename}': {e}")

    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     # Check if command line arguments are provided
#     if len(sys.argv) != 3:
#         print("Usage: python read_files.py <directory_path> <file_extension>")
#         sys.exit(1)
#
#     # Get directory path and file extension from command line arguments
#     directory_path = sys.argv[1]
#     file_extension = sys.argv[2]
#
#     # Call the read_files function with provided arguments
#     read_files(directory_path, file_extension)


#--------------------------------- Exercitiul 2


def rename_files(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # Get a list of all files in the directory
        files = os.listdir(directory)

        # Sort the files to ensure consistent numbering
        files.sort()

        # Rename each file with a sequential number prefix
        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_name = f"file{index}{os.path.splitext(filename)[1]}"
            new_path = os.path.join(directory, new_name)

            try:
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")

            except Exception as e:
                print(f"Error renaming file '{filename}': {e}")

    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     # Check if command line arguments are provided
#     if len(sys.argv) != 2:
#         print("Usage: python rename_files.py <directory_path>")
#         sys.exit(1)
#
#     # Get directory path from command line arguments
#     directory_path = sys.argv[1]
#
#     # Call the rename_files function with the provided directory path
#     rename_files(directory_path)


#--------------------------------- Exercitiul 3


def calculate_total_size(directory):
    total_size = 0

    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # Iterate through all files in the directory and its subdirectories
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)

                try:
                    # Get the size of each file and add it to the total
                    file_size = os.path.getsize(file_path)
                    total_size += file_size

                except Exception as e:
                    print(f"Error getting size of file '{file_path}': {e}")

    except Exception as e:
        print(f"Error: {e}")

    return total_size

# if __name__ == "__main__":
#     # Check if command line arguments are provided
#     if len(sys.argv) != 2:
#         print("Usage: python calculate_file_size.py <directory_path>")
#         sys.exit(1)
#
#     # Get directory path from command line arguments
#     directory_path = sys.argv[1]
#
#     # Call the calculate_total_size function with the provided directory path
#     total_size = calculate_total_size(directory_path)
#
#     if total_size > 0:
#         print(f"Total size of all files in '{directory_path}': {total_size} bytes")
#     else:
#         print(f"No files found in '{directory_path}'")



#--------------------------------- Exercitiul 4


def count_file_extensions(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # Check if the directory is empty
        if not os.listdir(directory):
            print(f"No files found in '{directory}'.")
            return

        # Dictionary to store the counts of each file extension
        extension_counts = {}

        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            # Ignore directories
            if os.path.isfile(os.path.join(directory, filename)):
                # Get the file extension
                _, file_extension = os.path.splitext(filename)

                # Increment the count for the file extension
                extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        # Print the counts
        print("File extension counts:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")

    except Exception as e:
        print(f"Error: {e}")

# if __name__ == "__main__":
#     # Check if command line arguments are provided
#     if len(sys.argv) != 2:
#         print("Usage: python count_file_extensions.py <directory_path>")
#         sys.exit(1)
#
#     # Get directory path from command line arguments
#     directory_path = sys.argv[1]
#
#     # Call the count_file_extensions function with the provided directory path
#     count_file_extensions(directory_path)
