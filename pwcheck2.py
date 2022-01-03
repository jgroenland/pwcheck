#!/usr/bin/python
#
# Check pwned file by using a dict
# note this doesn work
#   Memory full after 44.739.242 records, while file contains 613.584.246 lines

import os
import hashlib
import sys

pwned_passwords_file = "/home/josg/data/pwned-passwords-sha1-ordered-by-count-v7.txt"
#pwned_passwords_file = "/home/josg/data/test.txt"

# pwhash is the dict with hashes
pwhash = { }

def readPassfile():
    password_file = pwned_passwords_file

    line_number = 0

    with open(password_file, "r") as file:
      for line in file:
        line_number = line_number + 1
        hash = line.split(":")
        pwhash.update( { hash[0] : line_number } )
        print (line_number)



def searchForPass(password):
    pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print("\nSearching for %s" %password ) 
    line_number = pwhash.get( pass_hash )
    if line_number :
        print("Password found on line %s" %line_number )
    else:
        print( "Password not found")

# Main program
if len(sys.argv) == 2 :

  # passwd is passed via command line
  args = sys.argv
  searchForPass(args[1])

else :
  # read file
  print("Reading file ..")
  readPassfile()
  print("Done")

  # ask for passwd until user wants to quit
  asknext = True
  while asknext :
    userinput = input( "Enter passwd (q to quit): ")
    if userinput == "q" :
      asknext = False
    else: 
      searchForPass (  userinput )
