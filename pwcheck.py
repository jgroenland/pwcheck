#!/usr/bin/python

# pwcheck by scanning file. 
# This is the simplest approach however can take a long time when a password is not found as it still needs to scan the whole file

import os
import hashlib
import sys

pwned_passwords_file = "/home/josg/data/pwned-passwords-sha1-ordered-by-hash-v8.txt"
#pwned_passwords_file = "/home/josg/data/pwned-passwords-sha1-ordered-by-count-v7.txt"
#pwned_passwords_file = "/home/josg/data/test.txt"

def searchForPass(password):
    pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print("\nSearching for %s" %password ) 
    #print("hash %s" %pass_hash)
    #print("hashstart %s" %pass_hash[0])
  
    password_file = pwned_passwords_file
    #print("Searching in: %s" % password_file)

    with open(password_file, "r") as file:
      for line in file:
        
        #first check for 1st digit match, to speed up comparison
        if line[0] == pass_hash[0] :
          pwned_hash, pwned_count = line.split(":")
          #print("Found %s, occurrences: %s" % (pwned_hash, pwned_count))

          if pwned_hash == pass_hash:
            print("Found: '%s' as %s occurrences: %s" % (password, pwned_hash, pwned_count))
            return
        
    
    print("Password not found")

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


