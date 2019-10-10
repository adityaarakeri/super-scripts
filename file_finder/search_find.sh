#!/bin/bash
# Author  : Luis M Pena
# Purpose : Script that manages the find functions

# Include source files
source general_functions.sh
source find_functions.sh

function main {

    echo "Search Interface"
    find_files

}

# Make sure this is ran as check
check_root

# Run Main Function
main
