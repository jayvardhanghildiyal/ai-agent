#!/bin/bash

# run the calc script

echo add a math query ! add spaces before and after the operand

read QUERY

uv run calculator/main.py $QUERY