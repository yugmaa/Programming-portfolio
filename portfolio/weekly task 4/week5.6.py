'''this program takes the name of a file as a command-line argument, and creates a backup copy of that file'''

import sys
import os
import shutil

if len(sys.argv)!=2:  #checks if the number of argument is two.
    print(f"usage: python 233k5.6.py")
else:
    original_filename= sys.argv[1]  #get the first argument
    if os.path.isfile(original_filename):
        backup_filename= original_filename + ".backup"  #backup file created with the same filename
        shutil.copy(original_filename, backup_filename)  #original file copied to the backup file
        print(f"your backup file is created.")
    else:
        print(f" {original_filename} does not exist")