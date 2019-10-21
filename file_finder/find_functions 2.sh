#!/bin/bash
# Author  : Luis M Pena
# Purpose : Script that contains find functions.


function find_byroot {


	echo "Type in the name of config file or query to search entire root partition"
  echo "Searching root directory"

  _QUERY=
  read _QUERY
  find / -type f -name "$_QUERY"
  echo "Done ..."

}

function find_byetc {

	echo "Searching etc directory   "
	echo "Type in the name of config file OR Query to search /etc"

  _QUERY2=
  read _QUERY2

  find /etc |grep "$_QUERY2"
  echo "Done ..."
}

function find_bystring {

	echo "Search for a string or query inside a specified directory or file "
	echo "This will search for a STRING, not file. use two options 1 and 2 for that"

	echo "Type in location of directory"
  _DIR=
  read _DIR


	echo "Type in the STRING OR SUBSTRING"

	_QUERY3=
  read _QUERY3
  grep -Ri "$_QUERY3" * "$_DIR"
  #  grep -Ri 4/ * /
  # find 4 followed by / * everything in root /

}

function find_byusername {

	echo "Searching files by username"
	_USERQ=
	read _USERQ

	find / -user "$_USERQ"
}


function find_bygroup {

	echo " Searching for files related to group "
	_GROUPQ=
	read _GROUPQ

	find / -group "$_GROUPQ"

}

function find_byconfig {

	echo " Searching for all config files "
	find / . -type f -name "*.conf"

	echo "Done..."
}

function find_byextenstion {

	echo "Enter file extension. EX: .html .php .py"
	_EXTENSION=
	read _EXTENSION

	find / -type f -name "*$_EXTENSION"
	echo " Searching for files by extention "


}

function find_bycma {

	echo " Searching for files that have been created,modified,accessed in the last hour "

  echo "###############################"
	echo "find files CHANGED in last hour"
	find / -cmin -60

  echo "###############################"
  "finding files MODIFIED in last hour"
	find / -mmin -60

  echo "###############################"
	echo "find files ACCESSED in last Hour"
	find / -amin -60

}

function find_bylog {

	echo " Searching for all log files "
	find / . -type f -name "*.log"
	echo "Done..."

}

function find_bypro {

	echo "Type in Parameter you want to search for in running processes"
	_PRO=
	read _PRO
	ps -e |grep "$_PRO"

}

function find_allpro {

	echo "Displaying all Processes"
	ps -e |grep less

	echo "Displaying All services"
	service --status-all
	chconfig --list

}

function find_files {

    _FFCHOICE=
    echo "How would you like to search";

    echo "1) Search entire / FOR FILES";
    echo "2) Search /etc FOR FILES";
    echo "3) Search for a STRING or SUBSTRING inside a file or directory ";
    echo "4) Search for files created or related to username ";
    echo "5) Search for files created or related to groups";
		echo "6) Search for ALL CONFIG FILES";
		echo "7) Search for files by file extention";
    echo "8) Search for files created, modified or accessed in the last hour";
    echo "9) Search for logs";
		echo "10) Search For Running Proccesses"
		echo "11) Searcg All Running Proccesses and Services"

		read _FFCHOICE

case $_FFCHOICE in

    1) find_byroot; press_enter ;;
    2) find_byetc ; press_enter ;;
    3) find_bystring ; press_enter ;;
    4) find_byusername ; press_enter ;;
		5) find_bygroup; press_enter ;;
    6) find_byconfig ; press_enter ;;
    7) find_byextenstion ; press_enter ;;
    8) find_bycma ; press_enter ;;
    9) find_bylog ; press_enter ;;
		10) find_bypro; press_enter ;;
		11) find_allpro; press_enter ;;
    0) exit ;;
    *) echo "Enter a digit above and try not to break this program.";

      esac


}
