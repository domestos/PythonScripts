import os
import time

DAYS = 60  # Maximal age of files to stay, older will be beleted
FOLDERS = [
            "~/Downloads",
            "~/Documents"
          ]

TOTAL_DELETED_SIZE  = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS  = 0               # Total deleted empty FOLDERS
nowTime = time.time()                 # Get current time in SECONDS
ageTime =  nowTime-60*60*24*DAYS  # 60sec*60min*24h*DAYS  = we get the number of seconds that contain 60 days

def delete_old_files(folder):
    """Delete files older X DAYS"""
    global nowTime
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE
    for path, dirs, files, in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)   # get Full PATH to file
            fileTime=  os.path.getmtime(fileName) # get life time
            if fileTime < ageTime:                # if life time < set time
                sizeFile = os.path.getsize(fileName) #get size of file
                TOTAL_DELETED_SIZE += sizeFile    # Count SUM of all deteled filesize
                TOTAL_DELETED_FILES +=1           # Count number of deleted files
                print("Deleted file: "+ str(fileName))
                os.remove(fileName)               # Delete file

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_is_run = 0                   #value for recursion
    for path, dirs, files, in os.walk(folder):
        if(not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_is_run +=1
            print("Deleted empty dir: "+ str(path))
            os.rmdir(path)
    if empty_folders_in_is_run>0:
        delete_empty_dir(folder)

#============MAIN=====================================
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)
endtime = time.asctime()

print("-------------------------------------------------------")
print("START TIME "            +starttime)
print("Total Delete size   : " +str(int(TOTAL_DELETED_SIZE/1024/1024))+ "MB")
print("Total Delete files  : " +str(TOTAL_DELETED_FILES))
print("Total Delete folders: " +str(TOTAL_DELETED_DIRS))
print("END TIME: "             +endtime)
print("-------------------------------------------------------")
