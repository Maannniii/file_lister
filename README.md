"""This is my first python project in bit bucket
I am a beginner in python i created this script based on my knowledge in the language
Actually i created this script initially to address my issue and then i want to make it public so that others can use it"""

#Description:
This script lists all the no of files,directories,hidden files,hidden directories under each directory by default.
I have also added support to command line arguments
Just run as python file-lister.py to list the no of files.directories,hidden files,hidden directories under each directory.

#Requirements:
Python 2.6+

#Instructions:
* Run as python file-lister.py to list the no of files.directories,hidden files,hidden directories under each directory.
* script without additional arguments gives outputs no of files,directories,hidden files,hidden directories recursively from present working directory.


#Argument details:
""" any argument with any value makes the script to skip the output of respective value """
-f,--file - makes the script to skip printing no of files.
-d,--dir - makes the script to skip printing no of directories.
-hf,--hidden-dir - makes the script to skip printing no of hidden files.
-hd,--hidden-dir - makes the script to skip printing no of hidden directories.
-p,--path - custom path to scan and print.

#Usage:
python file-lister.py
python file-lister.py -p "path to scan"
python file-lister.py -f "any value"