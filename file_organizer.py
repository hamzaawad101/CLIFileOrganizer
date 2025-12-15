import os
import shutil


target_folder=input("Enter path for folder: ")
print(target_folder)

#check if path exists
if os.path.exists(target_folder) & os.path.isdir(target_folder):
    extensions={item.split('.')[-1]for item in os.listdir(target_folder)if os.path.isfile(os.path.join(target_folder,item))}


    print(extensions)

    #create folders for each extension type
    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder,extension)):
            os.makedirs(os.path.join(target_folder,extension))

    #move files to designated folders
    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder,item)):
            file_extension=item.split('.')[-1]
            shutil.move(os.path.join(target_folder,item),os.path.join(target_folder,file_extension,item))
#check if path is directory or file
elif os.path.isfile(target_folder):
        print("Path entered is a file.Path must be a folder")
else:
    print("The path does not exist.")