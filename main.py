from PIL import Image
import os, errno

myPath = 'D:\\ft'


def ensure_dir(dir_name):
    """
    Ensure that a named directory exists; if it does not, attempt to create it.
    """
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def move_photo(file_path, new_dir):
    ensure_dir(new_dir[:new_dir.rfind('\\')])
    os.rename(file_path, new_dir)
    return


def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


def discover_files():
    files_list = []
    for path, subDirs, files in os.walk(myPath):
        for name in files:
            files_list.append(os.path.join(path, name))

    return files_list


fl = discover_files()
if len(fl) > 0:
    for file in fl:
        date = get_date_taken(file)
        print(date)
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        move_photo(file, myPath + '\\' + year + '\\' + day + '_' + month + '\\' + file[file.rfind('\\')+1:])