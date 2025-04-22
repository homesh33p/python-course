import pathlib
import sys

def printpath():
	print(f"Inner sys.path: {sys.path}")
	print(f"Inner CWD: {pathlib.Path.cwd()}")