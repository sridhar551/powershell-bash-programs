#!/bin/bash
echo "Enter filename to remove"
read fn
rm -i $fn
echo $((1 + $RANDOM % 10))

