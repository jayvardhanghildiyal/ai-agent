#!/bin/bash

# to run the main.py file
echo -e "\nwhat is it you wish to ask ?"

read QUESTION

uv run main.py $QUESTION
