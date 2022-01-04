#!/usr/bin/python
#
# Convert pwned file to a shelve
#  Doesnt work in practice, takes too long to process
# 
import os
import hashlib
import sys
import shelve

pwned_passwords_file = "/home/josg/data/pwned-passwords-sha1-ordered-by-count-v7.txt"
#pwned_passwords_file = "/home/josg/data/test.txt"

shelve_file = "/home/josg/data/pwned-shelve.db"

d = shelve.open(shelve_file)

def readPassfile():
    password_file = pwned_passwords_file

    line_number = 0
    cnt = 0

    with open(password_file, "r") as file:
      for line in file:
        line_number = line_number + 1
        cnt = cnt + 1
        hash = line.split(":")
        d [ hash[0] ] = line_number
        if cnt == 1000000 :
            print (line_number)
            cnt = 0


# read file
print("Reading file ..")
readPassfile()
print("Done")

d.close()