import os

def rename_files():
    ##1. get file names from a folder
        #os.listdir:mac-originial fileposition as listed below
        #           windows-os.listdir(r"C:/...")   r means raw address
    file_list = os.listdir("/Users/longxia/Desktop/nanodegree/2 secret message/prank")
    saved_path = os.getcwd()
    print("current working directory: " + saved_path)
    os.chdir("/Users/longxia/Desktop/nanodegree/2 secret message/prank")
    print("current working directory: " + os.getcwd())

    ##2. for each file, rename filename
    for file_name in file_list:
        print("old name - " + file_name)
        print("new name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)  #change directory back to the original

rename_files()
