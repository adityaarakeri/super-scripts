#!/bin/sh
# Open my usual applications on PC startup

# Open a terminal window 
gnome-terminal --working-directory=$HOME &

# Open 2 vscode windows
# - first opens my Github working directory
# - second opens my notes directory
code $HOME/Workplace/Github &
code $HOME/Dropbox/Notebook &

# Open my web broswer (Google Chrome) and:
# - Open Gmail, Google Calendar and Google Keep 
sleep 5 && {
  google-chrome --new-window mail.google.com calendar.google.com keep.google.com &
}
