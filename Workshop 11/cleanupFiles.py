
import os, shutil


os.chdir('Lyrics/Christmas')

for filename in os.listdir('.'):

    if not os.path.isdir(filename):
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        print(new_name)



