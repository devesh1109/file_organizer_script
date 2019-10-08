import os
import shutil


def get_path():
    return os.getcwd()


def organize_path(source_path):
    if get_path() is not source_path:
        if os.path.exists(source_path):
            os.chdir(source_path)
    files = os.listdir(source_path)
    dir_categ = ['Music', 'Images', 'Videos', 'Documents', 'Compressed', 'Miscellaneous', 'Programs']
    ext_list_images = ['.gif', '.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    ext_list_audio = ['.mp3', '.aac', '.wav', '.ogg', '.wma', '.flac']
    ext_list_video = ['.wmv', '.mp4', '.mkv', '.avi', '.mov', '.flv', '.gifv', '.yuv', '.rm', '.3gp', '.mpg', '.mpeg']
    ext_list_doc = ['.doc', '.docx', '.html', '.htm', '.odt', '.pdf', '.xls', '.xlsx', '.ods', '.txt', '.ppt', '.pptx']
    ext_list_comp = ['.rar', '.zip', '.gz', '.tar', '.mar', '.sbx', '.iso', '.lz', '.7z', '.cab', '.dmg', '.jar',
                     '.tgz', '.wim', '.zipx']
    ext_list_exec = ['.exe', '.java', '.class', '.c', '.cpp', '.py', '.app', '.vb', '.scr', '.msi']
    for categ in dir_categ:
        if not os.path.exists(categ):
            os.makedirs(os.path.join(source_path, categ))
        else:
            pass
    for file in files:
        if os.path.isdir(file):
            pass
        elif os.path.isfile(file):
            if os.path.splitext(file)[1].strip() in ext_list_images:
                print(file)
                shutil.move(file, os.path.join(source_path,"Images"))
            elif os.path.splitext(file)[1].strip() in ext_list_audio:
                print(file)
                shutil.move(file, os.path.join(source_path, "Music"))
            elif os.path.splitext(file)[1].strip() in ext_list_video:
                print(file)
                shutil.move(file, os.path.join(source_path, "Videos"))
            elif os.path.splitext(file)[1].strip() in ext_list_doc:
                print(file)
                shutil.move(file, os.path.join(source_path, "Documents"))
            elif os.path.splitext(file)[1].strip() in ext_list_comp:
                print(file)
                shutil.move(file, os.path.join(source_path, "Compressed"))
            elif os.path.splitext(file)[1].strip() in ext_list_exec:
                print(file)
                shutil.move(file, os.path.join(source_path, "Programs"))
            else:
                print(file)
                shutil.move(file, os.path.join(source_path, "Miscellaneous"))


organize_path(r"D:\testing")