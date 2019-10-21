import os, sys, ctypes
import subprocess as sp

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    
    py_path = os.getcwd()

    f=open("update.bat","w+")
    f.write("setx /m Path \"%Path%" + py_path + ";" + py_path+"\Scripts;\"\n")
    #f.write("pause")
    f.close()

    sp.call("update.bat")

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
