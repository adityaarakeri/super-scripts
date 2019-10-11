#!/bin/bash
# Author  : Luis M Pena
# Purpose : source file to include general functions. such as reset or main.
# That way I dont have to rewrite them.

function check_root {

  echo "You Are Currently using Bash $( bash --version )"

  if [ "$EUID" != 0 ];
  then echo -e "$_MSGERROR No Super User Access....Now Exiting..";

    exit 0;
  fi

}

function press_enter {

    echo ""
    echo -n "Press Enter To continue"
    read
    clear

}


function reset {
    main

}
