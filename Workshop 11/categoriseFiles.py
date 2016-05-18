
import os, shutil



def version1():

    categories = []

    os.chdir('FilesToSort')

    for filename in os.listdir('.'):

        extension = filename[filename.rfind('.') + 1:]
        if extension not in categories:
            categories.append(extension)
            os.mkdir(extension)
        shutil.move(filename, extension)


def version2():

    extension_categories = {}
    categories = []

    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        extension = filename[filename.rfind('.') + 1:]

        if extension not in extension_categories:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_categories[extension] = category


            if category not in categories:
                categories.append(category)
                os.mkdir(category)
        shutil.move(filename, extension_categories[extension])

version2()
