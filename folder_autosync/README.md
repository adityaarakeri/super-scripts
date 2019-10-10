# AutoSync 

## Overview:

This is a script to automatically sync a local folder with a remote folder on ssh server. 

## Why would you find that useful?

It is common for many projects to be developed and run in specific machine/os only accessible by ssh. While you can always ssh into the machine and use vim for coding, it is much more convenient to develop on your own laptop using IDE and run the project in the remote machine. 

## Prerequisites

* Install fswatch
```
sudo brew install fswatch
```

* Setup your ssh key so that you can ssh into remote server without an explicit password

## Usage 

* Start autosync as a background process  
```
nohup ./autosync.sh [path_to_local_folder] [ip address of your remote machine] [path_to_remote_folder]&
# e.g. nohup ./autosync.sh ~/project 192.168.0.3 /home/bob&
```

* Stop autosync  
```
./stopsync.sh
```
___
