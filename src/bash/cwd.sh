#!/bin/bash
# cwd = copy working directory
# for use in conjunction with .bash_aliases
# echo `pwd` `date` >> ~/.places.txt << prior version, dated command substitution syntax. not very unixy anymore.
echo $(pwd) $(date) >> ~/.places.txt
