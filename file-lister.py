'''script to list no of files and dirs in present working directory or custom path as well as sub dirs of that directories'''
import os
from argparse import ArgumentParser
from Queue import Queue
from sys import argv
q=Queue()
arg=""

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
	print "path = ",location
	if not arg.file:
		print "files = ",len(files(location))
	if not arg.dir:
		print "directories = ",len(directories(location))
	if not arg.hidden_file:
		print "Hidden files = ",hid_fil(location)
	if not arg.hidden_dir:
		print "Hidden directories = ",hid_dir(location)
	while not q.empty():
		main(q.get())

if __name__=="__main__":
	pars=ArgumentParser()
	pars.add_argument('-f','--file',help=" if not required",required=False)
	pars.add_argument('-d','--dir',help="0 if not required",required=False)
	pars.add_argument('-hf','--hidden-file',help="0 if not required",required=False)
	pars.add_argument('-hd','--hidden-dir',help="0 if not required",required=False)
	pars.add_argument('-p','--path',help="custom path to directory",required=False)
	globals()['arg']=pars.parse_args()
	if not arg.path:
		arg.path=os.getcwd()
	if arg.path == ".":
		arg.path=os.path.abspath(".")
	main(arg.path)
