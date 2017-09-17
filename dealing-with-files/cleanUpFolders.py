#! /usr/bin/env python3
"""
cleanUpFolder.py v1.1 - 2017 Copyright: TheSpatializer - Apache License 2.0
This script has been written in Python 3.5 and can be used for educational purpose only.
Edition is encouraged as well as remarks and ideas for future improvement.
Source : 
Please, link the source of the code you use and do not try to make money out of others' work.
------------------------------Credits----------------------------
Cheers to Martin Thoma (https://stackoverflow.com/users/562769/martin-thoma)
for his answer on this thread: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
"""
from os import listdir, remove
from os.path import isfile, join

def cleanFilesList(filesList):
	filesList.remove("cleanUpFolders.py")
	for i in filesList:
		if i[0]=='.':
			filesList.remove(i)
	return(files)

def areThereFolders(onlyFiles,foldContent):
	if len(onlyFiles)<len(foldContent):
		ret=len(foldContent)-len(onlyFiles)
	elif len(onlyFiles)==len(foldContent):
		ret=0
	else:
		ret="Error 42"
	return(ret)

# Change value for the directory you want to clean
folder="/Users/webmaster/Downloads/test"

# Create list of all unhidden files in the folder
files = [f for f in listdir(folder) if isfile(join(folder, f))]
cleanFilesList(files)
# Create list of all the first level unhidden content in the folder
filesxfolders = listdir(folder)
cleanFilesList(filesxfolders)
# Comparing lists to detect folders
nbFolders=areThereFolders(files,filesxfolders)

# Avoiding problems
if type(nbFolders) is str:
	input("There seems to be a problem here, don't want to know about it!\nPress Enter to leave!!")

else:
	# The folder is empty of files
	if len(files)==0:
		print("There does not seem to be any file in this directory.")
		# See below --> l.78
		if nbFolders>0:
			if nbFolders<2:
				print("\n"+str(nbFolders)+" folder has been detected in this directory.")
			elif nbFolders>1:
				print("\n"+str(nbFolders)+" folders have been detected in this directory.")
			print("This version of the program doesn't allow to purge them,")
			print("you will have to do it yourself.\n")
		#Bye-bye
		input("Press Enter to leave...")
	
	# The user is not dumb
	else:
		# Some little chit-chat!
		print("Do you want the following files to be deleted?:")
		for i in files:
			print(i)
		ans=''
		while ans!='y' and ans!='n':
			ans = input("(y/n): ")
		
		if ans=='y':
			# Deleting files (only files)
			for i in files:
				remove(folder+"/"+i)
			print("\nThe files have been removed from your computer.")
			
			# [Work in progress] About subdirectories
			if nbFolders>0:
				if nbFolders<2:
					print("\n"+str(nbFolders)+" folder has been detected in this directory.")
				elif nbFolders>1:
					print("\n"+str(nbFolders)+" folders have been detected in this directory.")
				print("This version of the program doesn't allow to purge them,")
				print("you will have to do it yourself.\n")
			#Bye-bye
			input("Press Enter to leave...")
		
		elif ans=='n':
			# Why even run the script?!
			input("\nPress Enter to leave.")
