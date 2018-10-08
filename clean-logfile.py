#!/bin/python3

#===============================================================================
#               ********* THIS SCRIPT CLEAN LOG FILE **********
#
#                the script gets 3 parameters:
#                file_name, limit_size, count_files
#
# The log file will clean if size of this file is more than limit size,
# before clean the current log file will copied to new file
#===============================================================================

import shutil  # for compy file
import os      # for get filesize and check if file exist
import sys     # for comand line arguments

# clean-logfile.py  filelogname.txt  10 kByt  5 count of files
if (len(sys.argv)<4):
    print ("Missing arguments!  Usage is script.py 10  5")
    exit(1)

file_name   = sys.argv[1]
limit_size   = int(sys.argv[2])
count_files  = int(sys.argv[3])


if (os.path.isfile(file_name) == True):             #check if MAIN filelog exist
    logfile_size = os.stat(file_name).st_size       #get filsesize in BYTES
    logfile_size = logfile_size / 1024              #convert to KILLOBYTES
    if(logfile_size >= limit_size):
        if(count_files>0):
            for currentFileNum in range(count_files, 1, -1):
                src = file_name+"_"+str(currentFileNum-1)
                dst = file_name+"_"+str(currentFileNum)
                if(os.path.isfile(src) == True ):
                    shutil.copyfile(src, dst)
                    print("Copied: "+ src + " to "+dst)
            shutil.copyfile(file_name, file_name+"_1")
            print("Copied: "+ file_name + " to " + file_name+"_1")
        myfile = open(file_name, 'w')
        myfile.close()
