#import os
import os
#specify the drictories you want to list
directory_path='/python/practice/ch1'

# list all the files and the directories in the specified path
contents=os.listdir(directory_path)

#print each file and directories
for item in contents :
    print(item)