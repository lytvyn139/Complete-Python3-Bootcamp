# pip3 install send2trash
import os, shutil, send2trash

os.getcwd()
print(os.listdir())
print(os.listdir('/home/coding/python/udemy/pierian-data/advanced_modules'))

#will move files
#shutil.move('practice.txt', '/home/coding/python/udemy/pierian-data/advanced_modules/1')

""" Deleting Files """
# os.unlink(path) which deletes a file at the path your provide

""" Deleting Empty folders """
# os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide

""" !!! DANGER WILL REMOVE ALL FILES AND FOLDER IN PATH """
# shutil.rmtree(path) 
# this is the most dangerous, as it will remove all files and folders contained in the path. All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.

""" Move to trash """
#send2trash.send2trash('1/practice.txt')


""" Tree Generator """
for folder , sub_folders , files in os.walk("show_dir"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')
    
