#!/usr/bin/python

import os
import hashlib
import sys

pwned_passwords_file = "/home/josg/data/pwned-passwords-sha1-ordered-by-count-v4.txt"
#pwned_passwords_file = "/home/josg/data/test.txt"

def searchForPass(password):
    pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print("\nSearching for %s" %password ) 
  
    password_file = pwned_passwords_file
    print("Searching in: %s" % password_file)

    line_number = 0

    with open(password_file, "r") as file:
      for line in file:
        line_number = line_number + 1
        pwned_hash, pwned_count = line.split(":")
        #print("Found %s line %s" % (pwned_hash, line_number))

        if pwned_hash == pass_hash:
          print("Found: '%s' as %s on line %s" % (password, pwned_hash, line_number))
          return
        
    
    print("Not found, all clear!")

if len(sys.argv) != 2 :
  print ("Usage: python3 test.py <pw>")
nargs = len(sys.argv)
print ( " nargs %s" %nargs)

args = sys.argv
searchForPass(args[1])