#ugwy imports
import shutil
import os
import sys
import glob
#smecsy code
src = input("What am i cloning senpai: ") # what am i cloning senpai
dest = input("Where is it going senpai : ") # where am i cloning to senpai
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest) # function hehe
        for filename in glob.glob(os.path.join(dest, '*')): #selects ebewythin
            with open(filename, 'r') as f: #allow me to read
                text = f.read() #i can read senpai
                file=open(filename, 'w') # gib perms to write uwu
                file.write(str(text)) # write the contnts of senpais files
    except shutil.Error as e:
        print('A friggin shutil error occured senpai %s' % e) # lets hope you never see this omega 
    except OSError as e: #if the os bugs out
        print('There was a OS error ;-; NANI TF ;;-;; %s' % e) #lets hope you never see this senpai
copyDirectory(src, dest) # runs the uwu function
#thankies for using 

