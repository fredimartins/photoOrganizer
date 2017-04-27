from PIL import Image
import os, errno, time

myPath = 'C:\\Users\\adm-f\\Pictures\\iCloud Photos\\Downloads'
myNewPath = 'C:\\Users\\adm-f\\Desktop\\google_photos'


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
    try:
        ensure_dir(new_dir[:new_dir.rfind('\\')])
        if os.path.exists(new_dir):
          new_dir = new_dir[:new_dir.rfind('.')] + '_NEW' + new_dir[new_dir.rfind('.'):]
        os.rename(file_path, new_dir)
    except FileExistsError as e:
        print('NEW file already exists')
    return


def get_date_taken(path):
    date = ''
    try:
        #print(time.strftime("%Y:%m:%d", time.gmtime(os.path.getmtime(path))))
        date = Image.open(path)._getexif()[36867]
    except Exception as e:
        print('taken date not found: ' + path)

    if date == '':
        date = time.strftime("%Y:%m:%d", time.gmtime(os.path.getmtime(path)))

    return date

def discover_files():
    files_list = []
    for path, subDirs, files in os.walk(myPath):
        for name in files:
            files_list.append(os.path.join(path, name))

    return files_list


fl = discover_files()
if len(fl) > 0:
    for file in fl:
        print(file)
        date = get_date_taken(file)
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        move_photo(file, myNewPath + '\\' + year + '\\' + month + '_' + day + '\\' + file[file.rfind('\\')+1:])
