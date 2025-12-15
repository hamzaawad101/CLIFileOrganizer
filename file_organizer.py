import os
import shutil


target_folder=input("Enter path for folder: ")
print(target_folder)

#check if path exists
if os.path.exists(target_folder) and os.path.isdir(target_folder):
    extensions={item.split('.')[-1]for item in os.listdir(target_folder)if os.path.isfile(os.path.join(target_folder,item))}


    print(extensions)

    #create folders for each extension type
    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder,extension)):
            os.makedirs(os.path.join(target_folder,extension))

    #move files to designated folders
    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)

        # explicitly skip directories
        if os.path.isdir(item_path):
            continue
        if '.' in item:
            file_extension=item.split('.')[-1]
        else:
            file_extension="no_extension"
        folder_path = os.path.join(target_folder, file_extension)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        #move file into folder
        dest_path = os.path.join(target_folder, file_extension, item)
        counter = 1
        # check if file with same name exists
        while os.path.exists(dest_path):
            base_name, ext = os.path.splitext(item)  # split "file.txt" into "file" and ".txt"
            new_name = f"{base_name}_{counter}{ext}"  # create "file_1.txt", "file_2.txt", etc.
            dest_path = os.path.join(target_folder, file_extension, new_name)
            counter += 1

        # finally move the file
        shutil.move(item_path, dest_path)

#check if path is directory or file
elif os.path.isfile(target_folder):
        print("Path entered is a file.Path must be a folder")
else:
    print("The path does not exist.")