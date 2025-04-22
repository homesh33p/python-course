# File operations-
# 	os, path, Read, Write, append, encoding
# 	pathlib
# 		refer: https://stackabuse.com/introduction-to-the-python-pathlib-module/
#		https://docs.python.org/3/library/pathlib.html
# 		https://realpython.com/python-pathlib/
#	shutil:
# 		https://docs.python.org/3/library/shutil.html

import pathlib
import shutil

# #current working directory
# print(f"Current working directory: {pathlib.Path.cwd()}")

# # Working with paths:
# dirpath = pathlib.Path(r"C:\Shared")
# filepath = pathlib.Path(r"C:\Shared\UbuntuTrusty\Marion Thornton - Classical Dynamics of Particles and Systems.pdf")
# print(filepath)
# print(f"relative: {filepath.relative_to(dirpath)}")
#
# # getting filename, suffix
# print(f"full filename: {filepath.name}")
# print(f"filename only: {filepath.stem}")
# print(f"Suffix: {filepath.suffix}")
# #
# #Check if it is a file or folder:
# print(filepath.is_dir())
# print(filepath.is_file())

# #or we can also use relative paths:
# workingdir = pathlib.Path.cwd()
# brazil = pathlib.Path(r"South America\Brazil")
# print(brazil)
# print(brazil.absolute())

# # you can also get the parents:
# print(brazil.parent)
# print(brazil.absolute().parent)
# print(brazil.absolute().parent.parent)


# #read from text files
filepath = pathlib.Path.cwd() / 'toreadfrom.txt'
buffer = open(filepath,mode='r')
lines = buffer.read()
print(lines)
buffer.close()

# # #or
# with open(filepath,mode='r') as buffer:
# 	lines = buffer.read()
# 	print(lines)

# #read line by line
# with open(filepath,mode='r') as buffer:
# 	line = buffer.readline()
# 	print(line)
#
# #read line and store in an array:
# linesArr = []
# with open(filepath,mode='r') as buffer:
# 	line = buffer.readline()
# 	while line:
# 		linesArr.append(line)
# 		line = buffer.readline()
# print(linesArr)
#
# #or you can use pathlib library to read directly:
# linesArr.clear()
# lines = filepath.read_text()
# print(lines)
#
# #writing into files:
# newFilePath = pathlib.Path("towriteinto.txt")
# with newFilePath.open(mode="w") as buffer:
# 	buffer.write("We have bugun writing into files!")
#
# # but be careful of the mode, "w" will overwrite existing files"
# newFilePath = pathlib.Path("towriteinto.txt")
# with newFilePath.open(mode="w") as buffer:
# 	buffer.write("Its been overwritten")
# #
# #to avaoid overwriting, we use append mode:
# newFilePath = pathlib.Path("towriteinto.txt")
# with newFilePath.open(mode="a") as buffer:
# 	buffer.write("Now its appending!")
#
# #to write line by line use:
# with newFilePath.open(mode="a") as buffer:
# 	buffer.writelines("Now its appending!")
# #
# #or
# with newFilePath.open(mode="a") as buffer:
# 	buffer.writelines(["\nNow its appending!","\nCongratulations!!"])


#Note: there are different modes of wrtiting or reading a file
# ex: read, readbytes, write, writebytes, writetext, writeappend, append, and many more
# Research and try out in your own time


# #rename files:
# # Rename this file or directory to the given target,
# #  and return a new Path instance pointing to target.
# source = pathlib.Path("source.txt")
# dest = pathlib.Path("destination.txt")
# dest = source.replace(target=dest)
# print(dest)

#Copy file:
# #but be careful, because if the destination already exists,
# #  it will be overwritten
# source = pathlib.Path("source.txt")
# dest = pathlib.Path("destination.txt")
# shutil.copy(src=source,dst=dest)
#
# # to avoid overwriting, check if file exists first:
# source = pathlib.Path("source.txt")
# dest = pathlib.Path("destination.txt")
# if not dest.exists():
# 	shutil.copy(src=source,dst=dest)

# #deleting a file:
# # Note: Be careful of the file permissions, or will throw an error
# targetpath = pathlib.Path("destination.txt")
# targetpath.unlink()


# #Creating directory:
folderpath = pathlib.Path("South America")
# folderpath.mkdir()
# #
# #Combining paths:
# folderpath = folderpath / "Brazil"
# print(folderpath)
# folderpath.mkdir()

# Note: this will create a directory only if it does not exist,
# Else will throw error
# to avoid, use exists_ok=True

# #Combining paths:
# folderpath = folderpath / "Brazil"
# print(folderpath)
# folderpath.mkdir(exist_ok=True)

folderpath = folderpath / "Argentina" / "Buenos Aires"
# print(folderpath)
# try:
# 	folderpath.mkdir()
# except Exception as err:
# 	print(err)

# Parent folder does not exist, so use parents=True
# to create the entire structure
# folderpath.mkdir(parents=True)

# Deleting a folder:
# # will work only if folder is empty
# # Also will throw error when the folder is not empty
# try:
# 	folderpath.rmdir()
# except Exception as err:
# 	print(err)

# try:
# 	shutil.rmtree(folderpath)
# except Exception as err:
# 	print(err)

'''--------------------------------------------------------'''
#lets try in a different folder:
# folderpath = pathlib.Path("C:\Shared\Python_offering_test_area")
# folderpath = folderpath / "Brazil"
# folderpath = folderpath / "Argentina" / "Buenos Aires"
# folderpath.mkdir(parents=True,exist_ok=True)
# folderpath = folderpath.parent / "Patagonia"
# folderpath.mkdir(parents=True,exist_ok=True)
# try:
# 	print(f"removing folder: {folderpath}")
# 	folderpath.rmdir()
# except Exception as err:
# 	print(err)

# folderpath = folderpath.parent.parent
# print(f"folder path: {folderpath}")
# try:
# 	print(f"removing the entire folder tree: {folderpath}")
# 	shutil.rmtree(folderpath)
# except Exception as err:
# 	print(err)

#Note: Shutil.rmtree will remove folders recursively,
# meaning, it will remove the entire folder tree inside that folder

# #iterating a directory:
# rootdir = 'South America'
# print(list(pathlib.Path(rootdir).iterdir()))
# for path in pathlib.Path(rootdir).iterdir():
# 	if path.is_dir():
# 		print(path)

# #simple recursion:
# def listdirs(rootdir):
# 	for path in pathlib.Path(rootdir).iterdir():
# 		if path.is_dir():
# 			print(path)
# 			listdirs(path)

# rootdir = 'South America'
# listdirs(rootdir)

''' iterating using method glob:
refer:https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob

Glob the given relative pattern in the directory represented by this path,
yielding all matching files (of any kind):'''

# folderpath = pathlib.Path(r"C:\Users\utsos\Google Drive (utsosg.ed@gmail.com)\Python Offering")
# pyfiles = folderpath.glob("*.py")
# # print(pyfiles)
# for file in pyfiles:
# 	print(file)

# #The “**” pattern means
# # “this directory and all subdirectories, recursively”.
# # In other words, it enables recursive globbing:
# folderpath = pathlib.Path(r"C:\Users\utsos\Google Drive (utsosg.ed@gmail.com)\Python Offering")
# pyfiles = folderpath.glob('**/*.*')
# print(pyfiles)
# for file in pyfiles:
# 	print(file)

# all folders and files:
folderpath = pathlib.Path(r"C:\Users\utsos\Google Drive (utsosg.ed@gmail.com)\Python Offering")
pyfiles = folderpath.glob('**/*')
print(pyfiles)
for file in pyfiles:
	print(file)



