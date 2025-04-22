import sys

from .listChecker import checkList

def sumMyList(obj):
	obj = checkList(obj)
	return sum(obj)

# print(__name__)

if __name__=="__main__":
	# print(f"As script: {__name__}")
	# print(sys.path)
	mysum = sumMyList([1,3])
	print(mysum)