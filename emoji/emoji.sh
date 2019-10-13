#!/bin/sh

cat emoji_list | fzf | awk '{print $1}' | xclip -sel clip
