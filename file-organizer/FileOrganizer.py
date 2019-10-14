import os
import shutil
import sys

docs = ['pdf','docx','xlsx','doc','odt','ipynb','md','csv']
torrent = ['torrent']
image = ['jpg','png','bmp']
video = ['mp4','avi','3gp','mpg','mov','mkv','m4v','flv']
audio = ['mp3','wav','ogg']

def group_files(path,filename):
    file_format = filename.split('.')[1].lower()
    if file_format in docs:
        folder = 'Documents'
    elif file_format in torrent:
        folder = 'Torrents'
    elif file_format in image:
        folder = 'Images'
    elif file_format in video:
        folder = 'Videos'
    elif file_format in audio:
        folder = 'Audios'
    else:
        folder = 'Others'
    
    try:
        shutil.move(path+filename, path+folder+'/'+filename)
    except IOError:
        os.makedirs(path+folder)
        shutil.move(path+filename, path+folder+'/'+filename)

if (len(sys.argv) != 2):
    print('Wrong command! Please use format "python3 FileOrganizer.py <directory to organize>"')
else:    
    path = sys.argv[1]
    files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
    files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ] #list comprehension version

    for f in files:
        group_files(path,f)