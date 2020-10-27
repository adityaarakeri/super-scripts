#!/bin/bash

columns="$1"

# With no arguments, prints all the columns
if [[ ! $# -eq 0 ]]; then
	columns="$"$(echo "$@" | cut -d" " -f1-100 | sed "s/ /\"\\\\t\" \$/g")
fi

awk -F'\t' '{ print '"$columns"' }' < /dev/stdin