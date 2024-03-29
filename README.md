# pwcheck
Offline check for passwords in haveibeenpwned. Can be used if you dont want to expose your password to the haveibeenpwned website or API.

version 1.2; 
Jos Groenland

Python scripts to check if a password is existing in the haveibeenpwned database.
You need to download the file first from https://haveibeenpwned.com/Passwords

There are two versions: a brute force that just scans for the file, and a more intelligent one that uses splitted files.



## Pwcheck - brute force using one large file

For this you should download the `SHA-1`, `ordered by prevalence` file. Note that `ordered by hash` also works but is slower in finding obvious passwords.  
Use `pwcheck.py` to simply scan through the downloaded file. This can take a long time but it can be practical when you just want to check a single password.

## Pwcheck_split - use smaller splitted files

You need to download the file in `SHA-1` format, `ordered by hash`. First split the downloaded files into smaller ones, using `pwsplit.py`.  
Then use `pwcheck_split.py` to check passwords.

## Other versions
Moved to folder `old`. These methods turned out to be not usable in practise due to the large number of records in the password file.

`Pwcheck2` is using dict.  `Pwcheck 3` is using a shelve file.