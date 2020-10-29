from datetime import datetime
import time
import os
from glob import glob
    #_time_list = []
_now = time.mktime(datetime.now().timetuple())
_file_name=""
for files in glob(os.getcwd()+'\\uplaods'+'/*.docx'):
    _file_name=files
    #_f_time = os.path.getmtime(_file_name) #get file creation/modification time
    #if _now - _f_time > 30:
    os.remove(_file_name)
        #os.remove('C:\\Users\\shubh\\Documents\\ARYU\\DocConv\\uplaods'+"\\Converted.pdf")
'''for files2 in glob('C:\\Users\\shubh\\Documents\\ARYU\\DocConv\\uplaods'+'/*.pdf'):
    _f_time = os.path.getmtime(files2)
    if _now - _f_time > 30:
        os.remove(files2)'''