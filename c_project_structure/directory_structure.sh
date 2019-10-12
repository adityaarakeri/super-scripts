#!/bin/bash

mkdir $1
cd $1
mkdir src include bin build doc
git init
touch .gitignore
printf "bin/*\nbuild/*" >> .gitignore
touch Makefile

