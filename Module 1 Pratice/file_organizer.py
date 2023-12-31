import os
import shutil

def organize_files(directory, extension_mapping):
    for filename in os.listdir(directory):

        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):

            _, file_extension = os.path.splitext(filename)

            destination_folder = extension_mapping.get(file_extension[1:], 'Other')

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, filename))

if __name__ == "__main__":

    directory_path = input("Please enter the copied file path to be sorted: ")


    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Please enter a valid filepath")
    else:
        os.chdir(directory_path)

        extension_mapping = { 'pdf': 'PDFs', 'jpg': 'Images', 'jpeg': 'Images', 'png': 'Images', '7z': 'Zip', 'rar': 'Zip', 'zip': 'Zip', 'exe': 'EXE' }

    organize_files(directory_path, extension_mapping)

    print("Files organized successfully.")
