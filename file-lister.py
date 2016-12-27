'''script to list no of files and dirs in present working directory or custom path as well as sub dirs of that directories'''
import os
from argparse import ArgumentParser
from Queue import Queue
from sys import argv,setrecursionlimit
#setrecursionlimit(3000) if you get "maximum recursion depth exceeded" error enable this and set value > 1000 defaultvalue is 1000
q=Queue()

def files(pat):
	files=[x for x in os.listdir(pat) if not x.startswith(".") and os.path.isfile(os.path.join(pat,x))]
	return files

def directories(pat):
	dirs=[x for x in os.listdir(pat) if not x.startswith(".") and os.path.isdir(os.path.join(pat,x))]
	return dirs

def hid_fil(pat):
	hidden_files=[x for x in os.listdir(pat) if x.startswith(".") and os.path.isdir(os.path.join(pat,x))]
	return len(hidden_files)

def hid_dir(pat):
	hidden_dirs=[x for x in os.listdir(pat) if x.startswith(".") and os.path.isfile(os.path.join(pat,x))]
	return len(hidden_dirs)

def main(location):
	b=directories(location)
	for item in b:
		q.put(os.path.join(location,item))
	print "path =",location
	print "files =",len(files(location))
	if '-d' in argv[1:] or '--dir' in argv[1:]:
		print "directories =",len(directories(location))
	if '-f' in argv[1:] or '--hidden-file' in argv[1:]:
		print "Hidden files =",hid_fil(location)
	if '-hd' in argv[1:] or '--hidden-dir' in argv[1:]:
		print "Hidden directories =",hid_dir(location)
	while not q.empty():
		main(q.get())

if __name__=="__main__":
	if not argv[1:]:
		path=os.getcwd()
	if "-p" in argv[1:]:
	    path=argv[argv.index("-p")+1]
	elif "--path" in argv[1:]:
	    path=argv[argv.index("--path")+1]
	if path == ".":
		path=os.path.abspath(".")
	if path[0] =="/" or path[0:2] == "./" or path[0:3]=="../":
	    main(path)
	elif path[0].isalpha():
	    main(path)
