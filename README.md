***"""This is my first python project in bit bucket. 
I am a beginner in python i created this script based on my knumberwledge in the language. 
Actually i created this script initially to address my issue and then i want to make it public so that others can use it"""***

#Description:
This script lists all the number of files,directories,hidden files,hidden directories under each directory by default.
I have also added support to command line arguments
Just run as python file-lister.py to list the number of files,directories,hidden files,hidden directories under each directory.

#Requirements:
Python 2.6+

#Instructions:
* Run as python file-lister.py to list the number of files,directories,hidden files,hidden directories under each directory.
* script without additional arguments gives outputs number of files,directories,hidden files,hidden directories recursively from working directory.

#Usage:
* python file-lister.py [OPTION]
* -f,--file - prints number of files.
* -d,--dir - prints number of directories.
* -hf,--hidden-dir - prints number of hidden files.
* -hd,--hidden-dir - prints number of hidden directories.
* -p,--path - custom path to scan and print.

#numberte:
if you get "maximum recursion depth exceeded" error enable this and set value > 1000 defaultvalue is 1000
