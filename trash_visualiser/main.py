import shutil

import winshell
import os

def ClearScreen():
    try:
        os.system("cls")
    except:
        os.system("clear")
    print("------------------------ TRASH VISUALISER CLI ------------------------")

def get_dir_size(self, start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

class DeletedObject:
    def __init__(self, obj, typeOfObj, name, sahiPath, size, addOn):
        self.obj = obj
        self.typeOfObj = typeOfObj
        self.name = name
        self.sahiPath = sahiPath
        self.size = size
        self.addOn = addOn

def Beginning(dictionary):
    ClearScreen()
    if dictionary is None:
        listOfItems=list(winshell.recycle_bin())

        dictOfObjects = {}
        fmt = "{0:3} | {1:8} | {2:10}"
        print(fmt.format("Sr:","Type:", "Name:"))
        for i, v in enumerate(listOfItems):
            serialNo = i+1
            path = v.original_filename()
            listOfPath = path.split("\\")
            newPath = "\\\\".join(listOfPath)
            winshell.undelete(path)
            name = listOfPath[-1]
            if os.path.isdir(newPath) == True:
                type = "Folder"
                size = get_dir_size(newPath)
                listOfFolderItems = os.listdir(newPath)
                noOfFolder = 0
                noOfFile = 0
                for i in listOfFolderItems:
                    checkpath = newPath+ '\\\\' + i
                    if os.path.isdir(checkpath) == True:
                        noOfFolder +=1
                    elif os.path.isfile(checkpath) == True:
                        noOfFile +=1
                dictOfObjects[serialNo] = DeletedObject(v, type , name, newPath, "{0:.1f}".format(size/1024), [noOfFile, noOfFolder])
            elif os.path.isfile(newPath) == True:
                type = "file"
                size = os.path.getsize(newPath)
                dictOfObjects[serialNo]= DeletedObject(v, type, name, newPath, "{0:.1f}".format(size/1024), [])
            winshell.delete_file(path)
            print(fmt.format(serialNo,type,name))
        SelectedItem(dictOfObjects)
    else:
        fmt = "{0:3} | {1:8} | {2:10}"
        print(fmt.format("Sr:", "Type:", "Name:"))
        for k,v in dictionary.items():
            print(fmt.format(k, v.typeOfObj, v.name))
        SelectedItem(dictionary)


def SelectedItem(dict):
    print("Enter serial no of the file/folder you want to select")
    n = eval(input("Enter: "))
    ClearScreen()
    try:
        Obj= dict[n]
        print("Name: ", Obj.name )
        print("Path: ", Obj.obj.original_filename())
        print("Type: ", Obj.typeOfObj)
        print("Size: ", Obj.size)
        if Obj.addOn == []:
            pass
        else:
            print("No of files: ",Obj.addOn[0])
            print("No of Folders: ", Obj.addOn[1])
        OperationOnItem(Obj, dict)

    except:
        print("Please enter a valid serial no.")
        SelectedItem(dict)

def OperationOnItem(Obj, dict):
    print(" Press O to open the ", Obj.typeOfObj, " \n Press D to delete the ", Obj.typeOfObj,
          " \n Press R to restore the ", Obj.typeOfObj, "\n Press B to go back")
    raw_input = input("Enter: ")
    if raw_input == "O" or raw_input == "o":
        if Obj.typeOfObj == "file":
            ClearScreen()
            OpenFile(Obj,dict)
        elif Obj.typeOfObj == "Folder":
            ClearScreen()
            OpenFolder(Obj,dict)
    elif raw_input == "D" or raw_input == "d":
        DeleteItem(Obj)
    elif raw_input == "R" or raw_input == "r":
        RestoreItem(Obj)
    elif raw_input == "B" or raw_input == "b":
        Beginning(dict)


def OpenFile(obj, dict):
    try:
        winshell.undelete(obj.obj.original_filename())
        file= open(obj.sahiPath, 'r')
        R=file.read()
        file.close()
        winshell.delete_file(obj.obj.original_filename())
        print(R)
        print("Press any key to go back")
        key= input("Enter: ")
        if key != '':
            ClearScreen()
            OperationOnItem(obj, dict)
    except:
        ClearScreen()
        print("This file can not be opened ")
        OperationOnItem(obj, dict)



def DeleteItem(obj):
    winshell.undelete(obj.obj.original_filename())
    if obj.typeOfObj == "File":
        os.remove(obj.sahiPath)
    elif obj.typeOfObj == "Folder":
        shutil.rmtree(obj.sahiPath)
    Beginning(None)

def RestoreItem(obj):
    winshell.undelete(obj.obj.original_filename())
    Beginning(None)

def OpenFolder(obj, dict):
    winshell.undelete(obj.obj.original_filename())
    listOfDirs = os.listdir(obj.sahiPath)
    winshell.delete_file(obj.obj.original_filename())
    fmt = "{0:3} | {1:8} | {2:10}"
    print(fmt.format("Sr:", "Type:", "Name:"))
    Sr=0
    for i in listOfDirs:
        Sr+=1
        if "." in i:
            type = "file"
        else:
            type = "Folder"
        print(fmt.format(Sr, type, i))
    print(" Enter serial no to open any file/folder \n Press B to go back ")
    n = input("Enter: ")
    if str(n) == "B" or str(n) == "b":
        Beginning(dict)
    else:
        try:
            n= eval(n)
            name = listOfDirs[n-1]
            path = obj.sahiPath + "\\\\" + listOfDirs[n - 1]
            if "." in name:
                ClearScreen()
                OpenFileFromFolder(obj, path, dict)
            else:
                ClearScreen()
                OpenFolderFromFolder(obj, path, dict)
        except:
            ClearScreen()
            print(" Enter a valid serial no ")
            OpenFolder(obj, dict)

def OpenFileFromFolder(obj, filepath, dict):
    try:
        winshell.undelete(obj.obj.original_filename())
        file= open(filepath, "r")
        R= file.read()
        file.close()
        winshell.delete_file(obj.obj.original_filename())
        print(R)
        print(" Press any key to go back ")
        key = input(" Enter: ")
        if key:
            ClearScreen()
            OpenFolderFromFolder(obj, "\\\\".join(filepath.split("\\\\")[:-1]), dict)
    except:
        ClearScreen()
        print(" This file can not be opened ")
        OpenFolderFromFolder(obj, "\\\\".join(filepath.split("\\\\")[:-1]), dict)

def OpenFolderFromFolder(obj, folderpath, dict):
    winshell.undelete(obj.obj.original_filename())
    listOfDirs = os.listdir(folderpath)
    winshell.delete_file(obj.obj.original_filename())
    fmt = "{0:3} | {1:8} | {2:10}"
    print(fmt.format("Sr:", "Type:", "Name:"))
    Sr = 0
    for i in listOfDirs:
        Sr += 1
        if "." in i:
            type = "file"
        else:
            type = "Folder"
        print(fmt.format(Sr, type, i))
    print(" Enter serial no to open any file/folder \n Press B to go back ")
    n= eval(input("Enter: "))
    if str(n) == "B" or str(n) == "b":
        if obj.sahiPath == folderpath:
            Beginning(dict)
        else:
            ClearScreen()
            OpenFolderFromFolder(obj, "\\\\".join(folderpath.split("\\\\")[:-1]), dict)
    else:
        try:
            name = listOfDirs[n - 1]
            path = folderpath + "\\\\" + listOfDirs[n - 1]
            if "." in name:
                ClearScreen()
                OpenFileFromFolder(obj, path, dict)
            else:
                ClearScreen()
                OpenFolderFromFolder(obj, path, dict)
        except:
            ClearScreen()
            print(" Enter a valid serial no ")
            OpenFolderFromFolder(obj, folderpath, dict)


Beginning(None)
