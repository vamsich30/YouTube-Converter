import os
from timestamp import changed_time

def file_in_direc(base,out_file):
    if os.path.exists(out_file):
        print("[ " + base + " ] " + "file is already downloaded\nDo you want to download it again\nPress y/n to install/exit : ",end = "")

        while True:
            temp = input()[0]
            if temp == 'y' or temp == 'Y':
                changed_time(out_file)
                print("(•‿•)successfully Downloaded(•‿•)")
                exit()
            if temp == 'n' or temp == 'N':
                print("Terminated...")
                exit()
            else:
                print("Please enter only Y / N : ",end="")
                continue

