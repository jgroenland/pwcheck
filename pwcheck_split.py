#!/usr/bin/python

# pwcheck by scanning splitted file. 
# Assumes pwsplit was run to split the file into smaller files per hashes (3 digits)

import os
import hashlib
import sys

# folder where password data files are stored. (Use pwsplit to create these files)
datafolder = "/home/josg/data/v8"

def searchForPass(password):
    pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print("\nSearching for %s" %password ) 
    #print("hash %s" %pass_hash)
    #print("hashstart %s" %pass_hash[0])
  
    password_file = datafolder + "/" + pass_hash [0:3]
    #print("Searching in: %s" % password_file)

    with open(password_file, "r") as file:
      for line in file:
        pwned_hash, pwned_count = line.split(":")
        
        if pwned_hash == pass_hash:
            print("Found: '%s' ; occurences: %s" % (password, pwned_count))
            file.close()
            return
    # else password was not found    
    print("Password not found\n")
    file.close()

# Main program
if len(sys.argv) == 2 :
  # passwd is passed via command line
  args = sys.argv
  searchForPass(args[1])
else :
  # ask for passwd until user wants to quit
  asknext = True
  while asknext :
    userinput = input( "Enter passwd (q to quit): ")
    if userinput == "q" :
      asknext = False
    else: 
      searchForPass (  userinput )
