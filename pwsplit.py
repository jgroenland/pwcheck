#!/usr/bin/python
#
# Convert pwned file to a set of smaller files
# Assumes file is ordered by hash
# 
import os
import sys


pwned_passwords_file = "/home/josg/data/pwned-passwords-sha1-ordered-by-hash-v8.txt"
#pwned_passwords_file = "/home/josg/data/test.txt"

# folder where split files will be stored. Clear directory before starting job
datafolder = "/home/josg/data/v8"

# Read the password file and split
def readPassfile():
    password_file = pwned_passwords_file

    oldhash = "---"
    
    # open splitfile so first close wont give error
    splitfile = datafolder + "/" + "000" 
    spfile = open ( splitfile, "w")

    with open(password_file, "r") as pwfile:
      for line in pwfile:
        # look at first 3 chars
        hash = line [0:3]
        if hash == oldhash :
            # write line to file
            spfile.write(line)
        else :
            # close previous file
            spfile.close()
            # open new file and write line
            splitfile = datafolder + "/" + hash   
            spfile = open ( splitfile, "w")
            spfile.write (line )
            oldhash = hash
            print ( oldhash )
    pwfile.close()
    spfile.close()


# Main program
print("Reading file ..")
readPassfile()
print("Done")
