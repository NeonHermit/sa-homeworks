#!/bin/bash

read -p "Enter a file or dir pathname: " name

if [ -f "$name" ]
then
    echo "$name is a file."
    ls -l "$name"
elif [ -d "$name" ]
then
    echo "$name is a directory."
    ls -l "$name"
else
    echo "$name is another type of file."
fi
