#!/bin/bash/python3

import os
import time
import getpass

HOST=input("Enter Host IP: ")
PORT=input('Port Number for mysql: ')

database=input("Enter DATABASE Name  --->  ")
USER=input("Enter the username :")
Pass=getpass.getpass()
isDir=os.path.isdir('backup_mysql')
Directory = "backup_mysql"

if isDir:
  print('Directory already exists and dump will be stored in '+os.environ[ 'HOME' ]+'/'+Directory)

else:
  
  print('Making Directory')
  print('Directory created  and dump will be stored in '+os.environ[ 'HOME' ]+'/'+Directory)
  os.mkdir(Directory)

def getdump(database):
    file = time.strftime("%Y-%m-%d-%I")
    os.chdir(Directory)    
    os.popen("mysqldump -h %s -P %s -u %s -p%s %s --set-gtid-purged=OFF | gzip > %s.sql.gz" % (HOST,PORT,USER,Pass,database,database+"_"+file))
    print("\n|| Data base dumped to "+database+"_"+file+".sql.gz ||")
    
if __name__=="__main__":

    getdump(database)