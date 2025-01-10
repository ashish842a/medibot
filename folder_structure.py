import os

# Define the folder structure and files
files = [
    "src/__init__.py",
    "src/helper.py",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

def create_files(file_list):
    for file in file_list:
        # Split the file path to separate directories and file name
        dir_name = os.path.dirname(file)
        # Create directories if they don't exist
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        # Create the file
        with open(file, 'w') as f:
            f.write("")  # Empty content for now

if __name__ == "__main__":
    create_files(files)
    print("Folder structure and files created successfully.")
