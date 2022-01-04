#!/usr/bin/python
#
# Check pwned file by using a shelve file
# 
import os
import hashlib
import sys
import shelve


shelve_file = "/home/josg/data/pwned-shelve.db"

d = shelve.open(shelve_file)

def searchForPass(password):
    pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print("\nSearching for %s" %password ) 
    line_number = d.get( pass_hash )
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
  # ask for passwd until user wants to quit
  asknext = True
  while asknext :
    userinput = input( "Enter passwd (q to quit): ")
    if userinput == "q" :
      asknext = False
    else: 
      searchForPass (  userinput )
 
d.close()